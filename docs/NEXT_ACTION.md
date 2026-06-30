# Next Action

Last Updated: 2026-06-30

This file tells the next Codex session what to do first.

## Highest-ROI Next Action

Build a route and content inventory automation report for the current Cloudflare static site.

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

## Suggested Implementation

Create or extend a script that can inspect source files and/or generated `cloudflare-preview/` output and produce a durable report.

The first version should capture:

- Public route.
- Source file.
- Page family.
- Title.
- Meta description.
- Canonical URL.
- Sitemap inclusion.
- `llms.txt` inclusion.
- JSON-LD types found.
- H1 or primary heading.
- Internal link count.
- Quote/contact path presence.
- Notes for missing or weak coverage.

## Acceptance Criteria

- The report runs locally.
- Output is committed in a sensible reporting location or documented if generated reports should stay untracked.
- Findings are summarized in `PROJECT_STATE.md`, `BACKLOG.md`, `TECH_DEBT.md`, and `OPPORTUNITIES.md` as needed.
- Relevant validation runs successfully.

## Stop Conditions

Ask Steve only if the work requires credentials, external accounts, or a business decision not documented in the repo.

## After This Action

Use the inventory to prioritize schema coverage, internal links, metadata gaps, and AI citation-page improvements.
