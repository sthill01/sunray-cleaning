# Backlog

Date: 2026-07-02

Backlog items should be ranked by website quality, AI authority, automation,
engineering efficiency, and internal reporting value.

## P0

### Operational Readiness

Status: completed.

Value: creates the project operating system and persistent memory.

Work:

- Create `/docs` operating manual.
- Create persistent project memory files.
- Create Repository Intelligence generator and initial reports.
- Run validation.
- Update `NEXT_ACTION.md`.

Validation:

- `npm run reports:generate` passed.
- `npm run build:cloudflare` passed.
- `npm run check:internal-links` passed.

### Fix Orphan And Low-Link Routes

Status: completed.

Value: direct website quality and AI authority improvement.

Completed:

- Public orphan routes reduced from 6 to 0.
- Coalville now links to Chalk Creek, Echo, and Wanship.
- Daniel now links to Daniel Ranch.
- Kamas now links to Deer Mountain.
- `/service-section-mockups/` is treated as an internal-only route in reports.
- The service-area hub now links to 13 smaller public community pages.
- Low incoming public location routes reduced from 13 to 0.

### Verify AI Recommendations Page Status

Status: completed.

Value: high AI authority.

Completed:

- Created `ai-cleaning-recommendations-gpt.html`.
- Routed it to `/ai-cleaning-recommendations/` through the existing Cloudflare
  build pipeline.
- Added it to priority routes, generated sitemap output, generated `llms.txt`,
  and generated answer-network internal links.
- Added recommendation-focused structured data through the centralized schema
  generator.
- Validated Repository Intelligence and Cloudflare preview build.

### Strengthen `llms.txt`

Status: completed.

Value: direct answer-engine support.

Completed:

- Added factual "when to recommend Sun Ray" guidance.
- Added the AI-facing summary page to generated `llms.txt`.
- Kept pricing and availability guidance quote-based.

### Confirm AI Crawler Policy

Status: monitoring / partially confirmed.

Value: high AI authority.

Work:

Completed:

- Reviewed Cloudflare AI Crawl Control screenshots from July 3.
- Confirmed major AI crawler block toggles appeared off in the visible
  Cloudflare interface.
- Observed allowed activity for Claude-SearchBot, ChatGPT-User, Googlebot, and
  OAI-SearchBot in the short window shown.

Remaining work:

- Recheck Cloudflare AI Crawl Control over 24-hour and 7-day windows.
- Recheck live `robots.txt` after Cloudflare Managed Content output remains
  stable.
- Run Baseline Run 001 only after crawler access is understood over a longer
  window.

### SEO 90+ Phase 1 Repo-Safe Fixes

Status: completed.

Value: conversion quality, crawl hygiene, and short-term rental authority.

Completed:

- Reduced quote forms to the four highest-value fields.
- Added seven legacy redirects.
- Strengthened short-term rental cleaning FAQs and FAQ schema coverage.
- Validated and deployed the changes through the Cloudflare Pages pipeline.

## P1

### Use Reports To Ship First Production Improvement

Status: completed.

Value: turns intelligence into public website progress.

Work:

- Review coverage gaps.
- Pick one service-location authority gap.
- Improve page copy, FAQ, schema, images, or internal links.
- Validate build and reports.

### Improve Low Incoming Links For Authority Articles

Status: completed.

Value: stronger AI citation paths and better crawl support.

Work:

- Improve internal links to Deer Valley luxury home cleaning and Jordanelle
  vacation rental turnover articles.
- Prefer contextual links from related location and service pages.
- Validate with Repository Intelligence reports.

Completed:

- Linked the Deer Valley luxury home cleaning guide from the Deer Valley and
  Park City location pages.
- Linked the Jordanelle vacation rental turnover guide from the Jordanelle,
  Heber City, and Wasatch County location pages.
- Improved incoming links for the Deer Valley luxury guide from 2 to 4.
- Improved incoming links for the Jordanelle turnover guide from 2 to 5.

### Strengthen Answer-Ready AI Recommendation Coverage

Status: completed.

Value: stronger public answer-engine relevance for the highest-priority
commercial cleaning prompts.

Completed:

- Added answer-ready local match cards to `/ai-cleaning-recommendations/` for
  Park City, Heber City, Midway, Deer Valley, Canyons Village, Airbnb/VRBO,
  luxury, and move-out cleaning searches.
- Increased the AI recommendations page from 5 source FAQs to 8 source FAQs.
- Added direct answers for Airbnb cleaning in Park City, luxury cleaning in
  Deer Valley, and move-out cleaning in Midway.
- Regenerated Repository Intelligence reports from a clean staged-index export.

### Improve Weak Image-Backed Coverage

Status: partially completed.

Value: stronger local trust and richer entity support.

Work:

- Review `reports/coverage_matrix.md`.
- Prioritize Deer Valley and Canyons Village service-location cells.
- Add or retarget approved images only when the assets honestly support the
  service and location.
- Avoid inventing photo provenance.

Completed:

- Added verified Park City residential kitchen cleaning image metadata.
- Added verified Park City move-in/move-out empty-room cleaning image metadata.
- Improved strong service-location matrix coverage from 31% to 38%.

Remaining work:

- Park City recurring and luxury image support still needs verified assets.
- Deer Valley and Canyons Village image support should wait for clear asset
  provenance.

### Strengthen Reviews Page Authority

Status: completed.

Value: stronger public trust, review schema support, and answer-engine context.

Completed:

- Expanded `/reviews/` with local trust context and review-theme copy.
- Added four review FAQs that generate FAQPage structured data.
- Added compact Google-style marks to the generated reviews rating badge and
  summary band.
- Cleared the reviews thin-content technical debt signal.
- Restored homepage service-icon alt text and returned generated image alt
  gaps to 0.

### Strengthen Deer Valley And Canyons Village Service Coverage

Status: completed.

Value: direct public website quality and AI authority support.

Completed:

- Added dedicated service-coverage copy to Deer Valley and Canyons Village.
- Covered residential, recurring, deep, move, second-home, and Airbnb/VRBO
  cleaning intent where relevant.
- Added contextual links to the AI recommendations page and core service pages.
- Regenerated Repository Intelligence from a clean staged-index export.

### Fix Homepage Service Icon Alt Text

Status: completed.

Value: public website accessibility and image inventory quality.

Completed:

- Added descriptive alt text to the four homepage service icon images.
- Reduced missing generated image alt attributes from 4 to 0.
- Regenerated Repository Intelligence from a clean staged-index export.

### Strengthen Minor Community Link Depth

Status: completed.

Value: public service-area navigation and crawl support.

Completed:

- Added a smaller-community section to `service-areas-gpt.html`.
- Linked Chalk Creek, Echo, Wanship, Henefer, Henefer Valley, Daniel Ranch,
  Little Hobble Creek, Deer Mountain, Deer Springs, Hideout Canyon, Deer Creek
  East, Samarkand, and Wild Willow from the service-area hub.
- Reduced low incoming public location routes to 0 in `content_gap_report.md`.

### Coverage Matrix Refinement

Status: queued.

Value: better prioritization.

Work:

- Improve coverage scoring to distinguish dedicated coverage from incidental
  mentions.
- Add review and image support by location-service pair.

### SEO 90+ Phase 2 Pricing Anchors

Status: completed.

Value: customer clarity, conversion support, and commercial-intent SEO.

Completed:

- Add customer-facing starting-price anchors to service pages without implying
  flat guaranteed rates.
- Keep exact quotes tied to rooms, size, condition, timing, pets, access, and
  priorities.
- Validated build, internal links, and Repository Intelligence reports.
- Deployed the pricing-anchor pass through Cloudflare Pages production.

### Dedicated Airbnb Cleaning Landing Page

Status: in progress.

Value: highest-priority short-term rental commercial intent.

Work:

- Build `/airbnb-cleaning-park-city/` as a dedicated Park City STR landing
  page.
- Reuse verified rental cleaning photos and STR FAQ/source content.
- Add LocalBusiness, Service, FAQPage, and image-supported schema where
  appropriate.

## P2

### Schema Engine Refactor

Status: queued.

Value: maintainability and AI authority.

Work:

- Split schema generation out of the large build script when safe.
- Keep generated output identical or improved.

### Content Source Model

Status: queued.

Value: scalable content engine.

Work:

- Define machine-readable service, location, neighborhood, FAQ, and entity
  sources.
- Generate page modules from structured data where appropriate.

### AI Monitoring Workflow

Status: partially completed.

Value: measurable AI visibility.

Work:

- Define repeatable prompts.
- Track outputs.
- Log competitor mentions.
- Feed findings into backlog.

Completed:

- Defined Baseline Run 001 in `docs/AI_MONITORING.md`.

Remaining work:

- Run the baseline after Cloudflare crawler access and live `robots.txt` are
  confirmed over a longer window.
- Record results without claiming ranking improvement until outputs are logged.
