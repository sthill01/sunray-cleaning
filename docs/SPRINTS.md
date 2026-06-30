# Sprints

Date: 2026-06-30

SRAAP uses continuous engineering rather than isolated task prompts. Each sprint
should leave the repository easier to understand and more valuable.

## Current Sprint: Operational Readiness

Objective:

Create the operating environment that allows Codex to work autonomously over
many sessions.

Scope:

- `/docs` operating manual.
- Persistent project memory.
- Repository Intelligence generator.
- Initial generated reports.
- Build validation.
- Next-action handoff.

Exit criteria:

- Documentation exists in the repo.
- Reports can be generated with one command.
- Build still succeeds.
- Project state and next action are updated.

## Sprint Review Questions

At the end of every sprint, answer:

1. What delivered the greatest value?
2. What caused unnecessary complexity?
3. What can be automated before next sprint?
4. What documentation is now out of date?
5. What is the single highest-impact task for the next sprint?

Record the answers in `PROJECT_STATE.md`.

## Future Sprint Cadence

Each future sprint should:

1. Read docs and project state.
2. Generate or inspect Repository Intelligence reports.
3. Pick highest-ROI work using the constitution priority order.
4. Implement.
5. Validate.
6. Update docs, reports, and project state.
7. Commit.
