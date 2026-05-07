import argparse
import os
import re
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse


HREF_SRC_RE = re.compile(r'\b(?:href|src)\s*=\s*"([^"]+)"', re.IGNORECASE)


SKIP_PREFIXES = (
    "mailto:",
    "tel:",
    "sms:",
    "javascript:",
    "#",
)


SKIP_SCHEMES = {"http", "https"}


@dataclass(frozen=True)
class LinkIssue:
    source: Path
    raw: str
    resolved: Path | None
    reason: str


def _strip_fragment_and_query(url: str) -> str:
    url = url.split("#", 1)[0]
    url = url.split("?", 1)[0]
    return url


def _looks_external(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme) and parsed.scheme in SKIP_SCHEMES and bool(parsed.netloc)


def _to_local_path(site_root: Path, source_file: Path, url: str, canonical_domains: set[str]) -> Path | None:
    url = _strip_fragment_and_query(url.strip())
    if not url:
        return None

    for prefix in SKIP_PREFIXES:
        if url.lower().startswith(prefix):
            return None

    parsed = urlparse(url)
    if parsed.scheme and parsed.scheme in SKIP_SCHEMES and parsed.netloc:
        # Treat absolute links to canonical domains as internal; ignore other domains.
        host = parsed.netloc.lower()
        if host in canonical_domains:
            url = parsed.path or "/"
        else:
            return None

    if url.startswith("//"):
        return None

    # Root-relative
    if url.startswith("/"):
        rel = url.lstrip("/")
        if not rel:
            return site_root / "index.html"
        candidate = site_root / rel
        # If link points to a directory route like "/services", expect "/services/index.html"
        if candidate.is_dir():
            return candidate / "index.html"
        if candidate.suffix:
            return candidate
        # Common Webflow-ish / static routing
        if (candidate / "index.html").exists():
            return candidate / "index.html"
        if (candidate.with_suffix(".html")).exists():
            return candidate.with_suffix(".html")
        return candidate

    # Relative path
    base_dir = source_file.parent
    candidate = (base_dir / url).resolve()
    try:
        candidate.relative_to(site_root.resolve())
    except ValueError:
        # Prevent escaping the site root
        return None

    if candidate.is_dir():
        return candidate / "index.html"
    if candidate.suffix:
        return candidate
    if (candidate / "index.html").exists():
        return candidate / "index.html"
    if (candidate.with_suffix(".html")).exists():
        return candidate.with_suffix(".html")
    return candidate


def find_issues(site_root: Path, canonical_domains: set[str]) -> list[LinkIssue]:
    issues: list[LinkIssue] = []

    for html_path in sorted(site_root.rglob("*.html")):
        try:
            content = html_path.read_text(encoding="utf-8", errors="ignore")
        except OSError as exc:
            issues.append(LinkIssue(source=html_path, raw="", resolved=None, reason=f"read_error:{exc}"))
            continue

        for match in HREF_SRC_RE.finditer(content):
            raw = match.group(1).strip()
            if not raw:
                continue

            # Skip obvious external links early
            if _looks_external(raw):
                continue

            resolved = _to_local_path(site_root, html_path, raw, canonical_domains)
            if resolved is None:
                continue

            # ignore common non-file routes that are expected to be server-handled
            # (keep this minimal; most site routes should exist in static export)
            if "/api/" in raw:
                continue

            if not resolved.exists():
                issues.append(LinkIssue(source=html_path, raw=raw, resolved=resolved, reason="missing"))

    return issues


def render_markdown(issues: list[LinkIssue], site_root: Path, max_sources: int = 80, max_links_per_source: int = 20) -> str:
    if not issues:
        return f"# Internal Link Check\n\nNo missing internal links found under `{site_root}`.\n"

    by_source: dict[Path, list[LinkIssue]] = {}
    for issue in issues:
        by_source.setdefault(issue.source, []).append(issue)

    lines: list[str] = []
    lines.append("# Internal Link Check")
    lines.append("")
    lines.append(f"Site root: `{site_root}`")
    lines.append("")
    lines.append(f"Missing links found: **{len(issues)}**")
    lines.append("")

    for i, (source, items) in enumerate(sorted(by_source.items(), key=lambda kv: str(kv[0]))):
        if i >= max_sources:
            lines.append(f"- Truncated: more than {max_sources} source files with issues.")
            break
        rel_source = source.relative_to(site_root)
        lines.append(f"## `{rel_source.as_posix()}`")
        lines.append("")
        for j, item in enumerate(items[:max_links_per_source]):
            resolved_rel = None
            if item.resolved is not None:
                try:
                    resolved_rel = item.resolved.relative_to(site_root)
                except ValueError:
                    resolved_rel = item.resolved
            lines.append(f"- `{item.raw}` -> `{resolved_rel}` ({item.reason})")
        if len(items) > max_links_per_source:
            lines.append(f"- Truncated: more than {max_links_per_source} missing links in this file.")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Check internal links in a static site folder.")
    parser.add_argument("--root", required=True, help="Path to static site root (e.g. cloudflare-preview)")
    parser.add_argument("--out", required=False, help="Write markdown report to this file path")
    parser.add_argument(
        "--canonical-domain",
        action="append",
        default=[],
        help="Canonical domains to treat as internal (repeatable), e.g. www.sunray-cleaning.com",
    )
    args = parser.parse_args()

    site_root = Path(args.root).resolve()
    if not site_root.exists() or not site_root.is_dir():
        raise SystemExit(f"root not found or not a directory: {site_root}")

    canonical_domains = {d.strip().lower() for d in args.canonical_domain if d.strip()}
    # Provide a sane default if caller didn't specify
    canonical_domains.update({"www.sunray-cleaning.com", "sunray-cleaning.com"})

    issues = find_issues(site_root=site_root, canonical_domains=canonical_domains)
    report = render_markdown(issues=issues, site_root=site_root)

    if args.out:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report, encoding="utf-8")
    else:
        print(report)

    return 1 if issues else 0


if __name__ == "__main__":
    raise SystemExit(main())

