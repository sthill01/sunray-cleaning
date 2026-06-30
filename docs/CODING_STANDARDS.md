# Coding Standards

Version: 2.1

Last Updated: 2026-06-30

This is the daily-read implementation standard. Expanded standards live in `docs/standards/engineering.md`.

## Repository Rules

- Preserve the Cloudflare Pages build pipeline.
- Keep edits scoped to the requested or highest-ROI objective.
- Do not rewrite broad site areas for cosmetic reasons.
- Do not commit unrelated dirty files.
- Prefer existing patterns over new frameworks.
- Prefer structured parsers, generators, and data files over ad hoc string manipulation when practical.
- Keep generated output out of source commits unless the repo explicitly tracks that output.

## Build Rules

- Run `npm run build:cloudflare` for production-affecting changes when practical.
- On Windows, use `cmd /c npm run build:cloudflare` if PowerShell blocks `npm.ps1`.
- Use the existing Python build script instead of replacing the build system.
- Preserve clean extensionless route behavior.
- Keep sitemap, robots, redirects, headers, canonical URLs, and `llms.txt` behavior intact.

## Validation Rules

Select checks based on change scope:

- Docs-only changes: markdown/diff checks are usually sufficient.
- Build-system, route, page, SEO, or content changes: run Cloudflare build.
- Internal-link changes: run the internal-link checker against `cloudflare-preview/`.
- Schema changes: inspect generated JSON-LD for representative pages.
- Metadata changes: inspect representative generated pages and sitemap output.

Preferred internal-link check:

```powershell
python seo-automation\scripts\check_internal_links.py --root cloudflare-preview --out tracking\internal-link-report-cloudflare-preview.md --canonical-domain www.sunray-cleaning.com --canonical-domain sunray-cleaning.com
```

## Git Rules

- Work on a focused branch.
- Stage only files that belong to the current objective.
- Review staged diff before commit.
- Use concise commit messages that describe the outcome.
- Preserve user or generated work that existed before the current task.

## Documentation Rules

- Update `PROJECT_STATE.md` when sprint state changes.
- Update `NEXT_ACTION.md` before ending a sprint.
- Add external blockers to `BLOCKERS.md`.
- Add durable architecture decisions to `DECISIONS.md` and, when needed, an ADR under `docs/decisions/`.
- Add discovered technical debt to `TECH_DEBT.md`.
- Add authority or revenue ideas to `OPPORTUNITIES.md` or `IDEAS.md`.

## Quality Bar

Every implementation should be:

- Buildable.
- Reviewable.
- Reversible through Git.
- Consistent with current architecture.
- Helpful to future Codex sessions.
- Honest about validation gaps.
