from __future__ import annotations

import csv
import re
import sys
import time
import xml.etree.ElementTree as ET
from collections import deque
from dataclasses import dataclass
from datetime import datetime, timezone
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "webflow-fix-pack"
PREVIEW_SITEMAP = ROOT / "cloudflare-preview" / "sitemap.xml"
CURRENT_SITE = "https://www.sunray-cleaning.com"
USER_AGENT = "Mozilla/5.0 SunRayMigrationAudit/1.0"
MAX_PAGES = 250


@dataclass
class PageResult:
    url: str
    route: str
    status: int
    title: str = ""
    description: str = ""
    canonical: str = ""
    content_type: str = ""
    source: str = "crawl"
    error: str = ""


class LinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: list[str] = []
        self.title_parts: list[str] = []
        self.in_title = False
        self.description = ""
        self.canonical = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {name.lower(): value or "" for name, value in attrs}
        if tag.lower() == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"])
        elif tag.lower() == "link" and attrs_dict.get("rel", "").lower() == "canonical":
            self.canonical = attrs_dict.get("href", "")
        elif tag.lower() == "meta" and attrs_dict.get("name", "").lower() == "description":
            self.description = attrs_dict.get("content", "")
        elif tag.lower() == "title":
            self.in_title = True

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_parts.append(data)

    @property
    def title(self) -> str:
        return " ".join(part.strip() for part in self.title_parts if part.strip())


def fetch(url: str) -> tuple[int, str, str, str]:
    request = Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urlopen(request, timeout=20) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            body = response.read(2_000_000).decode(charset, "replace")
            return response.status, response.getheader("content-type", ""), body, ""
    except HTTPError as exc:
        body = exc.read(250_000).decode("utf-8", "replace")
        return exc.code, exc.headers.get("content-type", ""), body, str(exc)
    except URLError as exc:
        return 0, "", "", str(exc)


def normalize_url(url: str, base: str = CURRENT_SITE) -> str | None:
    if url.startswith(("mailto:", "tel:", "sms:", "javascript:", "#")):
        return None
    absolute, _ = urldefrag(urljoin(base, url))
    parsed = urlparse(absolute)
    if parsed.scheme not in {"http", "https"}:
        return None
    if parsed.netloc.lower() != urlparse(CURRENT_SITE).netloc.lower():
        return None
    path = re.sub(r"/+", "/", parsed.path or "/")
    if path != "/" and path.endswith("/"):
        path = path.rstrip("/")
    return urlunparse(("https", parsed.netloc.lower(), path, "", parsed.query, ""))


def route_for_url(url: str) -> str:
    parsed = urlparse(url)
    path = re.sub(r"/+", "/", parsed.path or "/")
    if path == "":
        path = "/"
    return path


def clean_route(route: str) -> str:
    route = re.sub(r"/+", "/", route or "/")
    if route != "/" and route.endswith("/"):
        route = route.rstrip("/")
    return route


def load_preview_routes() -> set[str]:
    if not PREVIEW_SITEMAP.exists():
        return set()
    xml_text = PREVIEW_SITEMAP.read_text(encoding="utf-8")
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_text)
    routes: set[str] = set()
    for loc in root.findall(".//sm:loc", namespace):
        if loc.text:
            routes.add(clean_route(urlparse(loc.text).path or "/"))
    return routes


def read_existing_redirects() -> dict[str, str]:
    redirects_path = ROOT / "cloudflare-preview" / "_redirects"
    redirects: dict[str, str] = {}
    if not redirects_path.exists():
        return redirects
    for raw in redirects_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            redirects[clean_route(parts[0])] = clean_route(parts[1])
    return redirects


def discover_sitemap_urls() -> tuple[list[str], int]:
    status, content_type, body, _ = fetch(f"{CURRENT_SITE}/sitemap.xml")
    if status != 200 or "xml" not in content_type.lower():
        return [], status
    root = ET.fromstring(body)
    namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    urls: list[str] = []
    for loc in root.findall(".//sm:loc", namespace):
        if loc.text:
            normalized = normalize_url(loc.text)
            if normalized:
                urls.append(normalized)
    return sorted(set(urls)), status


def crawl(seed_urls: Iterable[str]) -> list[PageResult]:
    queue: deque[str] = deque(seed_urls)
    seen: set[str] = set()
    results: list[PageResult] = []
    while queue and len(seen) < MAX_PAGES:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)
        status, content_type, body, error = fetch(url)
        parser = LinkParser()
        if body and "html" in content_type.lower():
            parser.feed(body)
            for href in parser.links:
                next_url = normalize_url(href, url)
                if next_url and next_url not in seen and next_url not in queue:
                    queue.append(next_url)
        results.append(
            PageResult(
                url=url,
                route=route_for_url(url),
                status=status,
                title=unescape(parser.title).strip(),
                description=unescape(parser.description).strip(),
                canonical=parser.canonical.strip(),
                content_type=content_type,
                error=error,
            )
        )
        time.sleep(0.1)
    return sorted(results, key=lambda item: item.route)


def suggest_target(route: str, preview_routes: set[str]) -> str:
    route_clean = clean_route(route)
    if route_clean in preview_routes:
        return route_clean
    aliases = {
        "/service-location/midway-heber": "/service-location/wasatch-county",
        "/service-location/heber-midway": "/service-location/wasatch-county",
        "/park-city": "/service-location/park-city",
        "/heber": "/service-location/heber-city",
        "/midway": "/service-location/midway",
        "/salt-lake": "/service-location/salt-lake-county",
        "/quote": "/contact",
        "/get-a-quote": "/contact",
        "/contact-us": "/contact",
    }
    if route_clean in aliases and aliases[route_clean] in preview_routes:
        return aliases[route_clean]
    slug = route_clean.rstrip("/").split("/")[-1]
    for prefix in ("/blog/", "/service-location/", "/services/"):
        candidate = prefix + slug
        if candidate in preview_routes:
            return candidate
    return ""


def write_outputs(results: list[PageResult], preview_routes: set[str], sitemap_status: int) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    redirects = read_existing_redirects()
    rows: list[dict[str, str]] = []
    redirect_rows: list[dict[str, str]] = []
    for item in results:
        route = clean_route(item.route)
        target = suggest_target(route, preview_routes)
        covered_by_page = "yes" if route in preview_routes else "no"
        covered_by_redirect = "yes" if route in redirects else "no"
        target = target or redirects.get(route, "")
        action = "covered"
        if covered_by_page == "no" and target:
            redirect_rows.append({"source": route, "target": target, "status": "301"})
        if item.status >= 400 and not target:
            action = "live_error"
        elif covered_by_page == "no" and covered_by_redirect == "yes":
            action = "covered_by_redirect"
        elif covered_by_page == "no" and covered_by_redirect == "no" and target:
            action = "add_redirect"
        elif covered_by_page == "no" and covered_by_redirect == "no":
            action = "needs_decision"
        rows.append(
            {
                "current_url": item.url,
                "current_route": route,
                "current_status": str(item.status),
                "title": item.title,
                "description": item.description,
                "canonical": item.canonical,
                "new_route_exists": covered_by_page,
                "redirect_exists": covered_by_redirect,
                "recommended_target": target,
                "action": action,
            }
        )

    sitemap_csv = OUT_DIR / "current-webflow-sitemap.csv"
    with sitemap_csv.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()) if rows else ["current_url"])
        writer.writeheader()
        writer.writerows(rows)

    redirects_csv = OUT_DIR / "webflow-launch-redirects.csv"
    with redirects_csv.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["source", "target", "status"])
        writer.writeheader()
        writer.writerows(redirect_rows)

    sitemap_xml = OUT_DIR / "current-webflow-sitemap.xml"
    live_urls = [row["current_url"] for row in rows if row["current_status"].startswith("2")]
    sitemap_xml.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "\n".join(f"  <url><loc>{url}</loc></url>" for url in live_urls)
        + "\n</urlset>\n",
        encoding="utf-8",
    )

    page_count = len([row for row in rows if row["current_status"].startswith("2")])
    direct_count = len([row for row in rows if row["new_route_exists"] == "yes"])
    redirect_count = len(redirect_rows)
    covered_redirect_count = len([row for row in rows if row["action"] == "covered_by_redirect"])
    add_redirect_count = len([row for row in rows if row["action"] == "add_redirect"])
    needs_decision = [row for row in rows if row["action"] == "needs_decision"]
    live_errors = [row for row in rows if row["action"] == "live_error"]
    discovered_errors = [row for row in rows if int(row["current_status"] or "0") >= 400]

    def route_lines(subset: list[dict[str, str]]) -> str:
        if not subset:
            return "- None"
        return "\n".join(
            f"- `{row.get('current_route', row.get('source', ''))}` -> `{row.get('recommended_target', row.get('target', 'TBD')) or 'TBD'}` ({row.get('title') or row.get('current_status') or row.get('status') or 'review'})"
            for row in subset
        )

    discovered_lines = "\n".join(
        f"- `{row['current_route']}` -> {row['current_status']} -> `{row['recommended_target'] or ('same route' if row['new_route_exists'] == 'yes' else 'TBD')}`"
        for row in rows
    )

    report = OUT_DIR / "webflow-migration-route-audit.md"
    report.write_text(
        f"""# Webflow Migration Route Audit

Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}

Current Webflow site: {CURRENT_SITE}
Preview sitemap checked: `cloudflare-preview/sitemap.xml`

## Summary

- Current Webflow `/sitemap.xml` status: `{sitemap_status}`.
- Live internal routes discovered: {len(rows)}
- Live 2xx pages discovered: {page_count}
- Routes already covered by matching preview pages: {direct_count}
- Launch redirects covered or recommended: {redirect_count}
- Redirects already present in `_redirects`: {covered_redirect_count}
- Redirects still missing from `_redirects`: {add_redirect_count}
- Needs manual decision: {len(needs_decision)}
- Live 4xx/5xx routes discovered during crawl: {len(discovered_errors)}
- Uncovered live errors after redirect mapping: {len(live_errors)}

## Launch Redirects

{route_lines(redirect_rows)}

## Needs Decision

{route_lines(needs_decision)}

## Live Error Routes Covered Or Flagged

{route_lines(discovered_errors)}

## Discovered Current Sitemap

{discovered_lines}

## Files

- CSV sitemap and coverage: `webflow-fix-pack/current-webflow-sitemap.csv`
- XML sitemap of current 2xx Webflow pages: `webflow-fix-pack/current-webflow-sitemap.xml`
- Redirect import CSV: `webflow-fix-pack/webflow-launch-redirects.csv`
""",
        encoding="utf-8",
    )

    print(f"Wrote {sitemap_csv}")
    print(f"Wrote {sitemap_xml}")
    print(f"Wrote {redirects_csv}")
    print(f"Wrote {report}")
    print(f"Discovered {len(rows)} live routes; {direct_count} direct matches; {redirect_count} launch redirects; {len(needs_decision)} decisions.")


def main() -> int:
    preview_routes = load_preview_routes()
    if not preview_routes:
        print("No preview sitemap found. Run cmd /c npm run build:cloudflare first.", file=sys.stderr)
        return 1
    sitemap_urls, sitemap_status = discover_sitemap_urls()
    seeds = sitemap_urls or [CURRENT_SITE + "/"]
    results = crawl(seeds)
    write_outputs(results, preview_routes, sitemap_status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
