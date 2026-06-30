# Sprints

Version: 2.1

Last Updated: 2026-06-30

SRAAP should be managed as an autonomous engineering program, not isolated prompts.

## Sprint Loop

Every sprint should follow:

1. Initialize using `docs/INITIALIZATION_PROTOCOL.md`.
2. Audit.
3. Prioritize.
4. Implement.
5. Validate.
6. Commit.
7. Document.
8. Plan next.

## Next Sprint

Name: Phase 1 - Repository Intelligence Layer

Goal: Build the first repository intelligence reports so future schema, metadata, internal-link, sitemap, `llms.txt`, content, and AI authority audits can be data-driven while also shipping a production website improvement.

Definition of done:

- Inventory script or equivalent repeatable workflow exists.
- Report captures route, source file, page family, title, description, canonical, sitemap status, `llms.txt` status, JSON-LD types, heading, internal-link count, and quote/contact path presence where practical.
- Findings update `PROJECT_STATE.md`, `BACKLOG.md`, `TECH_DEBT.md`, and `OPPORTUNITIES.md` as needed.
- At least one production page is improved or one production improvement is made implementation-ready from report findings.
- Relevant validation runs.
- Changes are committed without unrelated dirty files.

## Sprint Close Checklist

- Update `PROJECT_STATE.md`.
- Update `NEXT_ACTION.md`.
- Update `BACKLOG.md`.
- Update `CHANGELOG.md`.
- Add blockers to `BLOCKERS.md`.
- Add discoveries to `IDEAS.md`, `TECH_DEBT.md`, or `OPPORTUNITIES.md`.
- Add AI visibility findings to `AI_MONITORING.md`.
- Run relevant validation.
- Commit scoped work.

## Engineering Review Questions

At the end of every sprint, Codex should answer:

1. What delivered the most value?
2. What caused unnecessary complexity?
3. What can be automated before next sprint?
4. What documentation is now out of date?
5. What is the single highest-impact task for the next sprint?

The latest review belongs in `ENGINEERING_REVIEW.md`.

## Completed Sprints

### Initialization Protocol Adoption

Outcome: Converted Steve's mandatory initialization protocol from PDF into repo-owned documentation and wired it into the canonical session-start flow.

### Phase 0: Operational Readiness

Outcome: Added the flat `docs/` cockpit, project memory, next action, blockers, ideas, technical debt, opportunities, AI monitoring, changelog, and engineering review loop.

### Sprint 1: AI Authority Foundation

Outcome: Added the AI cleaning recommendations page, route support, sitemap and `llms.txt` coverage, structured data support, internal links, validation, and commit.

### Program Alpha Governance Foundation

Outcome: Added the initial governance handbook, standards, playbooks, roadmap, architecture, and decision records.

### Constitution Version 2

Outcome: Expanded SRAAP from a prompt-like brief into a repo-owned operating manual.
