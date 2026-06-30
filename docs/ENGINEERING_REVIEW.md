# Engineering Review

Last Updated: 2026-06-30

This file stores the latest end-of-sprint engineering review. Update it at every sprint close.

## Current Review: Repository Intelligence Layer

### 1. What delivered the most value?

The most valuable delivery is the first report baseline paired with a production improvement on the AI recommendations page. The reports now identify concrete production gaps instead of creating reporting for its own sake.

### 2. What caused unnecessary complexity?

The first authority scoring pass was too generous because generated sitewide content inflated prompt support. The generator was calibrated to use source-page title, description, H1, and route for prompt coverage.

### 3. What can be automated before next sprint?

Repository intelligence generation can be automated through `cmd /c npm run reports:intelligence`. Future automation should focus on reducing orphan pages and improving low-confidence prompt families.

### 4. What documentation is now out of date?

The docs now need to stay aligned with the production-first guardrail: use reports to choose website improvements before adding more internal reporting.

### 5. What is the single highest-impact task for the next sprint?

Strengthen Midway move-out cleaning coverage, then rerun repository intelligence to confirm improvement.

## Review Rule

Every sprint must answer these same five questions and update `PROJECT_STATE.md`, `NEXT_ACTION.md`, `BACKLOG.md`, `CHANGELOG.md`, and any affected logs.
