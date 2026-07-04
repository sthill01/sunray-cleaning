"""Check the isitagentready.com score for a site and log a dated report.

Read-only: posts a scan request and records the result. Never implements
findings automatically. Fake infrastructure (OAuth metadata for a
nonexistent auth server, API catalogs for APIs that don't exist, WebMCP
tools with no real actions behind them) is explicitly out of scope -- see
website-growth-system/10-agent-readiness-implementation-report-and-plan.md
"Do Not Do" for why.
"""

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

SCAN_ENDPOINT = "https://isitagentready.com/api/scan"


def _today_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def run_scan(url: str) -> dict:
    # Shell out to curl.exe rather than urllib: this project's Windows Python
    # install has an incomplete system cert bundle for urllib/ssl, while
    # curl.exe (Windows-bundled, schannel-backed) verifies cleanly.
    completed = subprocess.run(
        [
            "curl.exe",
            "-s",
            "--ssl-no-revoke",
            "-X",
            "POST",
            SCAN_ENDPOINT,
            "-H",
            "Content-Type: application/json",
            "--data-raw",
            json.dumps({"url": url}),
        ],
        capture_output=True,
        text=True,
        timeout=90,
        check=True,
    )
    return json.loads(completed.stdout)


def _walk_checks(checks: dict) -> list[tuple[str, str, str]]:
    rows = []
    for category, entries in (checks or {}).items():
        if not isinstance(entries, dict):
            continue
        for check_name, detail in entries.items():
            if isinstance(detail, dict):
                status = detail.get("status", "unknown")
                message = detail.get("message", "")
            else:
                status = str(detail)
                message = ""
            rows.append((category, check_name, status, message))
    return rows


def render_report(url: str, result: dict) -> str:
    overall = result.get("overall") or result.get("score")
    level = result.get("level")
    lines = [
        "# Agent Readiness Scan",
        "",
        f"Scanned URL: {url}",
        f"Scanned at: {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"Overall score: {overall}",
        f"Level: {level}",
        "",
        "## Checks",
        "",
        "| Category | Check | Status | Message |",
        "| --- | --- | --- | --- |",
    ]
    for category, check_name, status, message in _walk_checks(result.get("checks", {})):
        lines.append(f"| {category} | {check_name} | {status} | {message} |")
    lines.append("")
    lines.append("## Raw response")
    lines.append("")
    lines.append("```json")
    lines.append(json.dumps(result, indent=2))
    lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the isitagentready.com scan and write a dated markdown report."
    )
    parser.add_argument("--url", default="https://www.sunray-cleaning.com", help="Site to scan")
    parser.add_argument(
        "--out-dir",
        default="seo-automation/runs",
        help="Directory to write the dated report into (default: seo-automation/runs)",
    )
    parser.add_argument(
        "--stamp",
        default=_today_stamp(),
        help="Date stamp used in the report filename (default: today's date, YYYY-MM-DD)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parents[2]
    out_dir = (repo_root / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{args.stamp}-agent-readiness-scan.md"

    try:
        result = run_scan(args.url)
    except Exception as exc:  # noqa: BLE001 - report failure into the log instead of crashing silently
        out_path.write_text(
            f"# Agent Readiness Scan\n\nScanned URL: {args.url}\n"
            f"Scanned at: {datetime.now().isoformat(timespec='seconds')}\n\n"
            f"Scan FAILED: {exc}\n",
            encoding="utf-8",
        )
        print(f"Scan failed, wrote failure log to {out_path}")
        return 1

    out_path.write_text(render_report(args.url, result), encoding="utf-8")
    print(f"Wrote agent readiness report to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
