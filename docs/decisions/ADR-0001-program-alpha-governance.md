# ADR 0001: Program Alpha Governance Model

Date: 2026-06-30

Status: Accepted

## Context

Sprint 1 proved that Codex can inspect the Sun Ray Cleaning repository, understand the Cloudflare Pages static build, add a new AI authority page, route it, update generated SEO outputs, add schema, validate the build, and commit the result.

The project should no longer operate as a series of narrow file-edit prompts. It should operate as a governed software program with Steve as Chief Product Architect and Codex as Lead Software Engineer.

The governance structure should live in a canonical lowercase `docs/` directory with long-term project memory, standards, playbooks, roadmap, and decision records.

## Decision

Create `docs/` as the permanent SRAAP operating handbook.

Future Codex work should start from this handbook before production changes. The handbook defines the mission, Constitution, standards, architecture, automation approach, roadmap, sprint model, backlog, and decision log.

## Alternatives Considered

- Continue giving Codex individual implementation prompts.
- Keep project governance only in chat.
- Store standards outside the repository.
- Keep the first numbered `Docs/` scaffold.

## Consequences

Positive:

- Future sessions have stable context.
- Codex can make better autonomous decisions.
- Standards are version-controlled.
- Architecture and SEO decisions are auditable.
- The project can evolve like a real engineering organization.

Tradeoffs:

- Docs require upkeep.
- Standards can drift if not enforced.
- The handbook must stay practical, not ceremonial.

## Follow-Up Tasks

- Expand the Constitution into a fuller multi-volume handbook.
- Add templates for page types and automation specs.
- Add CI or script-based validation for core standards where possible.
- Keep decision records current when major implementation choices are made.
