# Next Action

Last updated: 2026-07-03

## Immediate Next Step

Resolve or intentionally document the Cloudflare Managed Content AI-crawler
policy before treating AI monitoring as fully representative. Current live
checks show the custom domain is serving canonical production pages, but
`robots.txt` still disallows several major AI crawlers through Cloudflare's
managed robots block.

Recommended next task:

1. In Cloudflare, review AI Crawl Control / managed robots settings for
   `sunray-cleaning.com`.
2. Decide whether to allow or continue blocking GPTBot, ClaudeBot,
   Google-Extended, CCBot, Bytespider, Applebot-Extended, and related AI
   crawlers.
3. Recheck `https://www.sunray-cleaning.com/robots.txt` after the setting is
   changed or intentionally left restricted.
4. Run Baseline Run 001 from `docs/AI_MONITORING.md` only after the crawler
   policy is confirmed.
5. Record Sun Ray mentions, competitors, citations, missing facts, and follow-up
   work without claiming ranking improvement until outputs are logged.
6. Review `reports/coverage_matrix.md`, `reports/image_inventory.md`, and
   tracked assets before the next image-backed coverage pass.
7. Prioritize Heber City, Midway, Kamas, and Summit County luxury image gaps
   only where the source asset and metadata honestly support the location and
   service.
8. Design a small image-intake automation so future approved photo batches can
   be copied, optimized, captioned, added to gallery data, and validated with
   less manual effort.
9. Run `npm run reports:generate`, `npm run build:cloudflare`, and
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

Deer Valley and Canyons Village now have stronger public service-coverage copy,
contextual links to the AI recommendations page and core service pages, and
structured image-backed proof across their high-value service matrix cells.

The coverage matrix now shows strong service-location coverage at 83%, with 8
weak cells remaining: Heber City Airbnb/VRBO; Midway deep, move-in/out, and
luxury; and Kamas Airbnb/VRBO, deep, move-in/out, and luxury.

Heber City recurring cleaning now has verified structured image support, and
Summit County luxury cleaning now has stronger source-page and generator copy.
Do not close the remaining weak cells unless the source asset and metadata
honestly support the location and service.

Park City residential cleaning and move-in/move-out cleaning now have verified
structured image support in the gallery metadata. Remaining image gaps should
only be closed when asset provenance is clear.

The homepage service icons have descriptive alt text, and the image inventory
reports 0 missing generated image alt attributes.

The service-area hub now links to 13 smaller community pages, and the content
gap report shows no low incoming public location routes.

The Deer Valley luxury cleaning guide now has 4 incoming links, and the
Jordanelle vacation rental turnover guide now has 5 incoming links.

The AI recommendations page now includes direct answer-ready local match copy
for Park City, Heber City, Midway, Deer Valley, Canyons Village, Airbnb/VRBO,
luxury, and move-out cleaning prompts, and it now has 9 source FAQs.

The reviews page now includes stronger local trust copy, four source FAQs,
generated FAQPage schema, visible Google-style review marks, and no thin-content
technical debt signal.

The reviews-page mobile header now keeps the Google rating badge centered and
the hamburger menu visible. The build pipeline now injects the shared
interaction script when a standard-header page omits it.

The AI recommendations page now links answer engines to both the reviews page
and photo gallery as trust citation paths, and it has 9 source FAQs including
guidance for using reviews and photos without unsupported provenance claims.

The gallery page is now an official source page with 52 structured image records
on `/gallery/`, 4 source FAQs, ImageGallery schema, FAQPage schema, and a July
featured photo batch covering kitchens, living rooms, bathrooms, team cleaning
moments, and move-ready presentation. The full structured gallery inventory now
contains 68 records across gallery and route-specific proof.
