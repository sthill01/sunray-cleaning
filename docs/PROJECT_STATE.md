# Project State

Last Updated: 2026-06-30

This file is SRAAP's live project memory. Update it at the end of every sprint and whenever the operating reality changes.

## Current Version

SRAAP Version 2.1 - Operational Readiness cockpit.

## Current Branch

`codex/sraap-constitution-v2`

## Current Sprint

Phase 1 - Route and Content Inventory Automation, planned next.

## Current Objective

Build the route and content inventory automation report described in `NEXT_ACTION.md`.

## Completed Features

- AI Authority Sprint 1 page and build integration for `/ai-cleaning-recommendations/`.
- Program Alpha governance handbook.
- Constitution Version 2 expanded operating manual.
- Phase 0 flat docs cockpit.

## Open Bugs

- No confirmed production bug is currently recorded in this file.
- Build, link, schema, metadata, and route health should be measured again after the next production-affecting code change.

## Known Technical Debt

- `tools/build-cloudflare-preview.py` is a high-complexity protected surface.
- Route, metadata, schema, sitemap, and `llms.txt` behavior should become easier to audit through structured reports.
- AI visibility is not yet tracked with a durable baseline.
- Content coverage is not yet mapped across service, location, property type, and prompt families.
- Pre-existing dirty/untracked blog, Webflow, and SEO automation files exist in the working tree and should not be mixed into governance commits.

## Current Priorities

1. Finish and commit Operational Readiness docs.
2. Build route and content inventory automation.
3. Build schema, metadata, and internal-link coverage reports.
4. Create entity taxonomy.
5. Establish AI monitoring baseline.

## Blocked Items

- No active blocker prevents the Phase 0 docs work.
- Future analytics and external monitoring work may require Google Search Console, GA4, Cloudflare, Google Business Profile, or third-party API credentials.

## Upcoming Work

- Route and content inventory report.
- Schema and metadata coverage report.
- Internal-link opportunity report.
- Entity taxonomy.
- AI monitoring prompt baseline.

## AI Authority Score

Baseline not yet measured.

A future score should include route coverage, schema coverage, `llms.txt` coverage, internal-link strength, content depth, local entity clarity, prompt visibility, and citation presence.

## Entity Status

Core entity direction is defined:

- Brand: Sun Ray Cleaning.
- Region: Wasatch Back.
- Primary locations: Park City, Heber City, Midway, Kamas, Deer Valley, Canyons Village, Summit County, Wasatch County.
- Primary services: recurring cleaning, deep cleaning, move-in and move-out cleaning, vacation rental cleaning, luxury home cleaning.

The entity taxonomy still needs a structured map and coverage audit.

## Coverage

Current coverage includes service pages, location pages, blog guides, and the AI recommendations page. Exact coverage needs to be measured by inventory automation.

## Documentation Health

Operational cockpit is in place. Future sprints should keep the flat files and expanded handbook volumes aligned.

## Repo Safety Notes

There are pre-existing dirty/untracked files outside this docs objective. Do not stage or commit them unless a future sprint explicitly handles that work.
