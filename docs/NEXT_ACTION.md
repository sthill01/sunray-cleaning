# Next Action

Last updated: 2026-06-30

## Immediate Next Step

Ship the first production website improvement using Repository Intelligence
findings.

Recommended next task:

1. Review `reports/orphan_pages.md` and `reports/content_gap_report.md`.
2. Fix the highest-value orphan or low-link pages through internal links, parent
   route membership, or documented retirement.
3. Verify whether `/ai-cleaning-recommendations/` should be implemented next.
4. Run `npm run reports:generate`, `npm run build:cloudflare`, and
   `npm run check:internal-links`.

## Session Startup Protocol

At the start of a future session:

1. Read `docs/CONSTITUTION.md`.
2. Read `docs/PROJECT_STATE.md`.
3. Read this file.
4. Read `docs/BACKLOG.md`.
5. Run or inspect `npm run reports:generate`.
6. Choose the highest-ROI production action unless blocked.

## Current Candidate Production Improvement

Verify and, if needed, implement `/ai-cleaning-recommendations/` because the
current worktree does not show `ai-cleaning-recommendations-gpt.html`.

Also investigate orphan routes listed in `reports/orphan_pages.md`: Chalk
Creek, Daniel Ranch, Deer Mountain, Echo, Wanship, and the internal
service-section mockup route.
