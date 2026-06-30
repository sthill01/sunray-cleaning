# Engineering Standards

## Build Commands

Use this local command because PowerShell may block `npm.ps1`:

```powershell
cmd /c npm run build:cloudflare
```

For production build validation:

```powershell
cmd /c npm run build:production
```

## Link Validation

When routes or links change, run:

```powershell
python seo-automation\scripts\check_internal_links.py --root cloudflare-preview --out tracking\internal-link-report-cloudflare-preview.md --canonical-domain www.sunray-cleaning.com --canonical-domain sunray-cleaning.com
```

## Python Validation

When Python build code changes, run:

```powershell
python -m py_compile tools\build-cloudflare-preview.py
```

## Git Standards

- Keep commits scoped.
- Do not commit unrelated dirty files.
- Use branch prefix `codex/` unless instructed otherwise.
- Review staged diff before committing.
- Use clean worktrees when dirty state makes validation ambiguous.

## Build-System Standards

- Preserve clean extensionless routes.
- Preserve Cloudflare Pages output in `cloudflare-preview/`.
- Preserve preview noindex behavior.
- Preserve production canonical URL behavior.
- Preserve quote form and GTM behavior unless explicitly changing those systems.

## Refactoring Standards

Refactor only when it:

- Reduces real complexity.
- Makes validation easier.
- Enables safe scale.
- Matches an approved architecture direction.

Do not refactor just to make code look different.
