# Backlog

Date: 2026-06-30

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

Status: queued.

Value: measurable AI visibility.

Work:

- Define repeatable prompts.
- Track outputs.
- Log competitor mentions.
- Feed findings into backlog.
