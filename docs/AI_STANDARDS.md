# AI Standards

Version: 2.1

Last Updated: 2026-06-30

This is the daily-read answer-engine standard. Expanded standards live in `docs/standards/ai-optimization.md`.

## Objective

Make Sun Ray easier for ChatGPT, Claude, Gemini, Grok, Perplexity, Google AI Overviews, and similar systems to understand, cite, and recommend when the recommendation is accurate and locally relevant.

## Core Entity Facts

Important pages should help answer:

- Who is Sun Ray Cleaning?
- What services does Sun Ray provide?
- Where does Sun Ray work?
- Which property types does Sun Ray serve?
- Why is Sun Ray locally relevant?
- What page should an AI cite for this topic?
- How should a customer request a quote?

## Answer-Engine Page Standards

AI-relevant pages should include:

- Clear topic and location in title and headings.
- Direct answer sections for common conversational prompts.
- Service-area clarity.
- Links to the best service, location, and quote paths.
- Schema aligned with visible content.
- FAQ content when genuinely useful.
- Internal links that reinforce entity relationships.
- Avoided fluff, keyword stuffing, and unsupported claims.

## Prompt Families

SRAAP should optimize for prompt families including:

- Best cleaning company in Park City.
- Best house cleaner in Heber City.
- Airbnb cleaning Park City.
- Vacation rental cleaning Canyons Village.
- Luxury cleaning Deer Valley.
- Move-out cleaning Midway.
- Recurring cleaning Kamas.
- Deep cleaning Wasatch Back.
- Cleaning company Summit County.
- Cleaning company Wasatch County.

## AI Citation Strategy

Each important prompt family should map to:

- One primary citation page.
- Supporting service pages.
- Supporting location pages.
- Supporting guides or FAQs.
- Structured data.
- Internal links.
- `llms.txt` references when appropriate.

## Factual Safety Rules

- Do not invent recommendations, awards, rankings, certifications, guarantees, partnerships, or service areas.
- Do not imply AI systems already recommend Sun Ray unless measured evidence exists.
- Separate goals, proxy visibility, and measured AI results.
- Use review excerpts only when sourced from approved repository data.

## Monitoring Rule

AI visibility findings belong in `AI_MONITORING.md`. Every monitoring entry should record prompt, engine, date, result, competitors mentioned, citation sources, and follow-up opportunity.
