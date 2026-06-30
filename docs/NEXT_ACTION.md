# Next Action

Last Updated: 2026-06-30

This file tells the next Codex session what to do first.

## Highest-ROI Next Action

Use the first Repository Intelligence reports to choose the next production website improvement.

Start by running the initialization check in `docs/INITIALIZATION_PROTOCOL.md`, then proceed if this next action is still valid.

## Why This Is Next

Route inventory is the foundation for nearly every SRAAP improvement:

- Sitemap coverage.
- `llms.txt` coverage.
- Metadata coverage.
- Schema coverage.
- Internal-link coverage.
- Orphan page detection.
- Content gap detection.
- AI prompt-to-page mapping.
- Local entity coverage.

Without this inventory, future work depends too much on manual inspection.

The new guardrail is that reporting must translate into website quality. The next cycle should start with `reports/` and select a production improvement from the highest-value gap.

## Suggested Implementation

Run:

```powershell
cmd /c npm run reports:intelligence
```

Then inspect:

- `reports/README.md`
- `reports/content_gap_report.md`
- `reports/authority_report.md`
- `reports/internal_links.md`
- `reports/technical_debt.md`

Choose one production improvement that advances website quality or AI authority before expanding internal tooling.

## Acceptance Criteria

- One production improvement is selected from report findings.
- Findings are summarized in `PROJECT_STATE.md`, `BACKLOG.md`, `TECH_DEBT.md`, and `OPPORTUNITIES.md` as needed.
- Relevant validation runs successfully.

## Stop Conditions

Ask Steve only if the work requires credentials, external accounts, or a business decision not documented in the repo.

## After This Action

Use the inventory to prioritize schema coverage, internal links, metadata gaps, and AI citation-page improvements.
