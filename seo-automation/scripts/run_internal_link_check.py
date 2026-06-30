import argparse
from datetime import datetime
from pathlib import Path


def _today_stamp() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run the internal-link checker and write a dated markdown report under seo-automation/runs/."
    )
    parser.add_argument(
        "--root",
        required=True,
        help="Path to static site root (e.g. cloudflare-preview)",
    )
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
    site_root = (repo_root / args.root).resolve()
    out_dir = (repo_root / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    out_path = out_dir / f"{args.stamp}-internal-link-report.md"
    checker = repo_root / "seo-automation" / "scripts" / "check_internal_links.py"

    cmd = [
        "python",
        str(checker),
        "--root",
        str(site_root),
        "--out",
        str(out_path),
    ]

    import subprocess

    completed = subprocess.run(cmd, check=False)
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
