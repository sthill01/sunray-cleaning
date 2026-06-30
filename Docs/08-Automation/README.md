# 08 Automation

## Automation Principle

If a task is repeated, rule-based, and risky to do manually, automate it.

If a task requires business judgment, automate the preparation and validation, not the final decision.

## Current Automation Surfaces

- Cloudflare static build.
- Internal link checker.
- Google review import.
- Meta social gallery import.
- Quote form forwarding.
- Google Sheets quote export.
- Content calendar artifacts.

## Automation Candidates

High priority:

- Content inventory report.
- Route coverage report.
- Sitemap vs route map validation.
- Schema validation spot checks.
- `llms.txt` route coverage check.
- Missing internal-link opportunity report.
- Image alt text coverage report.
- Blog card and route dedupe check.
- Location/service coverage matrix.

Medium priority:

- AI authority scorecard.
- Competitor page monitor.
- Local SERP and AI answer tracking.
- Content decay monitor.
- Review count and rating drift monitor.
- Cloudflare production crawlability monitor.

Later:

- Page scaffolding generator.
- Neighborhood page factory.
- FAQ generator with approval queue.
- Schema regression snapshots.
- Dashboard generation from monitoring output.

## Automation Safety Rules

Automation should:

- Report before destructive changes.
- Write logs to predictable folders.
- Avoid committing generated output unless required.
- Support dry-run behavior for risky operations.
- Validate after writing.

Automation should not:

- Publish live changes without explicit approval.
- Invent reviews or proof.
- Rewrite unrelated pages.
- Hide errors.
