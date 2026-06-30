# Architecture

Date: 2026-06-30

## Repository Shape

The repository is a static Sun Ray Cleaning website with a Python-driven
Cloudflare Pages build pipeline.

Primary folders:

- `/assets`: images, favicon files, logos, and job-gallery assets.
- `/blog`: GPT-suffixed blog source pages.
- `/data`: structured reviews, social-gallery records, and job-gallery records.
- `/functions`: Cloudflare Functions for quote and admin API routes.
- `/service-location`: GPT-suffixed location and neighborhood source pages.
- `/services`: GPT-suffixed service source pages.
- `/tools`: build, audit, image, and report generation scripts.
- `/seo-automation`: legacy and active SEO automation notes, scripts, and runs.
- `/cloudflare-preview`: generated build output.
- `/docs`: SRAAP operating manual and project memory.
- `/reports`: generated Repository Intelligence reports.

## Build Pipeline

Build command:

```powershell
npm run build:cloudflare
```

The command runs:

```powershell
python tools/build-cloudflare-preview.py
```

Production build command:

```powershell
npm run build:production
```

The production command sets:

- `SUNRAY_SITE_BASE_URL=https://www.sunray-cleaning.com`
- `SUNRAY_ALLOW_INDEXING=1`

Generated output directory:

```text
cloudflare-preview/
```

Cloudflare Pages should keep using `cloudflare-preview` as the build output
directory.

## Route Generation

Source pages are GPT-suffixed HTML files. The build script maps them to clean
extensionless routes:

- `index-gpt.html` -> `/`
- `about-gpt.html` -> `/about/`
- `services/deep-cleaning-gpt.html` -> `/services/deep-cleaning/`
- `service-location/park-city-gpt.html` -> `/service-location/park-city/`
- `blog/example-gpt.html` -> `/blog/example/`

The build script currently discovers:

- root `*-gpt.html`
- `service-location/*-gpt.html`
- `services/*-gpt.html`
- `blog/*-gpt.html`

## SEO And AI Enhancements

`tools/build-cloudflare-preview.py` injects or writes:

- Clean internal links.
- Canonical tags.
- `llms.txt` alternate link.
- Structured data.
- Breadcrumb schema.
- LocalBusiness and HouseCleaningService schema.
- Service schema on service pages.
- BlogPosting schema on blog posts.
- FAQPage schema when FAQ markup exists.
- ImageObject schema based on gallery data.
- Review schema from approved review data.
- Sitemap.
- Robots file.
- Cloudflare `_headers`.
- Cloudflare `_redirects`.
- Review, gallery, and answer-network sections.

## Data Flow

Structured source data:

- `data/reviews.json`: Google Business Profile rating and approved featured
  reviews.
- `data/job-gallery.json`: approved local cleaning images with route, service,
  location, alt, caption, and keyword metadata.
- `data/social-gallery.json`: imported Meta gallery records, currently requiring
  approval before publication.

Build flow:

1. Read GPT source pages.
2. Rewrite source links to clean routes.
3. Inject SEO, schema, reviews, gallery, and answer-network enhancements.
4. Copy assets and public static files.
5. Write sitemap, robots, redirects, headers, and `llms.txt`.
6. Emit clean route files to `cloudflare-preview`.

## Cloudflare Functions

Current function areas:

- `/functions/api/quote.js`: quote request endpoint.
- `/functions/api/admin/content.js`: admin placeholder API.
- `/functions/d32p/[[path]].js`: route/function support path.

External integrations require environment variables or account access and should
be listed in `BLOCKERS.md` when unavailable.

## Existing Strengths

- Static build is simple and Cloudflare-compatible.
- Route generation is centralized.
- Structured data is generated programmatically.
- Reviews and gallery data are structured.
- Location and service route coverage is already broad.
- Build output includes sitemap, robots, headers, redirects, and `llms.txt`.

## Existing Weaknesses

- The build script is large and mixes routing, SEO, schema, link rewriting, and
  content injection.
- Route, entity, link, image, FAQ, and schema coverage were not previously
  generated as first-class reports.
- Project state and decisions were not centralized in `/docs`.
- Some source pages still reflect a GPT-preview origin and depend on build-time
  cleanup.
- External analytics and search-console verification are not fully documented in
  the repo.
