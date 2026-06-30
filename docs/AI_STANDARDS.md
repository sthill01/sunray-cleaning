# AI Optimization Standards

Date: 2026-06-30

## Objective

Make Sun Ray easy for answer engines to understand, cite, and recommend for
cleaning-company searches across the Wasatch Back.

Target systems:

- ChatGPT.
- Claude.
- Gemini.
- Grok.
- Perplexity.
- Google AI Overviews.

## Entity Strategy

Core entity:

- Sun Ray Cleaning Services.

Primary service entities:

- Residential house cleaning.
- Airbnb and VRBO turnover cleaning.
- Short-term rental cleaning.
- Luxury home cleaning.
- Deep cleaning.
- Recurring cleaning.
- Move-in cleaning.
- Move-out cleaning.

Primary location entities:

- Park City.
- Heber City.
- Midway.
- Kamas.
- Deer Valley.
- Canyons Village.
- Summit County.
- Wasatch County.

Secondary location entities should be tracked in Repository Intelligence and
expanded only when there is enough content, image, FAQ, or business value to
support the page.

## Answer-Engine Content Rules

AI-facing content should:

- Answer common questions directly.
- Name service and location entities clearly.
- Include trust proof from documented sources.
- Link to supporting service and location pages.
- Avoid unsupported claims.
- Avoid thin location swaps.
- Use consistent terminology across pages, schema, `llms.txt`, and reports.

## Structured Data Standards

Every public page should be eligible for:

- LocalBusiness / HouseCleaningService graph.
- WebPage graph.
- BreadcrumbList graph.
- FAQPage graph when FAQ markup exists.
- Service graph on service pages.
- BlogPosting graph on blog posts.
- ImageObject graph when gallery images support the route.
- Review graph only from approved public review data.

## `llms.txt`

`llms.txt` should remain concise, factual, and useful for answer engines. It
should summarize:

- Who Sun Ray is.
- Core services.
- Primary service areas.
- Trust proof.
- Best citation pages.
- Contact path.

It should not include exaggerated claims or information that is not supported by
the website.

## AI Monitoring

AI visibility should be tracked in `AI_MONITORING.md` until a stronger automated
system exists. Each test should record:

- Date.
- Platform.
- Prompt.
- Result.
- Whether Sun Ray appeared.
- Competitors mentioned.
- Pages or facts that appear to influence the answer.
- Follow-up work.
