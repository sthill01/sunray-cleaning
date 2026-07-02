# Project State

Last updated: 2026-07-02

## Current Version

SRAAP v0.4: Operational Readiness, AI recommendations foundation, and review authority trust layer.

## Current Sprint

Production Improvement 9: review authority and trust-signal strengthening.

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
- Added contextual links from Deer Valley and Park City pages to the Deer
  Valley luxury home cleaning guide.
- Added contextual links from Jordanelle, Heber City, and Wasatch County pages
  to the Jordanelle vacation rental turnover guide.
- Improved incoming links for the Deer Valley luxury guide from 2 to 4 and the
  Jordanelle turnover guide from 2 to 5.
- Added `npm run deploy:production` so production deploys build with the
  canonical domain and indexing enabled before Wrangler uploads.
- Expanded the public AI recommendations page with answer-ready local matches
  for Park City, Heber City, Midway, Deer Valley, Canyons Village, Airbnb/VRBO,
  luxury, and move-out cleaning searches.
- Added three new AI recommendation FAQs that flow into generated FAQPage
  structured data.
- Defined Baseline Run 001 in `AI_MONITORING.md` so future AI visibility checks
  have a repeatable prompt set and capture format.
- Verified the custom domain is serving current production pages with canonical
  `www.sunray-cleaning.com` URLs and no stale `x-robots-tag` header on priority
  checks.
- Strengthened `/reviews/` with additional local trust context, review-theme
  copy, and four customer-facing review FAQs.
- Added generated Google-style review marks to the reviews rating badge and
  summary band while keeping the Trustindex verification language compact.
- Restored descriptive homepage service-icon alt text so the generated image
  inventory reports 0 missing alt attributes.
- Regenerated Repository Intelligence reports for 81 routes.

## Open Bugs

- Cloudflare Managed Content in `robots.txt` still disallows several AI
  crawlers including GPTBot, ClaudeBot, Google-Extended, CCBot, Bytespider, and
  Applebot-Extended. See `BLOCKERS.md`.

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

1. Resolve the Cloudflare Managed Content AI-crawler policy if the business
   wants major AI crawlers to access the site.
2. Run Baseline Run 001 from `AI_MONITORING.md` after the crawler policy is
   confirmed or intentionally left restricted.
3. Keep production deploys on `npm run build:production` /
   `npm run deploy:production`.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Improve image-backed coverage for priority service-location pairs with
  verified assets and structured gallery metadata.
- Run and record the first repeatable AI monitoring baseline after AI-crawler
  policy is confirmed.
- Review verified asset provenance for the next image-backed coverage pass.

## AI Authority Score

Current Repository Intelligence heuristic: 92.6 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage remains the weakest measured category at 54%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 81.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Public orphan routes detected: 0.
- Pages without source FAQs: 3.
- Low incoming public location routes: 2 legal/support pages.
- Structured gallery records: 47.
- Missing generated image alt attributes: 0.
- Weak service-location coverage cells: 22.
- Strong service-location matrix coverage: 54%.
- Deer Valley luxury guide incoming links: 4.
- Jordanelle turnover guide incoming links: 5.
- AI recommendations page source FAQs: 8.
- AI recommendations page raw source words: 1,352.
- Reviews page source FAQs: 4.

## Documentation Health

Initial docs structure created and linked from the root README. Needs ongoing
updates after every sprint.

## Sprint Review

1. Greatest value delivered: the reviews page now works as a stronger trust
   and answer-engine asset with richer local context, customer review FAQs,
   generated FAQ schema, visible Google-style review marks, and no thin-content
   technical debt signal.
2. Unnecessary complexity found: the build pipeline already centralizes review
   data and schema well enough; the immediate win was improving the source page
   and generated presentation rather than creating a separate review subsystem.
3. Automation to add next: make the Google Business Profile review import
   refreshable once API credentials or an approved export workflow exists.
4. Documentation now out of date: analytics/account state and Cloudflare
   AI-crawler policy still need external confirmation.
5. Highest-impact next task: decide whether to allow major AI crawlers in
   Cloudflare Managed Content, then run Baseline Run 001 or continue verified
   image-backed coverage for priority location-service pairs.
