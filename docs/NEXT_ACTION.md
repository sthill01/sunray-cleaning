# Next Action

Last updated: 2026-06-30

## Immediate Next Step

Fix the missing homepage icon alt attributes, then continue verified
image-backed service-location coverage using Repository Intelligence data.

Recommended next task:

1. Review `reports/image_inventory.md` and fix the four missing homepage icon
   alt attributes if those images are not intentionally decorative.
2. Review `reports/coverage_matrix.md`, `reports/image_inventory.md`, and
   tracked assets.
3. Prioritize Park City, Deer Valley, Canyons Village, and Wasatch County image
   gaps only where the source asset and metadata honestly support the location
   and service.
4. If provenance is unclear, improve customer-facing copy or internal links
   instead of adding unsupported image metadata.
5. Run `npm run reports:generate`, `npm run build:cloudflare`, and
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
