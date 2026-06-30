# Project State

Last updated: 2026-06-30

## Current Version

SRAAP v0.1: Operational Readiness.

## Current Sprint

Operational Readiness.

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

1. Ship the first production website improvement from Repository Intelligence
   findings.
2. Fix or intentionally retire orphan routes listed in `reports/orphan_pages.md`.
3. Improve weak service-location coverage listed in `reports/coverage_matrix.md`.
4. Verify whether the AI cleaning recommendations page exists in the current
   branch.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Use `reports/content_gap_report.md` to pick the first production improvement.
- Investigate orphan routes: Chalk Creek, Daniel Ranch, Deer Mountain, Echo,
  Wanship, and the internal service-section mockup route.
- Improve image-backed coverage for Deer Valley and Canyons Village service
  pairs.
- Verify or implement `/ai-cleaning-recommendations/`.

## AI Authority Score

Initial Repository Intelligence heuristic: 91.5 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage is the weakest measured category at 56%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 79.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Orphan routes detected: 6.
- Pages without source FAQs: 4.
- Weak service-location coverage cells: 22.
- Strong service-location matrix coverage: 56%.

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
5. Highest-impact next task: ship a production improvement that fixes orphan
   routes or implements the AI cleaning recommendations page.
