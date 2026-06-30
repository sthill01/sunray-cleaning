# Architecture

Version: 2.1

Last Updated: 2026-06-30

This is the daily-read architecture map. The expanded architecture notes live in `docs/architecture/README.md`.

## Current System

Sun Ray Cleaning is a static website built for Cloudflare Pages.

The source model uses:

- Root `*-gpt.html` files for top-level pages.
- `services/*-gpt.html` for service pages.
- `service-location/*-gpt.html` for city, county, and neighborhood pages.
- `blog/*-gpt.html` for guides.
- `data/` for reusable reviews, galleries, and structured content.
- `assets/` for images and icons.
- `tools/build-cloudflare-preview.py` for route generation, clean URL output, link rewriting, SEO injection, schema output, redirects, headers, sitemap, robots, and `llms.txt`.

The output model uses:

- `cloudflare-preview/` generated for Cloudflare Pages.
- Clean extensionless public URLs.
- Preview builds with noindex behavior.
- Production builds with production canonical URLs and crawlable robots behavior.

## Protected Surfaces

Treat these as high-impact files:

- `tools/build-cloudflare-preview.py`
- `package.json`
- `worker.js`
- `functions/api/quote.js`
- `quote-modal-gpt.js`
- `styles-gpt.css`
- `robots.txt`
- `sitemap.xml`
- `data/reviews.json`
- `data/job-gallery.json`
- `data/social-gallery.json`

Changes to protected surfaces require focused diff review and relevant validation.

## Target Architecture

SRAAP should evolve toward:

- Route metadata as a source of truth.
- Reusable page templates for repeated content types.
- Shared schema builders.
- Internal-link graph generation.
- Content inventory reports.
- Schema and metadata validation.
- Image metadata coverage checks.
- AI authority coverage reports.
- CI-ready validation.
- Dashboards for health, visibility, and opportunity.

## Architecture Principles

- Generated output is not the source of truth.
- Preserve the existing Cloudflare Pages pipeline unless an ADR changes it.
- Prefer structured data files and generators over repeated manual edits.
- Add abstractions only when they reduce real complexity or make scale safer.
- New content types should include route metadata, schema rules, link rules, and validation.
- External dependencies require a decision record when they affect long-term architecture.

## Current Architecture Risks

- `tools/build-cloudflare-preview.py` is a high-value, high-complexity file.
- Route, metadata, schema, sitemap, and `llms.txt` logic are not yet fully modular.
- Content coverage and internal-link quality are not yet measured by a first-class report.
- AI visibility is not yet measured with a durable prompt set.

## Architecture Next Step

Create a route and content inventory report that can become the source for coverage, internal-link, schema, metadata, and AI-authority audits.
