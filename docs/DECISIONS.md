# Decisions

Version: 2.1

Last Updated: 2026-06-30

This file is the operating decision index. Detailed architecture decision records live in `docs/decisions/`.

## Decision Rules

Create or update a decision record when work changes:

- Build architecture.
- Hosting model.
- Routing model.
- Schema strategy.
- Content generation model.
- Automation policy.
- External services.
- Data sources.
- Analytics architecture.
- Deployment process.

Small implementation choices can be summarized here. Long-lived architecture choices should become ADRs.

## Active Decisions

### DEC-0001: SRAAP Is an Autonomous Engineering Program

Status: Accepted

Codex is the Lead Software Engineer for SRAAP and should plan, implement, validate, document, and recommend next work from repository-owned docs rather than waiting for line-by-line prompts.

Reference: `docs/decisions/ADR-0001-program-alpha-governance.md`

### DEC-0002: The Flat Docs Cockpit Is Canonical for Session Start

Status: Accepted

Future Codex sessions start with the flat files in `docs/`, especially `README.md`, `NEXT_ACTION.md`, `PROJECT_STATE.md`, `BLOCKERS.md`, `CONSTITUTION.md`, `ROADMAP.md`, and `ARCHITECTURE.md`. Subdirectories remain expanded volumes and detailed references.

### DEC-0003: Cloudflare Pages Pipeline Remains Protected

Status: Accepted

The existing Cloudflare Pages static build system remains the production architecture. Build-system replacement requires an ADR and validation plan.

### DEC-0004: Documentation Is Project Memory

Status: Accepted

Chat context is temporary. Durable strategy, project state, next actions, blockers, ideas, technical debt, opportunities, AI monitoring, and sprint reviews belong in `docs/`.

### DEC-0005: Initialization Protocol Is Mandatory Before Major Work

Status: Accepted

Codex must run the startup check in `docs/INITIALIZATION_PROTOCOL.md` before major new features, sprints, automation, or architecture changes. Full Phase 0 repository intelligence does not need to be repeated unless architecture, hosting, build, or operating model changes materially.

## Pending Decisions

- Whether to add CI checks for build, link validation, and schema coverage.
- Which analytics sources to connect first once credentials are available.
- Which AI prompt monitoring method should become the standard baseline.
- Whether route metadata should be extracted into a structured data file or modular Python layer first.
