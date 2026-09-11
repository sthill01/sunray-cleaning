import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "cloudflare-preview"
SOURCE = ROOT / "ai-cleaning-recommendations-gpt.html"
BUILD_SCRIPT = ROOT / "tools" / "build-cloudflare-preview.py"


class AIRecommendationIndexabilityContractTests(unittest.TestCase):
    def build_site(self, *, production: bool) -> None:
        env = os.environ.copy()
        for name in ("CF_PAGES_BRANCH", "WORKERS_CI_BRANCH", "CF_BRANCH", "SUNRAY_ALLOW_INDEXING"):
            env.pop(name, None)

        if production:
            env["SUNRAY_SITE_BASE_URL"] = "https://www.sunray-cleaning.com"
            env["SUNRAY_ALLOW_INDEXING"] = "1"
        else:
            env["SUNRAY_SITE_BASE_URL"] = "https://sunray-cleaning-preview.pages.dev"

        result = subprocess.run(
            [sys.executable, str(BUILD_SCRIPT)],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stderr or result.stdout)

    def test_preview_source_and_build_stay_noindex_while_production_is_indexable(self):
        source = SOURCE.read_text(encoding="utf-8-sig")
        self.assertIn('<meta name="robots" content="noindex, follow">', source)

        self.build_site(production=False)
        preview_page = (OUTPUT / "ai-cleaning-recommendations" / "index.html").read_text(encoding="utf-8")
        preview_headers = (OUTPUT / "_headers").read_text(encoding="utf-8")
        preview_robots = (OUTPUT / "robots.txt").read_text(encoding="utf-8")

        self.assertIn('<meta name="robots" content="noindex, follow">', preview_page)
        self.assertIn("X-Robots-Tag: noindex, follow", preview_headers)
        self.assertIn("Disallow: /", preview_robots)

        self.build_site(production=True)
        production_page = (OUTPUT / "ai-cleaning-recommendations" / "index.html").read_text(encoding="utf-8")
        production_headers = (OUTPUT / "_headers").read_text(encoding="utf-8")
        production_robots = (OUTPUT / "robots.txt").read_text(encoding="utf-8")
        production_sitemap = (OUTPUT / "sitemap.xml").read_text(encoding="utf-8")

        self.assertIn('<meta name="robots" content="index, follow">', production_page)
        self.assertNotIn("X-Robots-Tag: noindex", production_headers)
        self.assertIn("Allow: /", production_robots)
        self.assertIn(
            "https://www.sunray-cleaning.com/ai-cleaning-recommendations/",
            production_sitemap,
        )

        self.assertIn(
            '<meta name="robots" content="noindex, follow">',
            SOURCE.read_text(encoding="utf-8-sig"),
        )


if __name__ == "__main__":
    unittest.main()
