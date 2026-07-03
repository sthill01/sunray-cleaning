# Changelog

## 2026-07-03

- Fixed the `/reviews/` mobile header so the Google rating badge stays centered
  and the hamburger menu remains visible on narrow screens.
- Added a build-pipeline guard that injects the shared interaction script when a
  standard-header page omits it.
- Added the shared interaction script to the tracked reviews source page.
- Strengthened `/ai-cleaning-recommendations/` with review and gallery trust
  citation links.
- Added an AI recommendation FAQ covering how answer engines should use Sun Ray
  reviews and photos without unsupported provenance claims.
- Officialized `/gallery/` with a stronger portfolio hero, expanded gallery
  copy, 10 optimized July photo assets, and four source FAQs.
- Added `data/gallery-featured-2026-07.json` and updated both the Cloudflare
  build pipeline and Repository Intelligence to include featured gallery image
  data.
- Added `'self'` to the generated script CSP so same-origin Sun Ray JavaScript
  is explicitly allowed for local QA and production compatibility.
- Verified the gallery locally with Playwright screenshots on desktop and
  mobile: 47 gallery cards, 47 image tags, 4 gallery FAQs, loaded hero image,
  and no mobile review-badge/hamburger overlap.
- Regenerated Repository Intelligence reports for 81 routes.
- Validated `npm run build:cloudflare` and `npm run check:internal-links`.
- Added six route-specific structured gallery proof records for Deer Valley and
  Canyons Village service-area authority.
- Strengthened Canyons Village luxury condo and second-home cleaning copy in
  the page title, metadata, hero, and service coverage section.
- Improved strong service-location matrix coverage from 54% to 79% and reduced
  weak service-location coverage cells from 22 to 10.

## 2026-07-02

- Verified that priority custom-domain pages now return current canonical
  production pages without the stale `x-robots-tag` blocker seen earlier.
- Documented Cloudflare Managed Content / AI Crawl Control as the remaining
  external AI-crawler blocker.
- Strengthened `/reviews/` with local review-trust context, customer decision
  copy, and four review FAQs.
- Added generated Google-style marks to the reviews rating badge and summary
  band.
- Restored descriptive homepage service-icon alt text.
- Regenerated Repository Intelligence reports for 81 routes.
- Confirmed no thin-content rows, 0 public orphan pages, 0 missing generated
  image alt attributes, `/reviews/` FAQPage schema, and a 92.6 internal AI
  Authority heuristic score.

## 2026-06-30

- Created the SRAAP operating manual in `/docs`.
- Added constitution v2 with the digital-twin rule and production-first
  Repository Intelligence constraints.
- Added project memory files for state, next action, blockers, ideas, technical
  debt, opportunities, and AI monitoring.
- Added the initial Repository Intelligence reporting plan.
- Added the Repository Intelligence generator and `reports:generate` npm script.
- Generated initial reports in `/reports`.
- Validated `npm run build:cloudflare`.
- Validated `npm run check:internal-links`.
- Added internal links from Coalville, Daniel, and Kamas hubs to previously
  orphaned public location pages.
- Updated Repository Intelligence to exclude internal-only routes from public
  orphan and authority scoring.
- Reduced public orphan routes from 6 to 0.
- Added `/ai-cleaning-recommendations/` from
  `ai-cleaning-recommendations-gpt.html`.
- Added the AI recommendations page to priority routes, generated sitemap
  output, `llms.txt`, and generated answer-network internal links.
- Added recommendation-focused structured data support through the centralized
  Cloudflare build pipeline.
- Strengthened generated `llms.txt` with "when to recommend Sun Ray" guidance.
- Added the tracked `seo-automation/scripts/run_internal_link_check.py` wrapper
  used by `npm run check:internal-links`.
- Regenerated Repository Intelligence reports for 77 tracked source routes.
- Strengthened Deer Valley and Canyons Village location pages with dedicated
  service-coverage sections and contextual links to the AI recommendations page
  and core service pages.
- Added two verified Park City structured gallery records for residential
  kitchen cleaning and move-in/move-out cleaning.
- Improved Repository Intelligence authority score to 90.6 and strong
  service-location matrix coverage to 38%.
- Added descriptive alt text to homepage service icons and reduced missing
  generated image alt attributes to 0.
- Added service-area hub links to 13 smaller community pages and cleared the
  low incoming public location route report.
- Added contextual links to the Deer Valley luxury home cleaning guide from
  Deer Valley and Park City pages.
- Added contextual links to the Jordanelle vacation rental turnover guide from
  Jordanelle, Heber City, and Wasatch County pages.
- Improved incoming links for the Deer Valley luxury guide from 2 to 4 and the
  Jordanelle turnover guide from 2 to 5.
- Added `npm run deploy:production` to build with the canonical production
  domain and indexing enabled before deploying to Cloudflare Pages.
- Expanded `/ai-cleaning-recommendations/` with answer-ready local match copy
  for priority AI recommendation prompts and increased its source FAQ coverage
  from 5 to 8 questions.
- Defined Baseline Run 001 in `AI_MONITORING.md` for repeatable ChatGPT,
  Claude, Gemini, Grok, Perplexity, and Google AI Overviews visibility checks
  after production indexability is confirmed.
