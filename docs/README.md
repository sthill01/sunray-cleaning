# Sun Ray AI Authority Platform Docs

These documents are the operating manual for the Sun Ray AI Authority Platform
(SRAAP). Future engineering sessions should read this directory before making
meaningful changes.

## Start Here

Read in this order:

1. `CONSTITUTION.md`
2. `PROJECT_STATE.md`
3. `NEXT_ACTION.md`
4. `ROADMAP.md`
5. `BACKLOG.md`
6. `BLOCKERS.md`
7. The standards document relevant to the work

The repository is the source of truth. Do not rely on conversation history for
project memory.

## Operating Model

Sun Ray is treated as three connected systems:

1. The public website, which customers and AI systems can read.
2. The SRAAP platform, which powers content, schema, linking, images, reviews,
   reporting, and automation.
3. The operating system, which documents decisions, priorities, blockers,
   state, and next actions.

The website remains the product. Internal tooling exists to make the public
website stronger.

## Documentation Map

- `CONSTITUTION.md`: mission, roles, decision rules, autonomy rules.
- `ROADMAP.md`: 90-day engineering plan and longer-term direction.
- `ARCHITECTURE.md`: current repo architecture and build pipeline.
- `CODING_STANDARDS.md`: implementation, validation, and git standards.
- `AI_STANDARDS.md`: answer-engine and entity optimization standards.
- `SEO_STANDARDS.md`: local SEO, metadata, schema, sitemap, and linking rules.
- `CONTENT_STANDARDS.md`: page, article, FAQ, and review standards.
- `AUTOMATION.md`: automation philosophy and report generation.
- `DECISIONS.md`: durable architecture and governance decisions.
- `BACKLOG.md`: prioritized work queue.
- `SPRINTS.md`: sprint history and review cadence.
- `CHANGELOG.md`: project-level changes by date.
- `PROJECT_STATE.md`: current memory snapshot.
- `NEXT_ACTION.md`: what Codex should do at session start.
- `BLOCKERS.md`: external items requiring the Product Owner.
- `IDEAS.md`: captured ideas that are not yet prioritized.
- `TECH_DEBT.md`: known technical debt and refactor candidates.
- `OPPORTUNITIES.md`: authority, content, automation, and growth opportunities.
- `AI_MONITORING.md`: prompt tracking for ChatGPT, Claude, Gemini, Grok,
  Perplexity, and Google AI Overviews.

## Repository Intelligence

Generated intelligence reports live in `/reports`. Run:

```powershell
npm run reports:generate
```

Reports should inform implementation, not replace judgment. If a reporting
sprint does not lead to a public website improvement, it should be treated as
unfinished unless there is a documented reason.
