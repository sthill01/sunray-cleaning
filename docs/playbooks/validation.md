# Validation Playbook

## Build

```powershell
cmd /c npm run build:cloudflare
```

## Production Build

Use only when production output behavior is relevant:

```powershell
cmd /c npm run build:production
```

## Internal Links

```powershell
python seo-automation\scripts\check_internal_links.py --root cloudflare-preview --out tracking\internal-link-report-cloudflare-preview.md --canonical-domain www.sunray-cleaning.com --canonical-domain sunray-cleaning.com
```

## Python Syntax

```powershell
python -m py_compile tools\build-cloudflare-preview.py
```

## Diff Review

Before commit:

```powershell
git status --short
git diff --stat
git diff --cached --stat
git diff --cached --check
```

## Clean Worktree Validation

When unrelated dirty files are present, use a temporary worktree from `HEAD` to verify the committed tree.
