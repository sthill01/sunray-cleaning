# SEO Standards

Date: 2026-06-30

## Local SEO Objective

Make Sun Ray the clearest, most trustworthy local result for residential
cleaning services across Park City, Heber City, Midway, Kamas, Summit County,
and Wasatch County.

## Metadata

Public pages should have:

- One clear title.
- One meta description.
- One H1.
- A canonical URL.
- Correct robots behavior for preview vs production.
- Relevant internal links.

## Internal Linking

Internal links should reinforce:

- Service-to-location relationships.
- Location-to-service relationships.
- Blog-to-service relationships.
- Blog-to-location relationships.
- Reviews, gallery, and trust proof.
- Quote conversion paths.

Avoid orphan pages. When a new page is added, update route generation,
navigation or contextual links, sitemap, `llms.txt` when appropriate, and
Repository Intelligence reports.

## Sitemap And Robots

The build system owns generated sitemap and robots output.

Preview builds should remain noindex. Production builds should be crawlable only
when `SUNRAY_ALLOW_INDEXING=1` is explicitly set.

## Image SEO

Images should include:

- Local descriptive alt text.
- Service metadata.
- Location metadata.
- Route targets.
- Captions when visible.
- ImageObject schema when used on public pages.

Use actual Sun Ray cleaning images whenever possible.

## Reviews

Review content must come from approved public sources. The repository should
track:

- Review count.
- Rating value.
- Source.
- Last verified date.
- Approved featured review excerpts.

Do not invent reviews.

## Local Coverage

Coverage should be measured across:

- Location to service.
- Location to FAQ.
- Location to reviews.
- Location to images.
- Location to blog articles.
- Location to schema.
- Service to FAQ.
- Service to images.
- Service to reviews.

Coverage gaps should feed `BACKLOG.md` and `OPPORTUNITIES.md`.
