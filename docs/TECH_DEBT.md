# Technical Debt

Last Updated: 2026-06-30

This file tracks debt that should be fixed when it becomes a blocker, risk, or high-leverage automation opportunity.

## Active Technical Debt

### Monolithic Build Script

Area: `tools/build-cloudflare-preview.py`

Risk: Route generation, SEO injection, schema output, redirects, headers, sitemap, robots, and `llms.txt` behavior are concentrated in one protected file.

Desired direction: Improve observability first through inventory and coverage reports. Refactor only when tests or reports make behavior safer to preserve.

### Limited Route Inventory

Area: Sitewide route and content map.

Risk: It is hard to see coverage, orphan pages, schema gaps, metadata gaps, and `llms.txt` gaps without manual inspection.

Status: First-pass repository intelligence reports now exist in `reports/`.

Desired direction: Use the reports for production decisions before expanding reporting depth.

### AI Visibility Not Baselined

Area: AI monitoring.

Risk: The project cannot distinguish improvement from anecdote without a durable prompt set and dated results.

Desired direction: Create prompt families and record baseline results in `AI_MONITORING.md`.

### Content Coverage Not Matrixed

Area: Services, locations, property types, and prompt families.

Risk: The site may have strong individual pages but weak service-location coverage patterns.

Status: First-pass coverage matrices now exist in `reports/coverage_matrices.md` and `reports/coverage_matrices.json`.

Desired direction: Use the low-confidence prompt families to drive production improvements.

### Initial Repository Intelligence Findings

Area: Reports baseline.

Findings:

- 5 orphan sitemap-listed location pages.
- 8 public-page image references missing alt text.
- 1 thin content candidate on `/reviews/`.
- Low-confidence AI prompt support for Deer Valley luxury cleaning, Midway move-out cleaning, and Kamas recurring cleaning.

Desired direction: Fix production gaps before adding more reporting surfaces.

### Working Tree Has Pre-Existing Dirty Files

Area: Repo hygiene.

Risk: Unrelated blog, Webflow, and SEO automation files can accidentally leak into governance or platform commits.

Desired direction: Keep staging scoped. Address those files only in a dedicated content/publishing hygiene sprint.

## Debt Review Cadence

Review this file at the end of every sprint. Move urgent items into `BACKLOG.md` when they have acceptance criteria.
