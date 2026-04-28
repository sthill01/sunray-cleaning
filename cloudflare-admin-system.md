# Sun Ray Cloudflare Admin System Plan

This repo now has a deployable static preview in `cloudflare-preview/`. The admin system should be added behind Cloudflare Access instead of relying on an unprotected static page.

## Recommended Architecture

- Host static public pages on Cloudflare Pages from `cloudflare-preview/`.
- Protect `/admin/*` with Cloudflare Access before enabling editing.
- Use Pages Functions for admin APIs under `/api/admin/*`.
- Use D1 for structured content: pages, blog posts, service areas, FAQs, testimonials, redirects, and form submissions.
- Use R2 for uploaded images if the team needs asset uploads.
- Keep production publishing static: admin edits create approved content, then a build process regenerates clean HTML pages and deploys.

## Current Scaffold

- `cloudflare-preview/admin/index.html`: admin placeholder route.
- `functions/api/admin/content.js`: API readiness endpoint.
- `functions/api/quote.js`: quote form endpoint with optional webhook forwarding.
- `wrangler.toml`: Cloudflare Pages output config.
- `tools/build-cloudflare-preview.py`: regenerates the clean URL preview build from GPT source pages.
- `data/reviews.json`: Google Business Profile aggregate-rating source and future approved review excerpts.
- `data/job-gallery.json`: curated job-photo metadata with service, location, keywords, alt text, captions, and target routes.

## Review Integration Workflow

- Store the Google Business Profile aggregate rating and review count in `data/reviews.json`.
- Do not invent individual review text. Add exact review excerpts only after export/owner approval.
- Use approved excerpts on high-conversion pages first: home, Park City, Airbnb/VRBO cleaning, deep cleaning, recurring cleaning, move cleaning, and contact.
- Keep review schema conservative: aggregate rating can be sitewide, while individual `Review` schema should only be added for exact public reviews.
- The automated importer lives at `scripts/import-google-reviews.mjs` and can be run with `npm run import:google-reviews`.
- The scheduled GitHub automation lives at `.github/workflows/import-google-reviews.yml` and runs daily plus manually from GitHub Actions.
- Required GitHub secrets: `GBP_ACCOUNT_ID`, `GBP_LOCATION_ID`, `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, and `GOOGLE_REFRESH_TOKEN`.
- Optional GitHub secret: `GBP_PROFILE_URL`, used as the source URL for review cards and schema.
- Anonymous Google reviewers stay anonymous. The importer only stores reviewer names and profile photos when Google returns them for non-anonymous reviews.

## Job Photo Workflow

- Add only selected, high-quality job photos to `assets/`; do not bulk-import every image.
- Add every published job photo to `data/job-gallery.json` with descriptive alt text, service type, city/neighborhood, caption, keywords, and route targets.
- Prioritize galleries on service pages, Park City/Heber/Midway pages, Airbnb/VRBO blog posts, and deep-clean/move-clean guides.
- For future admin uploads, store originals in R2, generate optimized web images, then write approved metadata into the build source before publishing.
- Use local SEO photo labels naturally: service + room/detail + city/neighborhood, for example `Park City Airbnb kitchen turnover cleaning by Sun Ray Cleaning Services`.

## Deployment Notes

1. Run `npm install`.
2. Run `npm run build:cloudflare`.
3. Deploy preview with `npm run deploy:preview`.
4. In Cloudflare Pages settings, add `SUNRAY_QUOTE_WEBHOOK_URL` if quote requests should forward to a CRM or automation webhook.
5. Before real admin writes, configure Cloudflare Access for `/admin/*`.
