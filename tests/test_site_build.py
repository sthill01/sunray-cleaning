import os
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "cloudflare-preview"


class SiteBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        env = os.environ.copy()
        env["SUNRAY_SITE_BASE_URL"] = "https://www.sunray-cleaning.com"
        env["SUNRAY_ALLOW_INDEXING"] = "1"
        result = subprocess.run(
            [sys.executable, str(ROOT / "tools" / "build-cloudflare-preview.py")],
            cwd=ROOT,
            env=env,
            text=True,
            capture_output=True,
        )
        if result.returncode != 0:
            raise AssertionError(result.stderr or result.stdout)

    def test_custom_404_is_noindex_and_not_in_sitemap(self):
        not_found = (OUTPUT / "404.html").read_text(encoding="utf-8")
        sitemap = (OUTPUT / "sitemap.xml").read_text(encoding="utf-8")

        self.assertIn('<meta name="robots" content="noindex, nofollow">', not_found)
        self.assertIn("Page Not Found | Sun Ray Cleaning", not_found)
        self.assertIn("That page is not available.", not_found)
        self.assertNotIn("/404", sitemap)

    def test_production_crawl_controls_and_canonical(self):
        home = (OUTPUT / "index.html").read_text(encoding="utf-8")
        headers = (OUTPUT / "_headers").read_text(encoding="utf-8")
        redirects = (OUTPUT / "_redirects").read_text(encoding="utf-8")
        robots = (OUTPUT / "robots.txt").read_text(encoding="utf-8")
        sitemap = (OUTPUT / "sitemap.xml").read_text(encoding="utf-8")

        self.assertIn('<meta name="robots" content="index, follow">', home)
        self.assertIn('<link rel="canonical" href="https://www.sunray-cleaning.com/">', home)
        self.assertIn('href="/styles.css?v=20260721-footer-badge-fix"', home)
        self.assertNotIn("X-Robots-Tag: noindex", headers)
        self.assertIn("/about-us /about/ 301", redirects)
        self.assertIn("Allow: /", robots)
        self.assertIn("Sitemap: https://www.sunray-cleaning.com/sitemap.xml", robots)
        self.assertNotIn("pages.dev", sitemap)
        self.assertGreaterEqual(sitemap.count("<loc>"), 100)

    def test_generated_pages_do_not_expose_webflow_preview_copy(self):
        offenders = []
        for path in OUTPUT.rglob("*.html"):
            content = path.read_text(encoding="utf-8")
            if "Webflow preview" in content or "planning and Webflow" in content:
                offenders.append(str(path.relative_to(OUTPUT)))

        self.assertEqual([], offenders)

    def test_hidden_trustindex_fallback_cannot_override_its_hidden_state(self):
        styles = (OUTPUT / "styles.css").read_text(encoding="utf-8")

        self.assertIn(".trustindex-badge-fallback[hidden] {\n  display: none !important;\n}", styles)

    def test_worker_static_assets_use_a_real_404(self):
        config = (ROOT / "wrangler.worker.toml").read_text(encoding="utf-8")
        self.assertIn('not_found_handling = "404-page"', config)
        self.assertIn('run_worker_first = ["/api/*", "/404", "/404/"]', config)

    def test_markdown_negotiation_is_homepage_only(self):
        function_source = (ROOT / "functions" / "index.js").read_text(encoding="utf-8")
        self.assertIn('url.pathname === "/"', function_source)

    def test_explicit_404_routes_return_the_error_document(self):
        pages_function = (ROOT / "functions" / "404.js").read_text(encoding="utf-8")
        worker_source = (ROOT / "worker.js").read_text(encoding="utf-8")

        self.assertIn('new URL("/__sunray_custom_404__", request.url)', pages_function)
        self.assertIn("status: 404", pages_function)
        self.assertIn('url.pathname === "/404"', worker_source)
        self.assertIn("serveNotFoundPage(request, env)", worker_source)


if __name__ == "__main__":
    unittest.main()
