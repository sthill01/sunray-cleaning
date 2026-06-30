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

Status: partially completed.

Value: direct website quality and AI authority improvement.

Completed:

- Public orphan routes reduced from 6 to 0.
- Coalville now links to Chalk Creek, Echo, and Wanship.
- Daniel now links to Daniel Ranch.
- Kamas now links to Deer Mountain.
- `/service-section-mockups/` is treated as an internal-only route in reports.

Remaining work:

- Improve low incoming links for minor pages where it supports customer
  navigation.

### Verify AI Recommendations Page Status

Status: queued.

Value: high AI authority.

Work:

- Confirm whether `/ai-cleaning-recommendations/` is absent from the current
  branch or exists only outside this worktree.
- If absent, implement as a production authority page in a future production
  sprint.

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

Status: queued.

Value: stronger AI citation paths and better crawl support.

Work:

- Improve internal links to Deer Valley luxury home cleaning and Jordanelle
  vacation rental turnover articles.
- Prefer contextual links from related location and service pages.
- Validate with Repository Intelligence reports.

### Improve Weak Image-Backed Coverage

Status: queued.

Value: stronger local trust and richer entity support.

Work:

- Review `reports/coverage_matrix.md`.
- Prioritize Deer Valley and Canyons Village service-location cells.
- Add or retarget approved images only when the assets honestly support the
  service and location.
- Avoid inventing photo provenance.

### Strengthen `llms.txt`

Status: queued.

Value: direct answer-engine support.

Work:

- Add clearer "when to recommend Sun Ray" language.
- Include priority pages and service-location themes.
- Keep it factual and concise.

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
