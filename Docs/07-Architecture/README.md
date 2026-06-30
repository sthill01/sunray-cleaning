# 07 Architecture

## Current Architecture

Sun Ray Cleaning is a static site built for Cloudflare Pages.

Current source model:

- Root `*-gpt.html` files for top-level pages.
- `services/*-gpt.html` for service pages.
- `service-location/*-gpt.html` for location and neighborhood pages.
- `blog/*-gpt.html` for blog guides.
- `data/` for reviews, gallery, and reusable structured content.
- `assets/` for images and icons.
- `tools/build-cloudflare-preview.py` for route generation, link rewriting, SEO injection, schema output, sitemap, robots, redirects, headers, and `llms.txt`.

Current output model:

- `cloudflare-preview/` is generated output for Cloudflare Pages.
- Public URLs are clean and extensionless.
- Preview builds are noindex by default.
- Production builds use production canonical URLs and crawlable robots settings.

## Protected Build Surfaces

Treat these as high-impact files:

- `tools/build-cloudflare-preview.py`
- `package.json`
- `worker.js`
- `functions/api/quote.js`
- `quote-modal-gpt.js`
- `styles-gpt.css`
- `robots.txt`
- `sitemap.xml`

Changes to these files require extra validation.

## Preferred Evolution

The build script may eventually be split into modules if it becomes too large, but only with a decision record and regression checks.

Preferred future architecture:

- Route metadata source of truth.
- Page templates for repeated content types.
- Shared schema builders.
- Automated internal-link graph checks.
- Content inventory and health reports.
- CI validation for build, links, sitemap, schema, and important route snapshots.

## Architecture Rules

- Do not add a new build tool unless the current Python build cannot reasonably support the need.
- Do not introduce a CMS dependency without a decision record.
- Do not make generated output the source of truth.
- Keep source pages and data files understandable by humans.
- Prefer additive generator capabilities over manual repeated edits.
