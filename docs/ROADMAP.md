# SRAAP Roadmap

Date: 2026-06-30

This roadmap covers the first 90 days of the autonomous engineering program.
It should be revised at the end of each sprint based on repository intelligence,
business priorities, and production performance.

## Phase 1: Operational Readiness

Objective: create the operating system that lets Codex work across many
sessions without losing context.

Expected business value:

- Lower Product Owner coordination burden.
- Faster future delivery.
- Better continuity across sessions.

Expected AI authority improvement:

- Better documentation of entities, relationships, standards, and coverage.
- Clearer prioritization for future AI-facing content and schema.

Engineering effort: medium.

Dependencies:

- Existing repository access.
- Existing Cloudflare build system.

Risks:

- Spending too long on internal process without production impact.

Deliverables:

- `/docs` operating manual.
- `PROJECT_STATE.md`, `NEXT_ACTION.md`, `BLOCKERS.md`, `IDEAS.md`,
  `TECH_DEBT.md`, `OPPORTUNITIES.md`, and `AI_MONITORING.md`.
- Initial Repository Intelligence reports in `/reports`.
- Backlog and 90-day roadmap.

## Phase 2: Repository Intelligence And Data-Driven Prioritization

Objective: make route, entity, service, location, image, review, FAQ, schema,
and internal-link coverage visible.

Expected business value:

- Faster identification of missing revenue pages and weak authority areas.
- Better prioritization of content and technical improvements.

Expected AI authority improvement:

- Stronger entity coverage.
- Better answer-engine support.
- Fewer orphan or thin pages.

Engineering effort: medium.

Dependencies:

- Phase 1 docs.
- Current route map and build script.
- Data files for reviews and gallery assets.

Risks:

- Over-engineering internal reports before using them for customer-facing
  improvements.

Deliverables:

- Route inventory.
- Schema inventory.
- Internal link inventory.
- Entity inventory.
- Coverage matrices.
- Knowledge graph baseline.
- Authority opportunity report.

## Phase 3: Production Authority Improvements

Objective: use the intelligence layer to ship the highest-return public
website improvements.

Expected business value:

- More qualified quote requests.
- Better local trust.
- Stronger service-location relevance.

Expected AI authority improvement:

- More complete answers for high-value prompts.
- Better local entity disambiguation.
- Stronger service and location relationships.

Engineering effort: medium to high.

Dependencies:

- Repository Intelligence findings.
- Human confirmation for facts that are not documented.

Risks:

- Creating too much thin content.
- Making claims that are not backed by evidence.

Candidate deliverables:

- AI cleaning recommendations page if still absent.
- Deer Valley luxury cleaning hub improvements.
- Park City vacation rental authority cluster.
- Wasatch County and Summit County service coverage expansions.
- FAQ and schema upgrades for service-location pairs.
- `llms.txt` improvements.
- Internal link improvements based on orphan and coverage reports.

## Longer-Term Direction

- Content engine for scalable service, location, neighborhood, FAQ, and guide
  generation.
- Schema engine fed by structured source data.
- Image intelligence and automated alt/caption coverage.
- Review intelligence and public trust proof workflow.
- AI monitoring across ChatGPT, Claude, Gemini, Grok, Perplexity, and Google AI
  Overviews.
- Analytics dashboards for authority, coverage, and conversion health.
