# Automation

Date: 2026-06-30

## Objective

Automate repetitive work so Codex can spend more time on high-value production
improvements.

Automation should reduce manual coordination, increase validation, or improve
AI authority. It should not become busywork.

## Current Automation

Package scripts:

- `npm run build:cloudflare`
- `npm run build:production`
- `npm run deploy:preview`
- `npm run deploy:production`
- `npm run import:google-reviews`
- `npm run import:social-gallery`
- `npm run check:internal-links`
- `npm run reports:generate`

Production deploys must use `npm run build:production` before upload so the
generated site uses the canonical `https://www.sunray-cleaning.com` base URL and
allows indexing. `npm run build:cloudflare` is the preview/local build path and
must not be used as the final production artifact.

GitHub workflows:

- Google review import.
- Social gallery import.

Build script:

- Route discovery.
- Link rewriting.
- SEO injection.
- Structured data generation.
- Sitemap generation.
- Robots generation.
- `llms.txt` generation.
- Cloudflare headers and redirects.

## Repository Intelligence

The Repository Intelligence Layer generates reports under `/reports`.

Initial reports include:

- Route inventory.
- Service inventory.
- Neighborhood inventory.
- Internal link inventory.
- Orphan pages.
- Thin content.
- Schema inventory.
- Image inventory.
- Review inventory.
- FAQ inventory.
- Entity inventory.
- Structured data report.
- Build report.
- Automation report.
- Technical debt.
- Content gaps.
- AI authority opportunities.
- Coverage matrix.
- Knowledge graph.

## Automation Review Questions

At the end of every sprint, ask:

1. What manual work still exists?
2. Can it be automated?
3. Should it be automated now?
4. What would the automation change in production?
5. What validation would prove it works?

## Automation Guardrails

- Do not automate a broken process before understanding it.
- Do not add automation that requires fragile credentials unless the value is
  clear.
- Do not generate large content sets without quality standards and validation.
- Prefer small durable scripts over large opaque systems.
