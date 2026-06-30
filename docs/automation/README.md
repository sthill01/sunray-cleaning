# Automation

## Objective

Codex should reduce manual coordination by automating repeated, rule-based work.

## Automation Bias

If something can be safely automated, automate it.

If a task requires business judgment, automate the audit, draft, and validation, then ask for the decision.

## Core Automation Responsibilities

Codex should look for ways to automate:

- Sitemap coverage.
- `llms.txt` coverage.
- Schema coverage.
- Internal link opportunities.
- Orphan page detection.
- Alt text coverage.
- Metadata coverage.
- Content inventory.
- Route inventory.
- Competitor monitoring.
- AI visibility monitoring.
- Sprint planning.
- Documentation updates.

## Safety Rules

Automation must:

- Be inspectable.
- Prefer dry-run behavior for risky changes.
- Report what it changed.
- Validate after writing.
- Avoid credentials in code.
- Avoid publishing live changes without approval when approval is required.

Automation must not:

- Invent facts.
- Hide errors.
- Commit unrelated files.
- Rewrite broad site areas without a clear objective.

## Agent Behavior

Codex should operate like a senior engineer:

1. Inspect current state.
2. Identify highest ROI opportunity.
3. Implement safely.
4. Validate.
5. Commit.
6. Document.
7. Recommend the next cycle.
