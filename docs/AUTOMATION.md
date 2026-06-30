# Automation

Version: 2.1

Last Updated: 2026-06-30

This is the daily-read automation standard. Expanded automation notes live in `docs/automation/README.md`.

## Objective

Reduce manual coordination by automating repeated, inspectable, rule-based work while preserving factual safety and Cloudflare compatibility.

Automation exists to improve the production website. Reporting and internal tools should not become the primary product.

## Automation Bias

If something can be safely automated, automate it.

If something requires business judgment, automate the audit, draft, and validation, then record the decision needed in `BLOCKERS.md`.

## Priority Automation Targets

- Route inventory.
- Content inventory.
- Sitemap coverage.
- `llms.txt` coverage.
- Schema coverage.
- Metadata coverage.
- Internal-link opportunities.
- Orphan page detection.
- Alt text coverage.
- Image metadata coverage.
- AI prompt monitoring.
- Competitor citation monitoring.
- Sprint planning.
- Documentation state updates.
- Build and link validation.

## Safety Rules

Automation must:

- Be inspectable.
- Prefer dry-run mode for risky changes.
- Report what it changed.
- Validate after writing.
- Avoid credentials in code.
- Avoid publishing live changes without approval when approval is required.
- Avoid rewriting unrelated work.

Automation must not:

- Invent facts.
- Hide errors.
- Commit unrelated files.
- Replace human business judgment.
- Make external account or DNS changes without Steve.

## Agent Behavior

Codex should operate like a senior engineer:

1. Inspect current state.
2. Identify the highest-ROI opportunity.
3. Implement safely.
4. Validate.
5. Commit.
6. Document.
7. Recommend the next cycle.

## Next Automation Build

The next automation milestone should be a route and content inventory report that supports later schema, metadata, link, content, and AI-authority coverage checks.

Every reporting sprint should also produce or directly schedule a production website improvement.
