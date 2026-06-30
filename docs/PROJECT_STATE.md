# Project State

Last updated: 2026-06-30

## Current Version

SRAAP v0.3: Operational Readiness plus AI recommendations authority foundation.

## Current Sprint

Production Improvement 6: service-area hub link-depth improvement.

## Completed This Sprint

- Created the docs operating manual.
- Created persistent memory files.
- Established Repository Intelligence as an internal capability that must serve
  production website improvements.
- Added `tools/generate-repository-intelligence.py`.
- Added `npm run reports:generate`.
- Generated 19 Repository Intelligence reports for 79 routes.
- Validated `npm run build:cloudflare`.
- Validated `npm run check:internal-links`.
- Added production-facing internal links from Coalville, Daniel, and Kamas hub
  pages to previously orphaned location pages.
- Updated Repository Intelligence to treat `INTERNAL_ONLY_ROUTES` as non-public
  routes in orphan, content gap, authority, and technical debt reporting.
- Reduced public orphan routes from 6 to 0.
- Added `ai-cleaning-recommendations-gpt.html` as the source for
  `/ai-cleaning-recommendations/`.
- Added the AI recommendations page to priority routes, generated sitemap
  output, `llms.txt`, and generated internal answer-network links.
- Added recommendation-focused structured data for the AI recommendations page.
- Strengthened `llms.txt` with factual "when to recommend Sun Ray" guidance.
- Regenerated 19 Repository Intelligence reports for 77 tracked source routes.
- Strengthened the Deer Valley and Canyons Village public pages with dedicated
  service coverage sections for residential, recurring, deep, move,
  Airbnb/VRBO, second-home, and luxury cleaning intent.
- Added direct contextual links from Deer Valley and Canyons Village pages to
  the AI recommendations page and core service pages.
- Added verified Park City structured gallery records for residential kitchen
  cleaning and move-in/move-out empty-room cleaning.
- Improved strong service-location matrix coverage from 31% to 38% and reduced
  weak service-location cells from 33 to 30.
- Added descriptive alt text to the four homepage service icon images so the
  generated image inventory no longer reports missing alt attributes.
- Added a "smaller communities and neighborhood service areas" section to the
  service-area hub linking to 13 low-incoming public location pages.
- Reduced low incoming public location routes from 13 to 0.

## Open Bugs

- No open bug has been confirmed in this sprint.

## Known Technical Debt

- Large build script mixes routing, SEO, schema, content injection, platform
  file generation, and gallery logic.
- Some source pages still rely on GPT-suffixed source naming and build-time
  cleanup.
- External analytics/search tooling state is not fully documented in the repo.
- Repository Intelligence reports are new and need refinement after first use.
- Image-backed coverage depends on structured gallery metadata; future edits
  must avoid unsupported location or service provenance.

## Current Priorities

1. Continue verified image-backed coverage only where assets honestly support
   the location and service.
2. Improve contextual internal links to high-authority service/location
   resources where reports show weak link depth.
3. Define the first repeatable AI monitoring prompt run in `AI_MONITORING.md`.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Improve image-backed coverage for priority service-location pairs with
  verified assets and structured gallery metadata.
- Improve contextual internal links to low-link authority articles.

## AI Authority Score

Current Repository Intelligence heuristic: 90.6 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage is the weakest measured category at 38%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 77.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Public orphan routes detected: 0.
- Pages without source FAQs: 0.
- Low incoming public location routes: 0.
- Structured gallery records: 12.
- Missing generated image alt attributes: 0.
- Weak service-location coverage cells: 30.
- Strong service-location matrix coverage: 38%.

## Documentation Health

Initial docs structure created and linked from the root README. Needs ongoing
updates after every sprint.

## Sprint Review

1. Greatest value delivered: Sun Ray now has a public AI recommendation summary
   page connected to sitemap, `llms.txt`, structured data, and internal links;
   Deer Valley and Canyons Village now also have stronger service-coverage copy
   and contextual service links; Park City residential and move-cleaning
   coverage now has verified structured image support; smaller community pages
   now have service-area hub links.
2. Unnecessary complexity found: answer-engine support belongs in the existing
   build pipeline, not a separate static file list; image-backed coverage must
   be handled through clean structured metadata, not incidental page images.
3. Automation to add next: improve coverage scoring around image-backed service
   and location pairs after one more production improvement.
4. Documentation now out of date: analytics/account state still needs external
   confirmation.
5. Highest-impact next task: improve contextual links to low-link authority
   articles, or continue verified image-backed service-location support where
   asset provenance is clear.
