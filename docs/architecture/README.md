# Architecture

## Current System

Sun Ray Cleaning is a static website built for Cloudflare Pages.

The current source model is:

- Root `*-gpt.html` files for top-level pages.
- `services/*-gpt.html` for service pages.
- `service-location/*-gpt.html` for city, county, and neighborhood pages.
- `blog/*-gpt.html` for guides.
- `data/` for reusable reviews, galleries, and structured content.
- `assets/` for images and icons.
- `tools/build-cloudflare-preview.py` for route generation, clean URL output, link rewriting, SEO injection, schema output, redirects, headers, sitemap, robots, and `llms.txt`.

The current output model is:

- `cloudflare-preview/` generated for Cloudflare Pages.
- Clean extensionless public URLs.
- Preview builds noindex by default.
- Production builds use production canonical URLs and crawlable robots behavior.

## Protected Surfaces

Treat these as high-impact:

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

Changes to protected surfaces require build validation and careful diff review.

## Target Platform Architecture

SRAAP should evolve toward:

- Route metadata as a source of truth.
- Page templates for repeated content types.
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
- The build system should become more modular only when it reduces real complexity.
- New content types should come with templates, route metadata, schema rules, and validation rules.
- Repeated manual edits should become generator capabilities.
- External dependencies require a decision record.
