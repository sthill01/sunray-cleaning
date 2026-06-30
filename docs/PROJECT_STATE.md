# Project State

Last Updated: 2026-06-30

This file is SRAAP's live project memory. Update it at the end of every sprint and whenever the operating reality changes.

## Current Version

SRAAP Version 2.3 - Repository Intelligence Layer in progress.

## Current Branch

`codex/sraap-constitution-v2`

## Current Sprint

Phase 1 - Repository Intelligence Layer and production improvement.

## Current Objective

Build the first Repository Intelligence Layer reports and pair them with a production-facing AI recommendations page improvement.

## Completed Features

- AI Authority Sprint 1 page and build integration for `/ai-cleaning-recommendations/`.
- Program Alpha governance handbook.
- Constitution Version 2 expanded operating manual.
- Phase 0 flat docs cockpit.
- Mandatory Initialization Protocol converted from PDF into repo-owned documentation and verified against the Word source file.
- Continuous Engineering directive accepted: repository intelligence must serve the production website.

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

1. Build route and content inventory automation.
2. Build schema, metadata, and internal-link coverage reports.
3. Create entity taxonomy.
4. Establish AI monitoring baseline.
5. Add documentation-health automation so startup docs stay aligned.

## Blocked Items

- No active blocker prevents the Phase 1 Repository Intelligence work.
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

Operational cockpit is in place, and the mandatory initialization protocol has been added. Future sprints should keep the flat files and expanded handbook volumes aligned.

Repository Intelligence must remain balanced against production website improvements.

## Repo Safety Notes

There are pre-existing dirty/untracked files outside this docs objective. Do not stage or commit them unless a future sprint explicitly handles that work.
