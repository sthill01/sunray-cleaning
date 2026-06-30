# Project State

Last updated: 2026-06-30

## Current Version

SRAAP v0.2: Operational Readiness plus first production authority improvement.

## Current Sprint

Production Improvement 1: orphan route cleanup.

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

## Open Bugs

- No open bug has been confirmed in this sprint.

## Known Technical Debt

- Large build script mixes routing, SEO, schema, content injection, platform
  file generation, and gallery logic.
- Some source pages still rely on GPT-suffixed source naming and build-time
  cleanup.
- External analytics/search tooling state is not fully documented in the repo.
- Repository Intelligence reports are new and need refinement after first use.

## Current Priorities

1. Verify whether the AI cleaning recommendations page exists in the current
   branch.
2. Improve weak service-location coverage listed in `reports/coverage_matrix.md`.
3. Improve low incoming links for selected blog and minor location pages.
4. Add image-backed coverage for Deer Valley and Canyons Village where assets
   honestly support the location and service.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Verify or implement `/ai-cleaning-recommendations/`.
- Improve image-backed coverage for Deer Valley and Canyons Village service
  pairs.
- Improve low incoming links for Deer Valley luxury cleaning and Jordanelle
  vacation rental articles.

## AI Authority Score

Current Repository Intelligence heuristic: 92.5 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage is the weakest measured category at 54%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 79.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Public orphan routes detected: 0.
- Pages without source FAQs: 3.
- Weak service-location coverage cells: 23.
- Strong service-location matrix coverage: 54%.

## Documentation Health

Initial docs structure created and linked from the root README. Needs ongoing
updates after every sprint.

## Sprint Review

1. Greatest value delivered: the repo now has a durable operating manual,
   project memory, and data-driven reports.
2. Unnecessary complexity found: coverage scoring can overstate authority if it
   treats broad mentions as strong support; the first version now marks weak
   cells separately.
3. Automation to add next: use report findings to update internal links and then
   consider a CI report check once noise is lower.
4. Documentation now out of date: no known docs are out of date after this
   sprint, but analytics/account state still needs confirmation.
5. Highest-impact next task: verify and implement the AI cleaning
   recommendations page if it is still absent, then use coverage reports to
   target weak Deer Valley and Canyons Village authority.
