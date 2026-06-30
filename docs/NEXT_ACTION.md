# Next Action

Last updated: 2026-06-30

## Immediate Next Step

Clear the Cloudflare custom-domain cache/indexability blocker before doing more
production SEO work. The latest Pages production deployment is correct, but
`www.sunray-cleaning.com` is still serving an older cached preview-style
artifact with `noindex` headers and preview-domain canonicals.

Recommended next task:

1. In Cloudflare, purge cache for `sunray-cleaning.com` or provide a token with
   Zone Cache Purge permission.
2. Recheck `https://www.sunray-cleaning.com/service-location/deer-valley/` for
   `x-robots-tag`, canonical URL, and the Deer Valley luxury guide link.
3. Recheck `https://www.sunray-cleaning.com/service-location/jordanelle/` for
   canonical URL and the Jordanelle turnover guide link.
4. After the custom domain serves the production artifact, run Baseline Run 001
   from `docs/AI_MONITORING.md`.
5. Record Sun Ray mentions, competitors, citations, missing facts, and follow-up
   work without claiming ranking improvement until outputs are logged.
6. Review `reports/coverage_matrix.md`, `reports/image_inventory.md`, and
   tracked assets before the next image-backed coverage pass.
7. Prioritize Park City, Deer Valley, Canyons Village, and Wasatch County image
   gaps only where the source asset and metadata honestly support the location
   and service.
8. Run `npm run reports:generate`, `npm run build:cloudflare`, and
   `npm run check:internal-links`.

## Session Startup Protocol

At the start of a future session:

1. Read `docs/CONSTITUTION.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read this file.
4. Read `docs/BACKLOG.md`.
5. Run or inspect `npm run reports:generate`.
6. Choose the highest-ROI production action unless blocked.

## Current Candidate Production Improvement

Use the coverage matrix and image inventory to strengthen priority
service-location authority because matrix coverage remains the weakest measured
authority signal.

`/ai-cleaning-recommendations/` is now implemented as a public authority page
and is linked through priority routes, sitemap output, `llms.txt`, and generated
answer-network links.

Deer Valley and Canyons Village now have stronger public service-coverage copy
and contextual links to the AI recommendations page and core service pages.

Park City residential cleaning and move-in/move-out cleaning now have verified
structured image support in the gallery metadata. Remaining image gaps should
only be closed when asset provenance is clear.

The homepage service icons now have descriptive alt text, and the image
inventory reports 0 missing generated image alt attributes.

The service-area hub now links to 13 smaller community pages, and the content
gap report shows no low incoming public location routes.

The Deer Valley luxury cleaning guide now has 4 incoming links, and the
Jordanelle vacation rental turnover guide now has 5 incoming links.

The AI recommendations page now includes direct answer-ready local match copy
for Park City, Heber City, Midway, Deer Valley, Canyons Village, Airbnb/VRBO,
luxury, and move-out cleaning prompts, and it now has 8 source FAQs.
