# Sun Ray AI Search + Local SEO Prompt Pack (use with Codex/ChatGPT)

These prompts are designed to generate Webflow-ready drafts, social repurposing, and weekly monitoring outputs while keeping Sun Ray’s voice: local, warm, practical, transparent, and specific to Park City / Heber City / Midway / Summit County / Wasatch County.

Note: keep public URLs extensionless (no `.html`).

---

## Prompt A — Webflow draft (page or blog)

```text
You are writing for Sun Ray Cleaning Services (Wasatch Back, Utah).

Target audience:
- Park City, Heber City, and Midway homeowners
- Vacation-home owners
- Airbnb/VRBO hosts and property managers

Target query: [PASTE PRIMARY KEYWORD]
Page type: [Webflow page OR Webflow CMS blog post]
Slug: [PASTE SLUG]
Primary city/area: [Park City / Heber City / Midway / Summit County / Wasatch County]
Service focus: [STR turnover / deep clean / recurring / move-in/out]

Write a Webflow-ready markdown draft with:
- SEO title and meta description
- Primary/secondary keywords
- Direct-answer intro paragraph (first 100 words)
- Practical sections with checklists where appropriate
- 5–8 FAQs (visible on page)
- Internal links list (service + location + contact)
- Clear CTA with (801) 604-2189
- A “Webflow Claude Prompt” block at the end

Constraints:
- Do not invent reviews or testimonials.
- Avoid making claims you can’t verify (licenses, awards, years-in-business).
- Use local details (Deer Valley, Canyons Village, Old Town, Red Ledges, Jordanelle) naturally.
```

---

## Prompt B — Social repurposing pack (from one page/post)

```text
Create a 2-week social pack from this page/post draft for Sun Ray Cleaning Services.

Inputs:
- Draft text: [PASTE DRAFT]
- Target area: [Park City / Heber / Midway]

Output:
1) 9 short posts (3/week x 3 weeks) for Instagram/Facebook (no hashtags required; keep local mention to 1 per post)
2) 1 Google Business Profile post (no phone number in description; use “Learn more” CTA)
3) 1 SMS review-request template (ask for honest review; suggest service + city phrasing)
4) 1 “internal links to add” reminder list (2–3 older pages that should link to the new page)
```

---

## Prompt C — Weekly visibility monitor write-up (manual-assisted)

```text
Run a local SEO + AI-search visibility snapshot for Sun Ray Cleaning Services.

Use the priority query set from seo-automation/keyword-competitor-monitor.md.
Competitors to compare:
- Park City House Cleaning
- Clean Casa
- High Mountain Luxury Cleaning
- Heber City Cleaning
- Chikas Cleaners
- Wasatch Cleaning
- American Housekeeping of Utah

Output a dated report in seo-automation/runs/YYYY-MM-DD-local-seo-llm-visibility-check.md with:
1) wins/losses vs last run
2) who shows up per query (directional; note constraints)
3) directories/review sites cited
4) low-hanging keyword opportunities
5) high-conversion keyword opportunities
6) pages to create/update in Webflow
7) internal links to add
8) schema/FAQ improvements
9) review/citation/backlink actions

If exact Google local-pack rank cannot be verified, say so and provide organic/citation proxies instead.
```
