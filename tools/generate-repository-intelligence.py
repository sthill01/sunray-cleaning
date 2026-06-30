from __future__ import annotations

import html
import json
import re
import runpy
import subprocess
from collections import Counter
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse


ROOT = Path(__file__).resolve().parents[1]
REPORTS = ROOT / "reports"
REPORT_DATA = REPORTS / "data"
BUILD_SCRIPT = ROOT / "tools" / "build-cloudflare-preview.py"

CORE_LOCATIONS = [
    "Park City",
    "Heber City",
    "Midway",
    "Kamas",
    "Deer Valley",
    "Canyons Village",
    "Summit County",
    "Wasatch County",
]

SERVICE_TARGETS = [
    ("Residential", ["residential cleaning", "house cleaning", "home cleaning"]),
    ("Airbnb/VRBO", ["airbnb", "vrbo", "short-term rental", "vacation rental"]),
    ("Deep cleaning", ["deep cleaning", "deep clean"]),
    ("Recurring", ["recurring", "weekly", "biweekly", "monthly"]),
    ("Move-in/out", ["move-in", "move-out", "move in", "move out"]),
    ("Luxury", ["luxury", "high-end"]),
]


def normalize_text(value: object) -> str:
    text = html.unescape("" if value is None else str(value))
    text = re.sub(r"<[^>]+>", " ", text)
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\u00a0": " ",
        "\u2122": "TM",
        "\u00ae": "(R)",
        "\u00a9": "(C)",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = re.sub(r"\s+", " ", text).strip()
    return text.encode("ascii", "ignore").decode("ascii")


def slugify(value: object) -> str:
    text = normalize_text(value).lower().replace("&", " and ")
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "all"


def word_count(value: str) -> int:
    return len(re.findall(r"\b[a-zA-Z][a-zA-Z0-9'-]*\b", value))


def markdown_cell(value: object) -> str:
    text = normalize_text(value)
    return text.replace("|", "\\|")


def md_table(headers: list[str], rows: list[list[object]]) -> str:
    if not rows:
        return "No rows.\n"
    header = "| " + " | ".join(markdown_cell(item) for item in headers) + " |"
    divider = "| " + " | ".join("---" for _ in headers) + " |"
    body = [
        "| " + " | ".join(markdown_cell(item) for item in row) + " |"
        for row in rows
    ]
    return "\n".join([header, divider, *body]) + "\n"


def write_report(name: str, body: str) -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    path = REPORTS / name
    path.write_text(body.rstrip() + "\n", encoding="utf-8")


def write_json(name: str, data: object) -> None:
    REPORT_DATA.mkdir(parents=True, exist_ok=True)
    path = REPORT_DATA / name
    path.write_text(json.dumps(data, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def report_date() -> str:
    return datetime.now(timezone.utc).date().isoformat()


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_parts: list[str] = []
        self.in_title = False
        self.current_heading: str | None = None
        self.heading_parts: list[str] = []
        self.headings: list[tuple[str, str]] = []
        self.in_summary = False
        self.summary_parts: list[str] = []
        self.summaries: list[str] = []
        self.in_json_script = False
        self.script_parts: list[str] = []
        self.schema_scripts: list[str] = []
        self.ignore_depth = 0
        self.text_parts: list[str] = []
        self.links: list[str] = []
        self.images: list[dict[str, str]] = []
        self.meta: dict[str, str] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr = {key.lower(): value or "" for key, value in attrs}
        if tag == "title" and not self.title_parts:
            self.in_title = True
        elif tag in {"h1", "h2", "h3"}:
            self.current_heading = tag
            self.heading_parts = []
        elif tag == "summary":
            self.in_summary = True
            self.summary_parts = []
        elif tag == "a" and attr.get("href"):
            self.links.append(attr["href"])
        elif tag == "img":
            self.images.append(
                {
                    "src": attr.get("src", ""),
                    "alt": attr.get("alt", ""),
                    "width": attr.get("width", ""),
                    "height": attr.get("height", ""),
                }
            )
        elif tag == "meta":
            key = attr.get("name") or attr.get("property")
            if key:
                self.meta[key.lower()] = attr.get("content", "")
        elif tag == "script":
            if attr.get("type", "").lower() == "application/ld+json":
                self.in_json_script = True
                self.script_parts = []
            else:
                self.ignore_depth += 1
        elif tag == "style":
            self.ignore_depth += 1

    def handle_data(self, data: str) -> None:
        if self.in_json_script:
            self.script_parts.append(data)
            return
        if self.ignore_depth:
            return
        if self.in_title:
            self.title_parts.append(data)
        if self.current_heading:
            self.heading_parts.append(data)
        if self.in_summary:
            self.summary_parts.append(data)
        self.text_parts.append(data)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self.in_title = False
        elif tag == self.current_heading:
            self.headings.append((tag, normalize_text(" ".join(self.heading_parts))))
            self.current_heading = None
            self.heading_parts = []
        elif tag == "summary":
            self.summaries.append(normalize_text(" ".join(self.summary_parts)))
            self.in_summary = False
            self.summary_parts = []
        elif tag == "script":
            if self.in_json_script:
                self.schema_scripts.append("".join(self.script_parts).strip())
                self.in_json_script = False
                self.script_parts = []
            elif self.ignore_depth:
                self.ignore_depth -= 1
        elif tag == "style" and self.ignore_depth:
            self.ignore_depth -= 1

    @property
    def title(self) -> str:
        return normalize_text(" ".join(self.title_parts))

    @property
    def text(self) -> str:
        return normalize_text(" ".join(self.text_parts))

    def heading(self, level: str) -> str:
        for tag, text in self.headings:
            if tag == level:
                return text
        return ""


def parse_html(content: str) -> PageParser:
    parser = PageParser()
    parser.feed(content)
    parser.close()
    return parser


def load_build_context() -> dict[str, object]:
    return runpy.run_path(str(BUILD_SCRIPT), run_name="sunray_build_context")


def schema_types_from_scripts(scripts: list[str]) -> list[str]:
    types: list[str] = []

    def add_type(value: object) -> None:
        if isinstance(value, str):
            types.append(value)
        elif isinstance(value, list):
            for item in value:
                add_type(item)

    def walk(node: object) -> None:
        if isinstance(node, dict):
            add_type(node.get("@type"))
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)

    for script in scripts:
        try:
            data = json.loads(script)
        except json.JSONDecodeError:
            continue
        walk(data)
    return sorted(set(types))


def normalize_internal_link(current_route: str, href: str) -> str | None:
    href = href.strip()
    if not href or href.startswith("#"):
        return None
    if href.startswith(("tel:", "sms:", "mailto:", "data:", "javascript:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme in {"http", "https"} and parsed.netloc not in {
        "sunray-cleaning.com",
        "www.sunray-cleaning.com",
        "sunray-cleaning-preview.pages.dev",
    }:
        return None

    base = "https://sunray.local" + current_route
    absolute = urlparse(urljoin(base, href))
    path = absolute.path or "/"
    if path.startswith("/assets/") or path.startswith("/api/"):
        return None
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    elif path.endswith(".html"):
        path = path[: -len(".html")] + "/"
    if "." in Path(path).name:
        return None
    if not path.startswith("/"):
        path = "/" + path
    if not path.endswith("/"):
        path += "/"
    return path


def route_label(route: str, context: dict[str, object]) -> str:
    label_func = context.get("route_label")
    if callable(label_func):
        return str(label_func(route))
    return route.strip("/").replace("-", " ").title() or "Home"


def page_kind(route: str, context: dict[str, object]) -> str:
    page_type = context.get("page_type")
    if callable(page_type):
        return str(page_type(route))
    if route.startswith("/services/"):
        return "service"
    if route.startswith("/service-location/"):
        return "location"
    if route.startswith("/blog/"):
        return "blog"
    return "page"


def load_json(path: Path, fallback: object) -> object:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8-sig"))


def git_status_lines() -> list[str]:
    try:
        result = subprocess.run(
            ["git", "status", "--short"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    except OSError:
        return []
    if result.returncode != 0:
        return []
    return [line for line in result.stdout.splitlines() if line.strip()]


def build_pages(context: dict[str, object]) -> list[dict[str, object]]:
    route_map_func = context["build_route_map"]
    rewrite_links = context["rewrite_links"]
    inject_seo = context["inject_seo_enhancements"]
    route_map: dict[str, str] = route_map_func()
    pages: list[dict[str, object]] = []

    for source_rel, route in sorted(route_map.items(), key=lambda item: item[1]):
        source = ROOT / source_rel
        raw = source.read_text(encoding="utf-8-sig")
        raw_parser = parse_html(raw)
        errors: list[str] = []
        try:
            rewritten = rewrite_links(raw, source, route, route_map)
            enhanced = inject_seo(rewritten, route, route_map)
        except Exception as exc:  # pragma: no cover - report should capture failures.
            enhanced = raw
            errors.append(f"{type(exc).__name__}: {exc}")
        parser = parse_html(enhanced)
        schema_types = schema_types_from_scripts(parser.schema_scripts)
        description = parser.meta.get("description", raw_parser.meta.get("description", ""))
        pages.append(
            {
                "route": route,
                "source": source_rel,
                "kind": page_kind(route, context),
                "label": route_label(route, context),
                "title": parser.title or raw_parser.title,
                "description": normalize_text(description),
                "h1": parser.heading("h1") or raw_parser.heading("h1"),
                "headings": [text for _tag, text in raw_parser.headings],
                "raw_text": raw_parser.text,
                "built_text": parser.text,
                "raw_word_count": word_count(raw_parser.text),
                "built_word_count": word_count(parser.text),
                "faq_count": len(raw_parser.summaries),
                "faqs": raw_parser.summaries,
                "links": parser.links,
                "images": parser.images,
                "schema_types": schema_types,
                "schema_count": len(parser.schema_scripts),
                "errors": errors,
            }
        )
    return pages


def build_link_maps(pages: list[dict[str, object]]) -> tuple[dict[str, list[str]], dict[str, list[str]]]:
    route_set = {str(page["route"]) for page in pages}
    outgoing: dict[str, list[str]] = {}
    incoming: dict[str, list[str]] = {route: [] for route in route_set}

    for page in pages:
        route = str(page["route"])
        targets: set[str] = set()
        for href in page["links"]:
            target = normalize_internal_link(route, str(href))
            if target and target in route_set and target != route:
                targets.add(target)
        outgoing[route] = sorted(targets)
        for target in targets:
            incoming[target].append(route)

    for route in incoming:
        incoming[route] = sorted(set(incoming[route]))
    return outgoing, incoming


def gallery_items() -> list[dict[str, object]]:
    base = load_json(ROOT / "data" / "job-gallery.json", [])
    social = load_json(ROOT / "data" / "social-gallery.json", {"items": []})
    items = list(base) if isinstance(base, list) else []
    if isinstance(social, dict):
        items.extend(
            item
            for item in social.get("items", [])
            if isinstance(item, dict) and item.get("approved") and item.get("asset")
        )
    return items


def text_mentions(text: str, terms: list[str]) -> bool:
    lower = text.lower()
    return any(term.lower() in lower for term in terms)


def location_terms(location: str) -> list[str]:
    terms = [location]
    if location == "Canyons Village":
        terms.append("Canyons")
    return terms


def service_focus_text(page: dict[str, object]) -> str:
    return " ".join(
        [
            str(page.get("label", "")),
            str(page.get("title", "")),
            str(page.get("description", "")),
            str(page.get("h1", "")),
            " ".join(str(item) for item in page.get("headings", [])),
        ]
    )


def build_coverage_matrix(pages: list[dict[str, object]], images: list[dict[str, object]]) -> dict[str, dict[str, dict[str, object]]]:
    matrix: dict[str, dict[str, dict[str, object]]] = {}
    for location in CORE_LOCATIONS:
        matrix[location] = {}
        location_needles = location_terms(location)
        for service_name, service_needles in SERVICE_TARGETS:
            supporting_pages: list[str] = []
            supporting_images = 0
            for page in pages:
                raw_text = str(page["raw_text"])
                focus = service_focus_text(page)
                route = str(page["route"])
                has_location = text_mentions(focus, location_needles) or slugify(location) in route
                has_service = text_mentions(focus, service_needles) or text_mentions(raw_text, service_needles)
                if has_location and has_service:
                    supporting_pages.append(route)
            for item in images:
                image_text = " ".join(
                    normalize_text(item.get(field, ""))
                    for field in ("location", "city", "county", "service", "keywords", "caption", "alt")
                )
                if text_mentions(image_text, location_needles) and text_mentions(image_text, service_needles):
                    supporting_images += 1
            matrix[location][service_name] = {
                "pages": sorted(set(supporting_pages)),
                "imageCount": supporting_images,
                "status": coverage_status(len(set(supporting_pages)), supporting_images),
            }
    return matrix


def coverage_status(page_count: int, image_count: int) -> str:
    if page_count == 0 and image_count == 0:
        return "gap"
    if page_count < 3 or image_count == 0:
        return "weak"
    return "strong"


def entity_inventory(pages: list[dict[str, object]], images: list[dict[str, object]], context: dict[str, object]) -> list[dict[str, object]]:
    build_areas = [str(item).replace(" UT", "") for item in context.get("CORE_AREAS", [])]
    build_topics = [str(item) for item in context.get("CORE_TOPICS", [])]
    route_entities = [
        route_label(str(page["route"]), context)
        for page in pages
        if str(page["route"]).startswith("/service-location/")
    ]
    entities = sorted(set(CORE_LOCATIONS + build_areas + build_topics + route_entities))
    rows: list[dict[str, object]] = []
    for entity in entities:
        if not entity or entity.lower() in {"home", "blog"}:
            continue
        page_routes = [
            str(page["route"])
            for page in pages
            if entity.lower() in str(page["raw_text"]).lower()
            or entity.lower() in str(page["title"]).lower()
            or entity.lower() in str(page["h1"]).lower()
        ]
        image_count = 0
        faq_count = 0
        for item in images:
            image_text = " ".join(normalize_text(value) for value in item.values())
            if entity.lower() in image_text.lower():
                image_count += 1
        for page in pages:
            faq_text = " ".join(str(item) for item in page.get("faqs", []))
            if entity.lower() in faq_text.lower():
                faq_count += 1
        rows.append(
            {
                "entity": entity,
                "pages": sorted(set(page_routes)),
                "pageCount": len(set(page_routes)),
                "imageCount": image_count,
                "faqPageCount": faq_count,
            }
        )
    return sorted(rows, key=lambda row: (-int(row["pageCount"]), str(row["entity"])))


def report_header(title: str) -> str:
    return f"# {title}\n\nGenerated: {report_date()}\n\n"


def generate_route_inventory(pages: list[dict[str, object]], outgoing: dict[str, list[str]], incoming: dict[str, list[str]]) -> None:
    rows = [
        [
            page["route"],
            page["kind"],
            page["source"],
            page["title"],
            page["h1"],
            page["raw_word_count"],
            len(outgoing[str(page["route"])]),
            len(incoming[str(page["route"])]),
            len(page["images"]),
            page["faq_count"],
            ", ".join(str(item) for item in page["schema_types"][:8]),
        ]
        for page in pages
    ]
    write_report(
        "route_inventory.md",
        report_header("Route Inventory")
        + md_table(
            [
                "Route",
                "Type",
                "Source",
                "Title",
                "H1",
                "Raw Words",
                "Out Links",
                "In Links",
                "Images",
                "FAQs",
                "Schema Types",
            ],
            rows,
        ),
    )


def generate_service_inventory(pages: list[dict[str, object]]) -> None:
    service_pages = [page for page in pages if page["kind"] == "service"]
    rows = [
        [
            page["route"],
            page["title"],
            page["raw_word_count"],
            page["faq_count"],
            len(page["images"]),
            "Service" in page["schema_types"],
        ]
        for page in service_pages
    ]
    write_report(
        "service_inventory.md",
        report_header("Service Inventory")
        + md_table(["Route", "Title", "Raw Words", "FAQs", "Images", "Service Schema"], rows),
    )


def generate_neighborhood_inventory(pages: list[dict[str, object]], context: dict[str, object]) -> None:
    location_pages = [page for page in pages if page["kind"] == "location"]
    parent_routes = context.get("LOCATION_PARENT_ROUTES", {})
    rows = [
        [
            page["route"],
            page["label"],
            parent_routes.get(str(page["route"]), ""),
            page["raw_word_count"],
            page["faq_count"],
            len(page["images"]),
        ]
        for page in location_pages
    ]
    write_report(
        "neighborhood_inventory.md",
        report_header("Neighborhood And Location Inventory")
        + md_table(["Route", "Entity", "Parent Route", "Raw Words", "FAQs", "Images"], rows),
    )


def generate_schema_inventory(pages: list[dict[str, object]]) -> None:
    counter: Counter[str] = Counter()
    for page in pages:
        counter.update(str(item) for item in page["schema_types"])
    summary = md_table(["Schema Type", "Page Count"], [[key, value] for key, value in counter.most_common()])
    rows = [
        [page["route"], page["schema_count"], ", ".join(str(item) for item in page["schema_types"])]
        for page in pages
    ]
    write_report(
        "schema_inventory.md",
        report_header("Schema Inventory")
        + "## Type Summary\n\n"
        + summary
        + "\n## Route Detail\n\n"
        + md_table(["Route", "JSON-LD Blocks", "Schema Types"], rows),
    )
    write_report(
        "structured_data_report.md",
        report_header("Structured Data Report")
        + "Every generated public route should include JSON-LD from the build pipeline.\n\n"
        + md_table(
            ["Route", "Has Schema", "FAQPage", "Service", "BlogPosting", "ImageObject", "Review"],
            [
                [
                    page["route"],
                    bool(page["schema_types"]),
                    "FAQPage" in page["schema_types"],
                    "Service" in page["schema_types"],
                    "BlogPosting" in page["schema_types"],
                    "ImageObject" in page["schema_types"],
                    "Review" in page["schema_types"],
                ]
                for page in pages
            ],
        ),
    )


def generate_image_inventory(pages: list[dict[str, object]], images: list[dict[str, object]]) -> None:
    missing_alt = [
        [page["route"], image.get("src", "")]
        for page in pages
        for image in page["images"]
        if not normalize_text(image.get("alt", ""))
    ]
    missing_assets = [
        [item.get("asset", ""), item.get("routes", [])]
        for item in images
        if item.get("asset") and not (ROOT / str(item.get("asset"))).exists()
    ]
    route_counts: Counter[str] = Counter()
    for item in images:
        for route in item.get("routes", []):
            route_counts[str(route)] += 1
    write_report(
        "image_inventory.md",
        report_header("Image Inventory")
        + f"- Structured gallery records: {len(images)}\n"
        + f"- Image tags in generated pages: {sum(len(page['images']) for page in pages)}\n"
        + f"- Missing alt attributes in generated pages: {len(missing_alt)}\n"
        + f"- Missing gallery source assets: {len(missing_assets)}\n\n"
        + "## Gallery Route Coverage\n\n"
        + md_table(["Route", "Structured Image Records"], [[route, count] for route, count in route_counts.most_common()])
        + "\n## Missing Alt Attributes\n\n"
        + md_table(["Route", "Image"], missing_alt[:50])
        + "\n## Missing Gallery Assets\n\n"
        + md_table(["Asset", "Routes"], missing_assets[:50]),
    )


def generate_review_inventory() -> None:
    reviews = load_json(ROOT / "data" / "reviews.json", {})
    featured = reviews.get("featuredReviews", []) if isinstance(reviews, dict) else []
    rows = [
        [
            review.get("author", ""),
            review.get("rating", ""),
            review.get("createTime", ""),
            bool(review.get("sourceUrl")),
            bool(review.get("profilePhotoUrl")),
        ]
        for review in featured
        if isinstance(review, dict)
    ]
    write_report(
        "review_inventory.md",
        report_header("Review Inventory")
        + f"- Source: {reviews.get('sourceName', '') if isinstance(reviews, dict) else ''}\n"
        + f"- Rating value: {reviews.get('ratingValue', '') if isinstance(reviews, dict) else ''}\n"
        + f"- Review count: {reviews.get('reviewCount', '') if isinstance(reviews, dict) else ''}\n"
        + f"- Last verified: {reviews.get('lastVerified', '') if isinstance(reviews, dict) else ''}\n"
        + f"- Featured reviews: {len(featured)}\n\n"
        + md_table(["Author", "Rating", "Date", "Has Source URL", "Has Photo"], rows),
    )


def generate_faq_inventory(pages: list[dict[str, object]]) -> None:
    rows = [
        [page["route"], page["faq_count"], " / ".join(str(item) for item in page.get("faqs", [])[:3])]
        for page in pages
    ]
    write_report(
        "faq_inventory.md",
        report_header("FAQ Inventory")
        + md_table(["Route", "FAQ Count", "Sample Questions"], rows),
    )


def generate_internal_link_reports(pages: list[dict[str, object]], outgoing: dict[str, list[str]], incoming: dict[str, list[str]]) -> None:
    rows = [
        [
            page["route"],
            len(outgoing[str(page["route"])]),
            len(incoming[str(page["route"])]),
            ", ".join(outgoing[str(page["route"])][:12]),
        ]
        for page in pages
    ]
    orphan_rows = [
        [route, len(outgoing.get(route, []))]
        for route, sources in sorted(incoming.items())
        if not sources and route != "/"
    ]
    write_report(
        "internal_links.md",
        report_header("Internal Link Inventory")
        + md_table(["Route", "Unique Out Links", "Unique In Links", "Sample Out Links"], rows),
    )
    write_report(
        "orphan_pages.md",
        report_header("Orphan Pages")
        + "Routes with no detected incoming internal links, excluding the homepage.\n\n"
        + md_table(["Route", "Out Links"], orphan_rows),
    )


def generate_thin_content_report(pages: list[dict[str, object]]) -> None:
    thin = [
        [page["route"], page["kind"], page["raw_word_count"], page["title"]]
        for page in pages
        if int(page["raw_word_count"]) < 450
    ]
    write_report(
        "thin_content.md",
        report_header("Thin Content")
        + "Threshold: fewer than 450 raw source words. This is a signal, not a final quality judgment.\n\n"
        + md_table(["Route", "Type", "Raw Words", "Title"], thin),
    )


def generate_entity_report(entity_rows: list[dict[str, object]]) -> None:
    rows = [
        [
            item["entity"],
            item["pageCount"],
            item["imageCount"],
            item["faqPageCount"],
            ", ".join(item["pages"][:8]),
        ]
        for item in entity_rows[:120]
    ]
    write_report(
        "entity_inventory.md",
        report_header("Entity Inventory")
        + md_table(["Entity", "Pages", "Images", "FAQ Pages", "Sample Routes"], rows),
    )


def generate_coverage_reports(matrix: dict[str, dict[str, dict[str, object]]]) -> None:
    rows: list[list[object]] = []
    gaps: list[list[object]] = []
    weak: list[list[object]] = []
    headers = ["Location"] + [service for service, _terms in SERVICE_TARGETS]
    for location, services in matrix.items():
        row: list[object] = [location]
        for service, data in services.items():
            page_count = len(data["pages"])
            image_count = data["imageCount"]
            if data["status"] == "gap":
                row.append("GAP")
                gaps.append([location, service])
            elif data["status"] == "weak":
                row.append(f"{page_count}p/{image_count}i WEAK")
                weak.append([location, service, page_count, image_count])
            else:
                row.append(f"{page_count}p/{image_count}i")
        rows.append(row)
    write_report(
        "coverage_matrix.md",
        report_header("Coverage Matrix")
        + "Cells show supporting page count and structured image count. `GAP` means no support detected by the current heuristic.\n\n"
        + md_table(headers, rows)
        + "\n## Detected Gaps\n\n"
        + md_table(["Location", "Service"], gaps)
        + "\n## Weak Coverage\n\n"
        + md_table(["Location", "Service", "Pages", "Images"], weak),
    )
    write_json("coverage_matrix.json", matrix)


def generate_content_gap_report(
    pages: list[dict[str, object]],
    matrix: dict[str, dict[str, dict[str, object]]],
    incoming: dict[str, list[str]],
) -> None:
    coverage_gaps = [
        [location, service, data["status"], len(data["pages"]), data["imageCount"]]
        for location, services in matrix.items()
        for service, data in services.items()
        if data["status"] in {"gap", "weak"}
    ]
    no_faq = [[page["route"], page["kind"], page["title"]] for page in pages if not page["faq_count"]]
    low_inlinks = [
        [page["route"], page["kind"], len(incoming[str(page["route"])]), page["title"]]
        for page in pages
        if str(page["route"]) != "/" and len(incoming[str(page["route"])]) <= 1
    ]
    write_report(
        "content_gap_report.md",
        report_header("Content Gap Report")
        + "## Coverage Gaps And Weak Cells\n\n"
        + md_table(["Location", "Service", "Status", "Pages", "Images"], coverage_gaps)
        + "\n## Pages Without Source FAQs\n\n"
        + md_table(["Route", "Type", "Title"], no_faq[:80])
        + "\n## Low Incoming Link Routes\n\n"
        + md_table(["Route", "Type", "In Links", "Title"], low_inlinks[:80]),
    )


def generate_authority_report(
    pages: list[dict[str, object]],
    matrix: dict[str, dict[str, dict[str, object]]],
    incoming: dict[str, list[str]],
) -> None:
    total = max(len(pages), 1)
    metadata_rate = sum(1 for page in pages if page["title"] and page["description"] and page["h1"]) / total
    schema_rate = sum(1 for page in pages if page["schema_types"]) / total
    link_rate = sum(1 for page in pages if str(page["route"]) == "/" or incoming[str(page["route"])]) / total
    faq_rate = sum(1 for page in pages if page["faq_count"]) / total
    image_rate = sum(1 for page in pages if page["images"]) / total
    cells = [data for services in matrix.values() for data in services.values()]
    coverage_rate = sum(1 for data in cells if data["status"] == "strong") / max(len(cells), 1)
    score = round(
        metadata_rate * 20
        + schema_rate * 20
        + link_rate * 15
        + faq_rate * 15
        + image_rate * 15
        + coverage_rate * 15,
        1,
    )
    rows = [
        ["Metadata completeness", f"{metadata_rate:.0%}", "20"],
        ["Structured data coverage", f"{schema_rate:.0%}", "20"],
        ["Internal link coverage", f"{link_rate:.0%}", "15"],
        ["Source FAQ coverage", f"{faq_rate:.0%}", "15"],
        ["Generated image coverage", f"{image_rate:.0%}", "15"],
        ["Strong service-location matrix coverage", f"{coverage_rate:.0%}", "15"],
    ]
    write_report(
        "authority_report.md",
        report_header("AI Authority Opportunity Report")
        + f"Internal heuristic score: {score} / 100\n\n"
        + "This score is not a ranking claim. It is a local engineering heuristic for prioritizing work.\n\n"
        + md_table(["Signal", "Coverage", "Weight"], rows),
    )


def generate_build_report(pages: list[dict[str, object]]) -> None:
    package = load_json(ROOT / "package.json", {})
    scripts = package.get("scripts", {}) if isinstance(package, dict) else {}
    output = ROOT / "cloudflare-preview"
    generated_routes = list(output.glob("**/index.html")) if output.exists() else []
    status = git_status_lines()
    write_report(
        "build_report.md",
        report_header("Build Report")
        + f"- Source route count: {len(pages)}\n"
        + f"- Existing build output route files: {len(generated_routes)}\n"
        + f"- Cloudflare output directory exists: {output.exists()}\n"
        + f"- Git status entries at report time: {len(status)}\n\n"
        + "## Package Scripts\n\n"
        + md_table(["Script", "Command"], [[key, value] for key, value in scripts.items()])
        + "\n## Page Build Simulation Errors\n\n"
        + md_table(
            ["Route", "Errors"],
            [[page["route"], " / ".join(page["errors"])] for page in pages if page["errors"]],
        ),
    )


def generate_automation_report() -> None:
    package = load_json(ROOT / "package.json", {})
    scripts = package.get("scripts", {}) if isinstance(package, dict) else {}
    workflows = sorted(path.name for path in (ROOT / ".github" / "workflows").glob("*") if path.is_file())
    tools = sorted(path.name for path in (ROOT / "tools").glob("*.py"))
    write_report(
        "automation_report.md",
        report_header("Automation Report")
        + "## NPM Scripts\n\n"
        + md_table(["Script", "Command"], [[key, value] for key, value in scripts.items()])
        + "\n## GitHub Workflows\n\n"
        + md_table(["Workflow"], [[name] for name in workflows])
        + "\n## Tool Scripts\n\n"
        + md_table(["Tool"], [[name] for name in tools]),
    )


def generate_technical_debt_report(pages: list[dict[str, object]], incoming: dict[str, list[str]]) -> None:
    detected = []
    for page in pages:
        issues = []
        if not page["title"]:
            issues.append("missing title")
        if not page["description"]:
            issues.append("missing description")
        if not page["h1"]:
            issues.append("missing h1")
        if int(page["raw_word_count"]) < 450:
            issues.append("thin raw content")
        if str(page["route"]) != "/" and not incoming[str(page["route"])]:
            issues.append("orphan")
        if issues:
            detected.append([page["route"], ", ".join(issues)])
    write_report(
        "technical_debt.md",
        report_header("Technical Debt Report")
        + "## Detected Signals\n\n"
        + md_table(["Route", "Signals"], detected)
        + "\n## Standing Debt\n\n"
        + "- Large build script has multiple responsibilities.\n"
        + "- Source pages still use GPT-suffixed filenames.\n"
        + "- Repository Intelligence reports are new and should be refined after use.\n"
        + "- External analytics and AI monitoring state is not fully documented.\n",
    )


def generate_knowledge_graph(pages: list[dict[str, object]], images: list[dict[str, object]]) -> None:
    nodes: dict[str, dict[str, str]] = {
        "sun_ray": {"label": "Sun Ray Cleaning Services", "type": "Organization"},
        "services": {"label": "Cleaning Services", "type": "Category"},
        "locations": {"label": "Wasatch Back Locations", "type": "Category"},
        "content": {"label": "Local Cleaning Content", "type": "Category"},
        "proof": {"label": "Reviews And Images", "type": "Category"},
    }
    edges: set[tuple[str, str, str]] = {
        ("sun_ray", "services", "offers"),
        ("sun_ray", "locations", "serves"),
        ("sun_ray", "content", "publishes"),
        ("sun_ray", "proof", "supported_by"),
    }
    for service, _terms in SERVICE_TARGETS:
        key = "service_" + slugify(service)
        nodes[key] = {"label": service, "type": "Service"}
        edges.add(("services", key, "includes"))
    for location in CORE_LOCATIONS:
        key = "location_" + slugify(location)
        nodes[key] = {"label": location, "type": "Place"}
        edges.add(("locations", key, "includes"))
    for page in pages:
        route = str(page["route"])
        if page["kind"] not in {"service", "location", "blog", "gallery"}:
            continue
        key = "route_" + slugify(route)
        nodes[key] = {"label": route, "type": "Route"}
        edges.add(("content", key, "contains"))
        for location in CORE_LOCATIONS:
            if location.lower() in str(page["raw_text"]).lower() or slugify(location) in route:
                edges.add((key, "location_" + slugify(location), "mentions"))
        for service, terms in SERVICE_TARGETS:
            if text_mentions(str(page["raw_text"]), terms) or text_mentions(service_focus_text(page), terms):
                edges.add((key, "service_" + slugify(service), "mentions"))
    for item in images:
        asset = str(item.get("asset", ""))
        if not asset:
            continue
        image_key = "image_" + slugify(Path(asset).stem)
        nodes[image_key] = {"label": Path(asset).name, "type": "Image"}
        edges.add(("proof", image_key, "contains"))
        for location in CORE_LOCATIONS:
            image_text = " ".join(normalize_text(value) for value in item.values())
            if location.lower() in image_text.lower():
                edges.add((image_key, "location_" + slugify(location), "depicts"))
        for service, terms in SERVICE_TARGETS:
            image_text = " ".join(normalize_text(value) for value in item.values())
            if text_mentions(image_text, terms):
                edges.add((image_key, "service_" + slugify(service), "depicts"))

    mermaid_lines = ["flowchart TD"]
    for key, node in sorted(nodes.items()):
        mermaid_lines.append(f'  {key}["{markdown_cell(node["label"])}"]')
    for source, target, label in sorted(edges):
        mermaid_lines.append(f"  {source} -- {label} --> {target}")

    write_report(
        "knowledge_graph.md",
        report_header("Knowledge Graph")
        + "```mermaid\n"
        + "\n".join(mermaid_lines)
        + "\n```\n",
    )
    write_json("knowledge_graph.json", {"nodes": nodes, "edges": sorted(list(edges))})


def main() -> None:
    context = load_build_context()
    pages = build_pages(context)
    images = gallery_items()
    outgoing, incoming = build_link_maps(pages)
    matrix = build_coverage_matrix(pages, images)
    entities = entity_inventory(pages, images, context)

    generate_route_inventory(pages, outgoing, incoming)
    generate_service_inventory(pages)
    generate_neighborhood_inventory(pages, context)
    generate_schema_inventory(pages)
    generate_image_inventory(pages, images)
    generate_review_inventory()
    generate_faq_inventory(pages)
    generate_internal_link_reports(pages, outgoing, incoming)
    generate_thin_content_report(pages)
    generate_entity_report(entities)
    generate_coverage_reports(matrix)
    generate_content_gap_report(pages, matrix, incoming)
    generate_authority_report(pages, matrix, incoming)
    generate_build_report(pages)
    generate_automation_report()
    generate_technical_debt_report(pages, incoming)
    generate_knowledge_graph(pages, images)

    write_json(
        "repository_inventory.json",
        {
            "generatedAt": report_date(),
            "routes": [
                {
                    "route": page["route"],
                    "source": page["source"],
                    "kind": page["kind"],
                    "title": page["title"],
                    "h1": page["h1"],
                    "rawWordCount": page["raw_word_count"],
                    "builtWordCount": page["built_word_count"],
                    "faqCount": page["faq_count"],
                    "imageCount": len(page["images"]),
                    "schemaTypes": page["schema_types"],
                    "outgoingInternalLinks": outgoing[str(page["route"])],
                    "incomingInternalLinks": incoming[str(page["route"])],
                }
                for page in pages
            ],
            "entities": entities,
        },
    )

    print(f"Generated {len(list(REPORTS.glob('*.md')))} reports for {len(pages)} routes.")


if __name__ == "__main__":
    main()
