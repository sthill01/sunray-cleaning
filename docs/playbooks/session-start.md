# Session Start Playbook

## Purpose

Every Codex session should start from the repository operating system, not from memory alone.

## Required Reading

Read:

1. `docs/README.md`
2. `docs/INITIALIZATION_PROTOCOL.md`
3. `docs/NEXT_ACTION.md`
4. `docs/PROJECT_STATE.md`
5. `docs/BLOCKERS.md`
6. `docs/CONSTITUTION.md`
7. `docs/ROADMAP.md`
8. `docs/ARCHITECTURE.md`

Then read the relevant standards for the work type.

## Orientation Steps

1. Check current branch.
2. Check dirty state.
3. Identify unrelated work that must not be staged.
4. Confirm whether `NEXT_ACTION.md` is still the highest-ROI action.
5. Inspect the relevant source files and docs.
6. Select a scoped implementation path.
7. Capture new blockers, ideas, technical debt, and opportunities in `docs/`.
8. Validate after changes.
9. Commit scoped work.
10. Update `PROJECT_STATE.md` and `NEXT_ACTION.md`.

## Initialization Rule

Before a major new feature or architecture change, follow `docs/INITIALIZATION_PROTOCOL.md`.

The full Phase 0 repository intelligence audit has been completed for the current architecture. Future sessions should run the startup check and only repeat the full audit if the repository architecture, hosting model, build pipeline, or operating model materially changes.

## When To Ask Steve

Ask only when blocked by:

- Credentials.
- DNS.
- Cloudflare settings.
- API keys.
- Payments.
- Legal decisions.
- Business strategy choices.
- Sensitive customer-facing claims.
