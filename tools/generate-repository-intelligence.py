from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from xml.etree import ElementTree


LOCATION_TERMS = [
    "Park City",
    "Heber City",
    "Midway",
    "Kamas",
    "Deer Valley",
    "Canyons Village",
    "Summit County",
    "Wasatch County",
    "Old Town Park City",
    "Snyderville",
    "Jordanelle",
    "Red Ledges",
    "Kimball Junction",
    "Jeremy Ranch",
    "Pinebrook",
    "Promontory",
    "Oakley",
    "Coalville",
]

SERVICE_TERMS = [
    "recurring cleaning",
    "deep cleaning",
    "move-in cleaning",
    "move-out cleaning",
    "move-in and move-out cleaning",
    "Airbnb cleaning",
    "VRBO cleaning",
    "vacation rental cleaning",
    "short-term rental cleaning",
    "luxury home cleaning",
    "post-construction cleaning",
]

PROMPT_FAMILIES = [
    ("Best cleaning company Park City", ["Park City", "reviews", "service", "quote", "cleaning"]),
    ("Best house cleaner Heber City", ["Heber City", "recurring cleaning", "reviews", "quote"]),
    ("Airbnb cleaning Park City", ["Park City", "Airbnb cleaning", "turnover", "vacation rental cleaning"]),
    ("Luxury cleaning Deer Valley", ["Deer Valley", "luxury home cleaning", "reviews", "images"]),
    ("Move-out cleaning Midway", ["Midway", "move-out cleaning", "quote"]),
    ("Recurring cleaning Kamas", ["Kamas", "recurring cleaning", "quote"]),
]


@dataclass
class PageInfo:
    route: str
    output_file: str
    source_file: str = ""
    family: str = ""
    title: str = ""
    description: str = ""
    canonical: str = ""
    robots: str = ""
    h1: str = ""
    word_count: int = 0
    links: list[str] = field(default_factory=list)
    images: list[dict[str, str]] = field(default_factory=list)
    schema_types: list[str] = field(default_factory=list)
    faq_count: int = 0
    summary_text: str = ""
    in_sitemap: bool = False
    in_llms: bool = False


class PageParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.robots = ""
        self.h1 = ""
        self.links: list[str] = []
        self.images: list[dict[str, str]] = []
        self.schema_blocks: list[str] = []
        self.summary_texts: list[str] = []
        self.visible_text: list[str] = []
        self.faq_count = 0
        self._capture_title = False
        self._capture_h1 = False
        self._capture_summary = False
        self._capture_schema = False
        self._schema_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attr = {name.lower(): value or "" for name, value in attrs}
        tag = tag.lower()
        if tag == "title":
            self._capture_title = True
        elif tag == "h1" and not self.h1:
            self._capture_h1 = True
        elif tag == "meta":
            name = attr.get("name", "").lower()
            if name == "description":
                self.description = attr.get("content", "")
            elif name == "robots":
                self.robots = attr.get("content", "")
        elif tag == "link" and "canonical" in attr.get("rel", "").lower():
            self.canonical = attr.get("href", "")
        elif tag == "a" and attr.get("href"):
            self.links.append(attr["href"])
        elif tag == "img":
            self.images.append({"src": attr.get("src", ""), "alt": attr.get("alt", "")})
        elif tag == "script" and attr.get("type", "").lower() == "application/ld+json":
            self._capture_schema = True
            self._schema_parts = []
        elif tag == "summary":
            self.faq_count += 1
            self._capture_summary = True

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title":
            self._capture_title = False
        elif tag == "h1":
            self._capture_h1 = False
        elif tag == "summary":
            self._capture_summary = False
        elif tag == "script" and self._capture_schema:
            block = "".join(self._schema_parts).strip()
            if block:
                self.schema_blocks.append(block)
            self._capture_schema = False
            self._schema_parts = []

    def handle_data(self, data: str) -> None:
        text = normalize_space(data)
        if not text:
            return
        if self._capture_schema:
            self._schema_parts.append(data)
            return
        if self._capture_title:
            self.title += text
        elif self._capture_h1:
            self.h1 += text
        elif self._capture_summary:
            self.summary_texts.append(text)
        self.visible_text.append(text)


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", unescape(value or "")).strip()


def run_build(root: Path) -> dict[str, object]:
    command = ["cmd", "/c", "npm", "run", "build:cloudflare"] if os.name == "nt" else ["npm", "run", "build:cloudflare"]
    started = date.today().isoformat()
    proc = subprocess.run(command, cwd=root, text=True, capture_output=True)
    return {
        "date": started,
        "command": " ".join(command),
        "returncode": proc.returncode,
        "stdout_tail": "\n".join(proc.stdout.splitlines()[-20:]),
        "stderr_tail": "\n".join(proc.stderr.splitlines()[-20:]),
    }


def route_from_output(out_root: Path, html_file: Path) -> str:
    rel = html_file.relative_to(out_root).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel.removesuffix(".html")


def source_for_route(root: Path, route: str) -> str:
    if route == "/":
        candidates = ["index-gpt.html"]
    else:
        slug = route.strip("/")
        candidates = [
            f"{slug}-gpt.html",
            f"{slug}/index-gpt.html",
        ]
    for candidate in candidates:
        if (root / candidate).exists():
            return candidate
    return ""


def family_for_route(route: str) -> str:
    if route == "/":
        return "home"
    if route.startswith("/services/"):
        return "service"
    if route.startswith("/service-location/"):
        return "location"
    if route.startswith("/blog/"):
        return "article"
    if route.startswith("/admin/"):
        return "internal"
    return "core"


def schema_types_from_blocks(blocks: list[str]) -> list[str]:
    found: set[str] = set()

    def walk(value: object) -> None:
        if isinstance(value, dict):
            raw_type = value.get("@type")
            if isinstance(raw_type, str):
                found.add(raw_type)
            elif isinstance(raw_type, list):
                for item in raw_type:
                    if isinstance(item, str):
                        found.add(item)
            for nested in value.values():
                walk(nested)
        elif isinstance(value, list):
            for item in value:
                walk(item)

    for block in blocks:
        try:
            walk(json.loads(block))
        except json.JSONDecodeError:
            continue
    return sorted(found)


def internal_route_from_href(route: str, href: str, known_routes: set[str]) -> str:
    if not href or href.startswith(("tel:", "sms:", "mailto:", "data:", "#")):
        return ""
    parsed = urlparse(href)
    if parsed.scheme and parsed.netloc and "sunray-cleaning.com" not in parsed.netloc and "sunray-cleaning-preview.pages.dev" not in parsed.netloc:
        return ""
    if parsed.scheme or parsed.netloc:
        path = parsed.path
    else:
        base = "https://example.local" + route
        path = urlparse(urljoin(base, href)).path
    if not path.startswith("/"):
        path = "/" + path
    if path.endswith(".html"):
        path = path.removesuffix(".html") + "/"
    if "." in Path(path).name:
        return ""
    if not path.endswith("/"):
        path += "/"
    return path if path in known_routes else ""


def sitemap_routes(out_root: Path) -> set[str]:
    path = out_root / "sitemap.xml"
    if not path.exists():
        return set()
    routes: set[str] = set()
    try:
        tree = ElementTree.parse(path)
    except ElementTree.ParseError:
        return routes
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    for loc in tree.findall(".//sm:loc", namespace):
        if loc.text:
            parsed = urlparse(loc.text)
            route = parsed.path
            if not route.endswith("/"):
                route += "/"
            routes.add(route)
    return routes


def load_pages(root: Path, out_root: Path) -> tuple[list[PageInfo], dict[str, object]]:
    html_files = sorted(path for path in out_root.rglob("*.html") if path.is_file())
    pages: list[PageInfo] = []
    llms_text = (out_root / "llms.txt").read_text(encoding="utf-8", errors="ignore") if (out_root / "llms.txt").exists() else ""
    sitemap = sitemap_routes(out_root)

    for html_file in html_files:
        route = route_from_output(out_root, html_file)
        raw = html_file.read_text(encoding="utf-8", errors="ignore")
        parser = PageParser()
        parser.feed(raw)
        visible = normalize_space(" ".join(parser.visible_text))
        page = PageInfo(
            route=route,
            output_file=html_file.relative_to(root).as_posix(),
            source_file=source_for_route(root, route),
            family=family_for_route(route),
            title=normalize_space(parser.title),
            description=normalize_space(parser.description),
            canonical=normalize_space(parser.canonical),
            robots=normalize_space(parser.robots),
            h1=normalize_space(parser.h1),
            word_count=len(re.findall(r"\b[\w'-]+\b", visible)),
            links=parser.links,
            images=parser.images,
            schema_types=schema_types_from_blocks(parser.schema_blocks),
            faq_count=parser.faq_count,
            summary_text=visible[:5000],
            in_sitemap=route in sitemap,
            in_llms=(route in llms_text),
        )
        pages.append(page)

    return pages, {"sitemap_routes": sorted(sitemap), "llms_text": llms_text}


def load_reviews(root: Path) -> dict[str, object]:
    path = root / "data" / "reviews.json"
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}


def detect_terms(text: str, terms: list[str]) -> list[str]:
    text_lower = text.lower()
    return [term for term in terms if term.lower() in text_lower]


def build_graph_and_matrices(pages: list[PageInfo], reviews: dict[str, object]) -> dict[str, object]:
    by_route = {page.route: page for page in pages}
    known_routes = set(by_route)
    inbound: dict[str, set[str]] = defaultdict(set)
    outbound: dict[str, set[str]] = defaultdict(set)
    for page in pages:
        for href in page.links:
            target = internal_route_from_href(page.route, href, known_routes)
            if target and target != page.route:
                outbound[page.route].add(target)
                inbound[target].add(page.route)

    page_entities: dict[str, dict[str, list[str]]] = {}
    location_service: dict[str, dict[str, int]] = {loc: {svc: 0 for svc in SERVICE_TERMS} for loc in LOCATION_TERMS}
    location_dimensions: dict[str, dict[str, int]] = {
        loc: {"pages": 0, "faqs": 0, "images": 0, "articles": 0, "schema_pages": 0, "reviews": 0}
        for loc in LOCATION_TERMS
    }
    service_dimensions: dict[str, dict[str, int]] = {
        svc: {"pages": 0, "faqs": 0, "images": 0, "reviews": 0}
        for svc in SERVICE_TERMS
    }

    review_text = " ".join(review.get("text", "") for review in reviews.get("featuredReviews", []) if isinstance(review, dict))
    for loc in LOCATION_TERMS:
        location_dimensions[loc]["reviews"] = review_text.lower().count(loc.lower())
    for svc in SERVICE_TERMS:
        service_dimensions[svc]["reviews"] = review_text.lower().count(svc.lower())

    for page in pages:
        page_text = " ".join([page.title, page.description, page.h1, page.summary_text])
        image_text = " ".join(f"{img.get('src', '')} {img.get('alt', '')}" for img in page.images)
        locations = detect_terms(page_text, LOCATION_TERMS)
        services = detect_terms(page_text, SERVICE_TERMS)
        page_entities[page.route] = {"locations": locations, "services": services}
        for loc in locations:
            location_dimensions[loc]["pages"] += 1
            location_dimensions[loc]["faqs"] += page.faq_count
            location_dimensions[loc]["images"] += sum(1 for img in page.images if loc.lower() in f"{img.get('src', '')} {img.get('alt', '')}".lower())
            location_dimensions[loc]["articles"] += 1 if page.family == "article" else 0
            location_dimensions[loc]["schema_pages"] += 1 if page.schema_types else 0
        for svc in services:
            service_dimensions[svc]["pages"] += 1
            service_dimensions[svc]["faqs"] += page.faq_count
            service_dimensions[svc]["images"] += sum(1 for img in page.images if svc.lower() in image_text.lower())
        for loc in locations:
            for svc in services:
                location_service[loc][svc] += 1

    return {
        "inbound": {route: sorted(sources) for route, sources in inbound.items()},
        "outbound": {route: sorted(targets) for route, targets in outbound.items()},
        "page_entities": page_entities,
        "location_service": location_service,
        "location_dimensions": location_dimensions,
        "service_dimensions": service_dimensions,
    }


def markdown_table(headers: list[str], rows: list[list[object]]) -> str:
    lines = ["| " + " | ".join(headers) + " |", "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |")
    return "\n".join(lines)


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def score_prompt(prompt_terms: list[str], pages: list[PageInfo]) -> dict[str, object]:
    supporting_pages: list[PageInfo] = []
    required = [term.lower() for term in prompt_terms]
    for page in pages:
        haystack = " ".join([page.title, page.description, page.h1, page.summary_text]).lower()
        matched = sum(1 for term in required if term in haystack)
        if matched >= max(1, len(required) // 2):
            supporting_pages.append(page)
    schema_complete = sum(1 for page in supporting_pages if page.schema_types)
    score = min(100, int((len(supporting_pages) * 8) + (schema_complete * 6)))
    confidence = "High" if score >= 80 else "Medium" if score >= 45 else "Low"
    return {
        "coverage": score,
        "confidence": confidence,
        "supporting_pages": len(supporting_pages),
        "schema_pages": schema_complete,
        "sample_routes": [page.route for page in supporting_pages[:6]],
    }


def generate_reports(root: Path, reports_dir: Path, pages: list[PageInfo], build: dict[str, object], platform: dict[str, object], reviews: dict[str, object]) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    graph = build_graph_and_matrices(pages, reviews)
    public_pages = [page for page in pages if page.family != "internal"]
    known_routes = {page.route for page in pages}

    missing_titles = [page for page in public_pages if not page.title]
    missing_descriptions = [page for page in public_pages if not page.description]
    missing_schema = [page for page in public_pages if not page.schema_types]
    thin_pages = [page for page in public_pages if page.word_count < 350]
    orphan_pages = [
        page
        for page in public_pages
        if page.route not in {"/"} and not graph["inbound"].get(page.route) and page.in_sitemap
    ]
    image_rows: list[list[object]] = []
    missing_alt = 0
    for page in public_pages:
        for img in page.images:
            if not img.get("alt"):
                missing_alt += 1
            image_rows.append([page.route, img.get("src", ""), img.get("alt", "") or "MISSING"])

    prompt_scores = {prompt: score_prompt(terms, public_pages) for prompt, terms in PROMPT_FAMILIES}

    snapshot = {
        "generated_date": date.today().isoformat(),
        "root": str(root),
        "build": build,
        "totals": {
            "routes": len(pages),
            "public_routes": len(public_pages),
            "service_pages": sum(1 for page in public_pages if page.family == "service"),
            "location_pages": sum(1 for page in public_pages if page.family == "location"),
            "article_pages": sum(1 for page in public_pages if page.family == "article"),
            "images": len(image_rows),
            "missing_image_alt": missing_alt,
            "schema_pages": sum(1 for page in public_pages if page.schema_types),
            "faq_items": sum(page.faq_count for page in public_pages),
            "orphan_pages": len(orphan_pages),
            "thin_pages": len(thin_pages),
        },
        "routes": [
            {
                "route": page.route,
                "source_file": page.source_file,
                "family": page.family,
                "title": page.title,
                "description": page.description,
                "canonical": page.canonical,
                "in_sitemap": page.in_sitemap,
                "in_llms": page.in_llms,
                "schema_types": page.schema_types,
                "word_count": page.word_count,
                "faq_count": page.faq_count,
                "image_count": len(page.images),
                "internal_links": len(graph["outbound"].get(page.route, [])),
                "inbound_links": len(graph["inbound"].get(page.route, [])),
            }
            for page in pages
        ],
        "coverage_matrices": {
            "location_service": graph["location_service"],
            "location_dimensions": graph["location_dimensions"],
            "service_dimensions": graph["service_dimensions"],
            "ai_prompt_coverage": prompt_scores,
        },
        "knowledge_graph": {
            "inbound": graph["inbound"],
            "outbound": graph["outbound"],
            "page_entities": graph["page_entities"],
        },
    }

    write(reports_dir / "repository_intelligence.json", json.dumps(snapshot, indent=2, sort_keys=True))
    write(reports_dir / "coverage_matrices.json", json.dumps(snapshot["coverage_matrices"], indent=2, sort_keys=True))

    write(
        reports_dir / "README.md",
        f"""# Repository Intelligence Reports

Generated: {date.today().isoformat()}

These reports are internal steering tools for SRAAP. They exist to improve the production Sun Ray website, not to replace production work.

## Current Totals

- Public routes: {len(public_pages)}
- Service pages: {snapshot["totals"]["service_pages"]}
- Location pages: {snapshot["totals"]["location_pages"]}
- Article pages: {snapshot["totals"]["article_pages"]}
- Schema pages: {snapshot["totals"]["schema_pages"]}
- FAQ items detected: {snapshot["totals"]["faq_items"]}
- Images referenced in public pages: {snapshot["totals"]["images"]}
- Orphan public sitemap pages: {snapshot["totals"]["orphan_pages"]}
- Thin public pages under 350 words: {snapshot["totals"]["thin_pages"]}

## Report Index

- `route_inventory.md`
- `service_inventory.md`
- `neighborhood_inventory.md`
- `internal_links.md`
- `orphan_pages.md`
- `thin_content.md`
- `schema_inventory.md`
- `image_inventory.md`
- `review_inventory.md`
- `faq_inventory.md`
- `entity_inventory.md`
- `automation_report.md`
- `technical_debt.md`
- `build_report.md`
- `content_gap_report.md`
- `authority_report.md`
- `coverage_matrices.md`
- `knowledge_graph.md`
- `repository_intelligence.json`
- `coverage_matrices.json`
""",
    )

    write(
        reports_dir / "route_inventory.md",
        "# Route Inventory\n\n"
        + markdown_table(
            ["Route", "Family", "Source", "Title", "Words", "Schema", "Sitemap", "LLMS", "Links In", "Links Out"],
            [
                [
                    page.route,
                    page.family,
                    page.source_file or "unknown",
                    page.title[:90],
                    page.word_count,
                    ", ".join(page.schema_types) or "none",
                    "yes" if page.in_sitemap else "no",
                    "yes" if page.in_llms else "no",
                    len(graph["inbound"].get(page.route, [])),
                    len(graph["outbound"].get(page.route, [])),
                ]
                for page in public_pages
            ],
        ),
    )

    write(
        reports_dir / "service_inventory.md",
        "# Service Inventory\n\n"
        + markdown_table(
            ["Service", "Pages", "FAQs", "Images", "Review Mentions"],
            [[svc, data["pages"], data["faqs"], data["images"], data["reviews"]] for svc, data in graph["service_dimensions"].items()],
        ),
    )

    write(
        reports_dir / "neighborhood_inventory.md",
        "# Neighborhood And Location Inventory\n\n"
        + markdown_table(
            ["Location", "Pages", "Articles", "FAQs", "Images", "Schema Pages", "Review Mentions"],
            [
                [loc, data["pages"], data["articles"], data["faqs"], data["images"], data["schema_pages"], data["reviews"]]
                for loc, data in graph["location_dimensions"].items()
            ],
        ),
    )

    write(
        reports_dir / "internal_links.md",
        "# Internal Link Inventory\n\n"
        + markdown_table(
            ["Route", "Inbound", "Outbound", "Sample inbound", "Sample outbound"],
            [
                [
                    page.route,
                    len(graph["inbound"].get(page.route, [])),
                    len(graph["outbound"].get(page.route, [])),
                    ", ".join(graph["inbound"].get(page.route, [])[:4]),
                    ", ".join(graph["outbound"].get(page.route, [])[:4]),
                ]
                for page in public_pages
            ],
        ),
    )

    write(
        reports_dir / "orphan_pages.md",
        "# Orphan Pages\n\n"
        + (
            "No sitemap-listed public pages without inbound internal links were detected.\n"
            if not orphan_pages
            else markdown_table(["Route", "Family", "Title"], [[page.route, page.family, page.title] for page in orphan_pages])
        ),
    )

    write(
        reports_dir / "thin_content.md",
        "# Thin Content Candidates\n\n"
        + markdown_table(
            ["Route", "Family", "Words", "Title"],
            [[page.route, page.family, page.word_count, page.title] for page in sorted(thin_pages, key=lambda item: item.word_count)],
        ),
    )

    write(
        reports_dir / "schema_inventory.md",
        "# Schema Inventory\n\n"
        + markdown_table(
            ["Route", "Schema Types", "Missing"],
            [[page.route, ", ".join(page.schema_types) or "none", "yes" if page in missing_schema else "no"] for page in public_pages],
        ),
    )

    write(
        reports_dir / "image_inventory.md",
        "# Image Inventory\n\n"
        + f"Total public-page image references: {len(image_rows)}\n\nMissing alt attributes: {missing_alt}\n\n"
        + markdown_table(["Route", "Image", "Alt"], image_rows[:250]),
    )

    featured_reviews = reviews.get("featuredReviews", []) if isinstance(reviews.get("featuredReviews"), list) else []
    write(
        reports_dir / "review_inventory.md",
        "# Review Inventory\n\n"
        + markdown_table(
            ["Metric", "Value"],
            [
                ["Source", reviews.get("sourceName", "unknown")],
                ["Review count", reviews.get("reviewCount", "unknown")],
                ["Rating", reviews.get("ratingValue", "unknown")],
                ["Featured reviews", len(featured_reviews)],
                ["Last verified", reviews.get("lastVerified", "unknown")],
            ],
        )
        + "\n\n## Featured Review Themes\n\n"
        + "\n".join(f"- {item}" for item in reviews.get("summaryHighlights", [])),
    )

    faq_pages = [page for page in public_pages if page.faq_count]
    write(
        reports_dir / "faq_inventory.md",
        "# FAQ Inventory\n\n"
        + markdown_table(["Route", "FAQ Count", "Title"], [[page.route, page.faq_count, page.title] for page in faq_pages]),
    )

    write(
        reports_dir / "entity_inventory.md",
        "# Entity Inventory\n\n## Location Entities\n\n"
        + markdown_table(
            ["Location", "Pages", "Images", "FAQs", "Review Mentions"],
            [[loc, data["pages"], data["images"], data["faqs"], data["reviews"]] for loc, data in graph["location_dimensions"].items()],
        )
        + "\n\n## Service Entities\n\n"
        + markdown_table(
            ["Service", "Pages", "Images", "FAQs", "Review Mentions"],
            [[svc, data["pages"], data["images"], data["faqs"], data["reviews"]] for svc, data in graph["service_dimensions"].items()],
        ),
    )

    script_files = sorted(
        path.relative_to(root).as_posix()
        for folder in ["tools", "scripts", "seo-automation/scripts", "functions"]
        for path in (root / folder).rglob("*")
        if path.is_file()
    )
    write(
        reports_dir / "automation_report.md",
        "# Automation Inventory\n\n"
        + markdown_table(["Automation Surface"], [[path] for path in script_files])
        + "\n\n## Automation Opportunities\n\n"
        + "- Promote repository intelligence generation into a regular validation command.\n"
        + "- Use coverage matrices to choose one production improvement per reporting sprint.\n"
        + "- Add CI checks after the report generator stabilizes.\n",
    )

    write(
        reports_dir / "technical_debt.md",
        "# Technical Debt Report\n\n"
        + markdown_table(
            ["Issue", "Count", "Recommended next action"],
            [
                ["Missing page titles", len(missing_titles), "Add source metadata or build injection."],
                ["Missing meta descriptions", len(missing_descriptions), "Add source metadata or SEO map entries."],
                ["Public pages missing schema", len(missing_schema), "Inspect schema generator coverage."],
                ["Thin content candidates", len(thin_pages), "Prioritize pages with authority or conversion value."],
                ["Orphan sitemap pages", len(orphan_pages), "Add relevant internal links or remove from sitemap if not public."],
                ["Image references missing alt", missing_alt, "Patch source image alt text or generator data."],
            ],
        ),
    )

    write(
        reports_dir / "build_report.md",
        "# Build Health\n\n"
        + markdown_table(
            ["Metric", "Value"],
            [
                ["Date", build["date"]],
                ["Command", build["command"]],
                ["Exit code", build["returncode"]],
                ["Public routes detected", len(public_pages)],
                ["Sitemap routes", len(platform["sitemap_routes"])],
            ],
        )
        + "\n\n## Build Output Tail\n\n```text\n"
        + str(build.get("stdout_tail", "")).strip()
        + "\n```\n\n## Build Error Tail\n\n```text\n"
        + str(build.get("stderr_tail", "")).strip()
        + "\n```\n",
    )

    gap_rows = []
    for loc, services in graph["location_service"].items():
        for svc, count in services.items():
            if count == 0:
                gap_rows.append([loc, svc, "missing"])
    write(
        reports_dir / "content_gap_report.md",
        "# Content Gap Report\n\n"
        + "This first-pass report flags location-service pairs with no detected page-level co-mention.\n\n"
        + markdown_table(["Location", "Service", "Status"], gap_rows[:250]),
    )

    write(
        reports_dir / "coverage_matrices.md",
        "# Coverage Matrices\n\n## Location -> Service\n\n"
        + markdown_table(
            ["Location", *SERVICE_TERMS],
            [[loc, *[services[svc] for svc in SERVICE_TERMS]] for loc, services in graph["location_service"].items()],
        )
        + "\n\n## Location -> Dimensions\n\n"
        + markdown_table(
            ["Location", "Pages", "FAQs", "Images", "Articles", "Schema Pages", "Reviews"],
            [[loc, data["pages"], data["faqs"], data["images"], data["articles"], data["schema_pages"], data["reviews"]] for loc, data in graph["location_dimensions"].items()],
        ),
    )

    write(
        reports_dir / "authority_report.md",
        "# AI Authority Report\n\n"
        + markdown_table(
            ["Prompt", "Coverage", "Confidence", "Supporting Pages", "Schema Pages", "Sample Routes"],
            [
                [
                    prompt,
                    f"{data['coverage']}%",
                    data["confidence"],
                    data["supporting_pages"],
                    data["schema_pages"],
                    ", ".join(data["sample_routes"]),
                ]
                for prompt, data in prompt_scores.items()
            ],
        )
        + "\n\n## Immediate Authority Opportunities\n\n"
        + "- Use the content gap report to choose production page improvements before adding more internal reports.\n"
        + "- Strengthen low-confidence prompt families with visible content, internal links, image alt text, and schema.\n"
        + "- Keep internal reporting below the website-quality and AI-authority priorities in the Constitution.\n",
    )

    edges = []
    for page in public_pages:
        entities = graph["page_entities"].get(page.route, {})
        for loc in entities.get("locations", []):
            edges.append([loc, "mentioned on", page.route])
        for svc in entities.get("services", []):
            edges.append([svc, "covered by", page.route])
    write(
        reports_dir / "knowledge_graph.md",
        "# Knowledge Graph\n\n"
        + "This is a lightweight relationship graph for future automation. It should stay simple until a stronger need exists.\n\n"
        + markdown_table(["Entity", "Relationship", "Route"], edges[:300]),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate SRAAP repository intelligence reports.")
    parser.add_argument("--root", default=".", help="Repository root to inspect.")
    parser.add_argument("--reports-dir", default="", help="Output reports directory. Defaults to <root>/reports.")
    parser.add_argument("--skip-build", action="store_true", help="Skip npm run build:cloudflare and inspect existing cloudflare-preview.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    reports_dir = Path(args.reports_dir).resolve() if args.reports_dir else root / "reports"
    out_root = root / "cloudflare-preview"

    build = {"date": date.today().isoformat(), "command": "skipped", "returncode": 0, "stdout_tail": "", "stderr_tail": ""}
    if not args.skip_build:
        build = run_build(root)
        if int(build["returncode"]) != 0:
            reports_dir.mkdir(parents=True, exist_ok=True)
            write(reports_dir / "build_report.md", "# Build Health\n\nBuild failed before repository intelligence could be generated.\n")
            print("Build failed. See reports/build_report.md.", file=sys.stderr)
            return int(build["returncode"])

    if not out_root.exists():
        print(f"Missing build output: {out_root}", file=sys.stderr)
        return 1

    pages, platform = load_pages(root, out_root)
    reviews = load_reviews(root)
    generate_reports(root, reports_dir, pages, build, platform, reviews)
    print(f"Generated repository intelligence reports in {reports_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
