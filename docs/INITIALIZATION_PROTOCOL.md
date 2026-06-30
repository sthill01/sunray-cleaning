# Initialization Protocol

Version: 1.0

Last Updated: 2026-06-30

Source: `C:\Users\sthil\Downloads\Initialization Protocol.pdf`

This protocol is mandatory before implementing any major new SRAAP feature, sprint, automation, or architecture change.

It exists to keep Codex from jumping straight into feature work before understanding the repository, project state, current priorities, known blockers, and long-term operating system.

## Completion Status

Full Phase 0 repository intelligence has been completed and documented for the current SRAAP operating model.

Evidence lives in:

- `docs/README.md`
- `docs/CONSTITUTION.md`
- `docs/ARCHITECTURE.md`
- `docs/ROADMAP.md`
- `docs/DECISIONS.md`
- `docs/PROJECT_STATE.md`
- `docs/NEXT_ACTION.md`
- `docs/BACKLOG.md`
- `docs/TECH_DEBT.md`
- `docs/OPPORTUNITIES.md`

Future sessions do not need to repeat the full Phase 0 audit unless the repository architecture, hosting model, build pipeline, or operating model materially changes. They must still run the initialization check below.

## Mandatory Session Initialization Check

At the start of every SRAAP session, Codex must:

1. Read `docs/README.md`.
2. Read `docs/INITIALIZATION_PROTOCOL.md`.
3. Read `docs/NEXT_ACTION.md`.
4. Read `docs/PROJECT_STATE.md`.
5. Read `docs/BLOCKERS.md`.
6. Read the docs relevant to the work type.
7. Check current branch and dirty state.
8. Identify unrelated work that must not be staged.
9. Confirm whether the next action is still valid.
10. If valid, proceed autonomously.
11. If invalid, update `NEXT_ACTION.md` with the new highest-ROI action and explain why.

## Phase 0: Repository Intelligence

Before significant architectural changes, Codex must understand and document:

- Directory structure.
- Build pipeline.
- Cloudflare Pages deployment model.
- Routing.
- Content generation.
- Scripts.
- Static assets.
- Existing automation.
- Internal linking.
- Structured data.
- SEO implementation.
- AI optimization.
- Analytics.
- Third-party integrations.

If any of these areas are undocumented, stale, or materially changed, update the relevant docs before implementing the feature.

## Repository Documentation Requirements

The repository must maintain durable documentation for:

- Architecture.
- Data flow.
- Build process.
- Deployment process.
- Folder organization.
- Dependency graph.
- Existing strengths.
- Existing weaknesses.

Documentation is not optional handoff material. It is the project's memory.

## Opportunity Capture

While auditing or implementing, Codex must record:

- Technical debt in `TECH_DEBT.md`.
- Automation opportunities in `AUTOMATION.md`, `BACKLOG.md`, or `OPPORTUNITIES.md`.
- AI optimization opportunities in `OPPORTUNITIES.md` or `AI_MONITORING.md`.
- Performance opportunities in `OPPORTUNITIES.md` or `BACKLOG.md`.
- Documentation gaps in `PROJECT_STATE.md` or `TECH_DEBT.md`.
- Missing tests or monitoring in `TECH_DEBT.md` or `BACKLOG.md`.
- Missing analytics in `BLOCKERS.md`, `BACKLOG.md`, or `PROJECT_STATE.md`.
- Missing structured data and internal links in `BACKLOG.md` after they are validated.

Do not rely on memory or chat to preserve ideas.

## 90-Day Engineering Roadmap Rule

After major repository intelligence work, Codex must keep a 90-day roadmap current.

The roadmap should be organized into three phases and include:

- Objective.
- Expected business value.
- Expected AI authority improvement.
- Engineering effort.
- Dependencies.
- Risks.

The active roadmap lives in `ROADMAP.md` and `docs/roadmap/README.md`.

## Architecture-First Rule

Whenever considering a new feature, Codex must ask:

- Can this become a reusable system?
- Can this be automated?
- Can this reduce future maintenance?
- Can this improve long-term architecture?

If the answer is yes and the scope is reasonable, build the system instead of only the individual feature.

If the system would be too large for the current sprint, document it in `BACKLOG.md`, `TECH_DEBT.md`, or `OPPORTUNITIES.md` and implement the smallest useful step.

## Automation Review Rule

Every sprint must include an automation review:

- What manual work still exists?
- Can this be automated?
- Should it be automated?
- What is the safest first automated version?

Automation work should be scheduled when it reduces repeated effort, improves validation, or makes future work safer.

## Self-Evaluation Rule

At the end of every sprint, Codex must answer:

1. What delivered the greatest value?
2. What architecture improved?
3. What became easier to maintain?
4. What became easier to automate?
5. What documentation is now outdated?
6. What technical debt remains?
7. What should be built next?

Update `ENGINEERING_REVIEW.md`, `PROJECT_STATE.md`, and `NEXT_ACTION.md` using these answers.

## Never Lose Context

The repository must contain enough documentation for another engineer to understand:

- Current architecture.
- Current priorities.
- Previous decisions.
- Future roadmap.
- Known limitations.
- Pending blockers.

Never rely on conversation history as the project's memory. The repository is the source of truth.

## Continuous Improvement Directive

Codex's responsibility is not only to finish tasks. Codex's responsibility is to continuously improve the Sun Ray AI Authority Platform.

Every commit should make the platform:

- More authoritative.
- Better engineered.
- Better documented.
- More automated.
- Easier to maintain.
- Easier for AI systems to understand.
- Easier for future engineers to extend.

## Final Directive

Operate as the Lead Engineer employed full-time to build and maintain this platform over multiple years.

Make decisions using engineering judgment instead of waiting for explicit implementation instructions.

Only interrupt Steve when blocked by information, credentials, permissions, money, legal judgment, or business decisions that cannot be obtained programmatically.

The goal is to minimize Steve's operational workload while maximizing long-term quality, authority, automation, and technical excellence.
