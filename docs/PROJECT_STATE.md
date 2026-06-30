# Project State

Last updated: 2026-06-30

## Current Version

SRAAP v0.3: Operational Readiness plus AI recommendations authority foundation.

## Current Sprint

Production Improvement 3: priority service-location coverage pass.

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

1. Add image-backed coverage for Park City, Deer Valley, and Canyons Village
   where assets honestly support the location and service.
2. Continue improving low incoming links for minor public location pages where
   it supports customer navigation.
3. Improve contextual internal links to high-authority service/location
   resources where reports show weak link depth.
4. Define the first repeatable AI monitoring prompt run in `AI_MONITORING.md`.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Improve image-backed coverage for priority service-location pairs with
  verified assets and structured gallery metadata.
- Continue improving minor service-location pages with only one incoming link.

## AI Authority Score

Current Repository Intelligence heuristic: 89.7 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage is the weakest measured category at 31%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 77.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Public orphan routes detected: 0.
- Pages without source FAQs: 0.
- Weak service-location coverage cells: 33.
- Strong service-location matrix coverage: 31%.

## Documentation Health

Initial docs structure created and linked from the root README. Needs ongoing
updates after every sprint.

## Sprint Review

1. Greatest value delivered: Sun Ray now has a public AI recommendation summary
   page connected to sitemap, `llms.txt`, structured data, and internal links;
   Deer Valley and Canyons Village now also have stronger service-coverage copy
   and contextual service links.
2. Unnecessary complexity found: answer-engine support belongs in the existing
   build pipeline, not a separate static file list; image-backed coverage must
   be handled through clean structured metadata, not incidental page images.
3. Automation to add next: improve coverage scoring around image-backed service
   and location pairs after one more production improvement.
4. Documentation now out of date: analytics/account state still needs external
   confirmation.
5. Highest-impact next task: add verified image-backed service-location support
   without inventing unsupported image provenance.
