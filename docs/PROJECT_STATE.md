# Project State

Last updated: 2026-07-03

## Current Version

SRAAP v0.6: Operational Readiness, AI recommendations foundation, review authority, mobile trust navigation, gallery proof, resort-area image authority, and coverage-matrix refinement.

## Current Sprint

Production Improvement 16: Park City Airbnb authority landing page and trust
expansion.

## Executive Status Checkpoint

A July 3 executive project status report rates SRAAP at approximately 30-35%
complete. The report grades the engineering foundation as excellent, Cloudflare
architecture as strong, AI optimization as good, technical SEO as strong,
content authority as moderate, entity authority as moderate, automation as
excellent, Repository Intelligence as emerging, and AI recommendation readiness
as moderate.

The operating thesis for the next sprint is to shift from infrastructure
maturity to undeniable authority. Every sprint should ask whether the work makes
Sun Ray more trusted, more understandable, and easier for customers and AI
systems to recommend.

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
- Fixed the `/reviews/` mobile header so the Google rating badge sits in the
  center slot and the hamburger menu remains visible on narrow screens.
- Added a build-pipeline guard that injects the shared interaction script on
  standard-header pages that are missing it, preventing source-page omissions
  from disabling mobile navigation.
- Added the shared interaction script to the tracked reviews source page.
- Strengthened `/ai-cleaning-recommendations/` by linking its trust citation
  paths to `/reviews/` and `/gallery/`.
- Added an AI recommendation FAQ explaining how answer engines should use Sun
  Ray reviews and photo proof without overstating unsupported provenance.
- Officialized `/gallery/` as a production source page with a stronger hero,
  real cleaning portfolio copy, and four source FAQs.
- Added 10 optimized July gallery assets covering kitchens, living rooms,
  bathrooms, team-in-action cleaning, stovetop detail work, move-ready spaces,
  and mountain-view home resets.
- Added `data/gallery-featured-2026-07.json` and updated the build pipeline so
  the July image batch appears first in gallery output and ImageGallery schema.
- Updated Repository Intelligence so featured gallery data is included in image
  inventory and coverage reports.
- Added `'self'` to the generated script CSP so same-origin Sun Ray JavaScript
  is explicitly allowed for local QA and production compatibility.
- Verified `/gallery/` locally with Playwright screenshots on desktop and
  mobile: 47 visible gallery cards, 47 image tags, 4 gallery FAQs, loaded hero
  image, and no mobile review-badge/hamburger overlap.
- Added six service-area proof records to structured gallery data for Deer
  Valley and Canyons Village coverage across residential, Airbnb/VRBO, deep
  cleaning, recurring cleaning, move-in/out cleaning, and luxury cleaning
  intent.
- Strengthened the Canyons Village source page title, metadata, hero copy, and
  service coverage copy for luxury condo and second-home cleaning intent.
- Improved strong service-location matrix coverage from 54% to 79% and reduced
  weak service-location coverage cells from 22 to 10.
- Updated verified Heber City recurring-cleaning image metadata in structured
  gallery data so recurring residential cleaning is no longer a weak
  service-location coverage cell.
- Strengthened the Summit County source page and generator template with
  luxury-home cleaning language in the title, metadata, hero, and planning copy.
- Regenerated Repository Intelligence reports for 81 routes.
- Improved strong service-location matrix coverage from 79% to 83% and reduced
  weak service-location coverage cells from 10 to 8.
- Started the `SEO-90-PLUS-ACTION-PLAN.md` Phase 1 repo implementation:
  simplified quote forms, added legacy redirects, strengthened short-term
  rental FAQs, and documented Turno registration as an external blocker.
- Completed the repo-safe Phase 1 SEO 90+ implementation and deployed it:
  simplified quote forms, legacy redirects, STR FAQ schema, and typo checks.
- Added customer-facing starting-price anchor sections to the service hub and
  core service pages for recurring cleaning, deep cleaning, move cleaning, and
  Airbnb/VRBO turnover cleaning.
- Deployed the service pricing-anchor pass to Cloudflare Pages production and
  verified custom-domain priority pages.
- Ingested the July 3 executive status report and moved the program focus from
  infrastructure readiness toward content depth, entity authority, and local
  trust proof.
- Published the Airbnb cleaning cost guide as a stronger human-facing authority
  article and added production `robots.txt` support that allows priority AI and
  search crawlers from the repo-generated Pages artifact.
- Verified the fresh Pages deployment serves the crawler-friendly `robots.txt`,
  but the live custom domain still has Cloudflare Managed Content prepended
  above the repo file with AI-crawler disallow groups. This is now tracked as an
  external Cloudflare setting blocker.

## Open Bugs

- Turno.com listing registration requires Product Owner action because it
  depends on creating or verifying a third-party marketplace profile.
- Cloudflare Managed `robots.txt` must be disabled or updated in AI Crawl
  Control / Bot Management so the custom domain stops prepending AI-crawler
  disallow rules above the repo-generated crawler-friendly file.

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

1. Build and deploy the dedicated `/airbnb-cleaning-park-city/` landing page as
   the next highest-ROI production authority improvement.
2. Continue Phase 2 of `SEO-90-PLUS-ACTION-PLAN.md` with homepage review proof,
   local citations, and third-party entity authority.
3. Clear the Cloudflare Managed `robots.txt` block, then recheck Cloudflare AI
   Crawl Control and live `robots.txt` over 24-hour and 7-day windows before
   running Baseline Run 001 from `AI_MONITORING.md`.
4. Keep production deploys on `npm run build:production` /
   `npm run deploy:production`.

## Blocked Items

See `BLOCKERS.md`.

## Upcoming Work

- Build the dedicated `/airbnb-cleaning-park-city/` landing page.
- Add contextual internal links from the STR service page, Park City location
  page, AI recommendations page, and Park City Airbnb guides.
- Add real Google review proof to the homepage in a compact, trust-building way.
- Run and record the first repeatable AI monitoring baseline after the
  Cloudflare Managed `robots.txt` block is removed and AI-crawler access is
  confirmed over a longer Cloudflare window.
- Review verified asset provenance for the next image-backed coverage pass.

## AI Authority Score

Current Repository Intelligence heuristic: 97.1 / 100.

This is not a ranking claim. It is an internal engineering signal. Strong
service-location matrix coverage remains the weakest measured category at 83%.

## Entity Status

Core entities are documented in `AI_STANDARDS.md`. Coverage will be measured in
`/reports/entity_inventory.md` and `/reports/coverage_matrix.md`.

## Coverage

- Source routes: 81.
- Generated reports: 19.
- Thin source pages under 450 words: 0.
- Public orphan routes detected: 0.
- Pages without source FAQs: 2.
- Low incoming public location routes: 2 legal/support pages.
- Structured gallery records: 68.
- `/gallery/` structured image records: 52.
- Missing generated image alt attributes: 0.
- Weak service-location coverage cells: 8.
- Strong service-location matrix coverage: 83%.
- Deer Valley luxury guide incoming links: 4.
- Jordanelle turnover guide incoming links: 5.
- AI recommendations page source FAQs: 9.
- AI recommendations page raw source words: 1,421.
- Reviews page source FAQs: 4.
- Gallery page source FAQs: 4.

## Documentation Health

Initial docs structure created and linked from the root README. Needs ongoing
updates after every sprint.

## Sprint Review

1. Greatest value delivered: Heber City recurring cleaning and Summit County
   luxury cleaning now have stronger, verified support without inventing
   unsupported location or service provenance.
2. Unnecessary complexity found: the coverage matrix is valuable, but the raw
   JSON shape is less readable than the markdown report, so humans should use
   `coverage_matrix.md` first unless automation needs machine-readable detail.
3. Automation to add next: create a repeatable image-intake script that copies,
   optimizes, captions, checks provenance, and validates approved photo batches
   into gallery data.
4. Documentation now out of date: analytics/account state and third-party
   citation status still need external confirmation.
5. Highest-impact next task: build the dedicated Park City Airbnb cleaning
   landing page, then continue filling verified image-backed coverage gaps.
   for Heber City Airbnb/VRBO, Midway, and Kamas.
