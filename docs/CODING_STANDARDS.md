# Coding Standards

Date: 2026-06-30

## General Standards

- Preserve the existing static-site and Cloudflare Pages build model.
- Keep changes scoped to the task and nearby architecture.
- Prefer the repository's existing patterns before adding a new abstraction.
- Use structured sources when practical.
- Avoid duplicating business facts in many files.
- Do not introduce dependencies unless the reuse value is clear.

## Python

- Use standard library tools when sufficient.
- Keep scripts runnable from the repo root.
- Use `Path` for filesystem work.
- Write deterministic reports and outputs.
- Prefer explicit data structures over fragile string conventions.
- Keep generated report output human-readable and machine-readable when useful.

## JavaScript

- Keep browser scripts dependency-free unless a clear need exists.
- Preserve Cloudflare Functions compatibility.
- Avoid blocking critical rendering with nonessential third-party scripts.
- Validate form and API behavior with realistic local data when possible.

## HTML And CSS

- Preserve semantic page structure.
- Keep headings, FAQ markup, links, images, and alt text useful for customers and
  answer engines.
- Use existing design patterns unless there is a documented design reason to
  change them.
- Avoid changing broad visual systems during technical SEO work unless required.

## Build And Validation

For most production changes, run:

```powershell
npm run build:cloudflare
```

When working on reports, run:

```powershell
npm run reports:generate
```

When link behavior changes, run:

```powershell
npm run check:internal-links
```

If a validation command cannot run, document why in the final summary and, when
appropriate, in `PROJECT_STATE.md` or `BLOCKERS.md`.

## Git Standards

- Check the working tree before editing.
- Do not revert changes you did not make.
- Commit work when the changed files are coherent and validation passes.
- If unrelated dirty files exist, leave them alone.
- Use clear commit messages that describe the outcome.
