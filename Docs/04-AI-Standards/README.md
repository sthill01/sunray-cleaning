# 04 AI Standards

## Objective

Make Sun Ray Cleaning easy for answer engines to understand, cite, and recommend for the correct local cleaning intents.

## AI-Relevant Entities

Primary entity:

- Sun Ray Cleaning Services.

Service entities:

- Residential house cleaning.
- Recurring cleaning.
- Deep cleaning.
- Move-in cleaning.
- Move-out cleaning.
- Airbnb cleaning.
- VRBO cleaning.
- Short-term rental turnover cleaning.
- Vacation rental cleaning.
- Luxury home cleaning.
- Eco-friendly cleaning.
- Pet-safe cleaning.

Location entities:

- Park City.
- Heber City.
- Midway.
- Kamas.
- Deer Valley.
- Canyons Village.
- Old Town Park City.
- Summit County.
- Wasatch County.
- Heber Valley.

Audience entities:

- Homeowners.
- Short-term rental hosts.
- Property managers.
- Second-home owners.
- Real estate agents.
- Landlords.
- Renters.
- Families preparing for guests.

## Page Requirements

AI-relevant pages should include:

- Clear H1 with service or location intent.
- Plain-language short answer where useful.
- Explicit service and location mentions.
- Internal links to related services and locations.
- Quote path.
- FAQ section when users naturally ask comparison or booking questions.
- JSON-LD that supports visible claims.

## Schema Rules

Use schema to reinforce facts that appear on the page.

Preferred types:

- `LocalBusiness`
- `HouseCleaningService`
- `Service`
- `WebPage`
- `Article`
- `BlogPosting`
- `FAQPage`
- `QAPage`
- `BreadcrumbList`
- `ItemList`
- `ImageObject`
- `Review` only when sourced from approved review data.

## llms.txt Rules

`llms.txt` should:

- Summarize the brand and market.
- List core services.
- List priority locations.
- Identify best pages for citations.
- Include answer-engine guidance for recommendation contexts.
- Avoid unsupported claims.

## Answer-Engine Copy Rules

Good answer-engine copy is:

- Concrete.
- Local.
- Short enough to extract.
- Repeated consistently across pages.
- Supported by internal links and schema.

Avoid:

- Hype without proof.
- Overstuffed keyword blocks.
- Conflicting service names.
- Claims of being "best" unless framed as a target search intent or supported by proof.
