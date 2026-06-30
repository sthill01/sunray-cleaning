# Next Action

Last updated: 2026-06-30

## Immediate Next Step

Verify and, if needed, implement `/ai-cleaning-recommendations/`.

Recommended next task:

1. Confirm whether `ai-cleaning-recommendations-gpt.html` exists in the current
   branch or another branch.
2. If absent, create the page and route it through the Cloudflare build
   pipeline.
3. Add it to priority routes, sitemap output, and `llms.txt` output if it is a
   public AI authority page.
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

Public orphan routes were fixed in the previous production improvement.
