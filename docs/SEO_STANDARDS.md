# SEO Standards

Version: 2.1

Last Updated: 2026-06-30

This is the daily-read SEO and local entity standard. Expanded standards live in `docs/standards/local-seo-entity-authority.md`.

## Objective

Strengthen Sun Ray as the trusted residential cleaning entity for Park City, Heber City, Midway, Kamas, Deer Valley, Canyons Village, Summit County, and Wasatch County.

## Local SEO Principles

- Build pages only when they have real service relevance and useful local content.
- Connect every important service to relevant locations.
- Connect every important location to relevant services.
- Keep business facts consistent across visible content, schema, sitemap output, and `llms.txt`.
- Avoid thin, duplicated, interchangeable local pages.
- Prefer local specificity over generic SEO copy.

## Technical SEO Requirements

Important public pages should have:

- Unique title and meta description.
- Canonical URL.
- Clean extensionless route.
- Appropriate headings.
- Useful internal links.
- Crawlable sitemap entry when public.
- Accurate structured data where relevant.
- Image alt text where images carry meaning.
- Clear quote or contact path.

## Schema Standards

Schema must:

- Match visible page content.
- Use accurate business, service, location, FAQ, article, breadcrumb, and review data.
- Avoid unsupported claims.
- Avoid duplicate or contradictory entities.
- Be spot-checked after generator changes.

## Internal-Link Standards

Internal links should:

- Reinforce service-location relationships.
- Point users to the best next decision page.
- Help AI systems identify canonical citation pages.
- Avoid over-linking repeated boilerplate.
- Use natural anchor text.

## Crawl and Index Standards

- Keep production sitemap URLs on the production canonical domain.
- Keep preview environments noindex unless intentionally changed.
- Validate robots and sitemap behavior after build-system changes.
- Treat sitemap, robots, canonical, and route conflicts as high priority.

## Measurement

Until direct analytics and search-console data are connected, use proxy measures carefully:

- Route coverage.
- Internal-link coverage.
- Schema coverage.
- Metadata coverage.
- AI prompt visibility checks.
- Competitor citation patterns.
- Crawl/indexability spot checks.
