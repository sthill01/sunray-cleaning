# Webflow Claude Prompt Pack: Weekly Maintenance Sprint

Use these prompts inside Webflow Claude. Copy/paste one block at a time.

Guardrails for every prompt:

```text
Before making changes, confirm the Webflow site and page/CMS item you are connected to.
Work only in draft/staging unless I explicitly approve production publishing.
Do not delete anything without asking first.
Preserve the brand name exactly: Sun Ray Cleaning.
Return a concise change log and a manual review checklist.
```

---

## Prompt A - Indexing (sitemap + robots) + redirect safety

```text
Audit this Webflow site's indexing setup and redirect hygiene:

1) Confirm whether the auto-generated sitemap is enabled. Report the exact live sitemap URL (www vs non-www).
2) Inspect robots.txt. Ensure it allows crawling and includes a Sitemap line that matches the canonical domain.
3) Open the Redirects manager and instruct me how to export redirects BEFORE importing a CSV.
4) After export, I will merge in new redirect rows (I will provide the merged CSV). Tell me how to import it back safely.

Do not publish production unless I explicitly approve it.
```

---

## Prompt B - Page SEO audit (titles/meta/OG + H1 rules)

```text
For the current page/CMS item:

1) Report current SEO title, meta description, Open Graph title/description/image, and canonical URL fields.
2) Propose improved SEO title (try for <60 chars) and meta description (~140-160 chars).
3) Check headings: ensure exactly one H1 and sensible H2/H3 structure; list any problems.
4) Check internal links for broken or odd targets; list anything that needs manual verification.

Ask before applying any metadata changes.
```

---

## Prompt C - Form friction reduction (quote form)

```text
Review the quote/contact form on this page:

1) List all fields and which ones are required.
2) Propose a 4-required-field configuration:
   - Name
   - Phone
   - Address (or City + ZIP)
   - Service Type
3) Recommend which fields should become optional (square footage, timing, notes, access, add-ons).
4) Recommend a short helper text for each required field to reduce errors.

Do not change required/optional settings until I approve.
```

---

## Prompt D - Testimonials + review widget plan (no invented content)

```text
Audit this page for trust proof:

1) Identify any empty testimonial/review sections and propose what to remove or replace.
2) If a Google Reviews widget is present: report vendor and any visible settings.
3) If no widget: propose two approaches:
   A) embed a reviews widget (what vendor options exist and what approvals are needed)
   B) manually add 6-10 owner-approved review excerpts across site sections

Do not fabricate testimonials or star ratings. Ask before adding any review text.
```

---

## Prompt E - Pricing anchors + CTA consistency

```text
Add or propose placements for pricing anchors + CTAs on this page:

Pricing anchors:
- Recurring from $149
- Deep clean from $289
- STR turnover from $119

CTAs:
- Primary: Get My Free Quote
- Secondary: Call or text (801) 604-2189

Recommend exact section placements and short copy. Ask before applying edits.
```

---

## Prompt F - Schema insertion (LocalBusiness + FAQ schema)

```text
Schema audit for this page/site:

1) Confirm whether any JSON-LD schema is present (LocalBusiness, Service, FAQPage, Article/BlogPosting).
2) If missing, propose where to add:
   - Sitewide LocalBusiness schema (global head)
   - Page-level FAQ schema (only for FAQs visible on the page)
3) Ensure schema matches visible content and uses the canonical domain consistently (www vs non-www).

Ask before inserting code.
```

---

## Prompt G - Stage a blog CMS draft from repo markdown

```text
Create or update a Webflow CMS blog draft for Sun Ray Cleaning using the markdown I paste next.
Do not publish production.

Requirements:
- Use the provided slug.
- Preserve the H1, H2s, FAQs, internal links, and phone CTA.
- Add SEO title + meta description from the draft.
- Suggest one hero image concept + alt text.
- Add FAQ schema based only on the visible FAQ content.

After staging:
- report any missing CMS fields
- list any broken links or manual review items
```

---

## Prompt H - Internal linking pass (bidirectional rule)

```text
For the current page/CMS item:

1) List all internal links on this page (include anchor text + destination).
2) Recommend 3-6 additional internal links using the bidirectional rule:
   - every blog post links to at least 1 service page and 1 location page
   - service and location pages should link to 2-3 relevant blog posts
3) Suggest improved anchor text that is descriptive (no "click here").
4) Ask before inserting or changing any links.

Do not publish production unless I explicitly approve it.
```

---

## Prompt I - Draft a dedicated Park City STR landing page (city + service match)

```text
Help me draft a new dedicated landing page for Park City short-term rental turnover cleaning.

Before making changes:
- Confirm the Webflow site you are connected to and whether you are creating a new page or editing an existing draft page.
- Work only in draft/staging first.
- Do not publish production unless I explicitly approve it.

Page goal: capture non-brand "Airbnb cleaning Park City" / "VRBO turnover cleaning Park City" intent.

Requested slug (draft): /park-city-airbnb-vrbo-turnover-cleaning

1) Propose a simple, conversion-first section outline (H1 + H2s), including:
   - Above-the-fold hero with clear CTA
   - What’s included checklist (arrival-ready turnover)
   - What’s different about Park City STR turnovers (dust, hard water, fast windows)
   - Service areas (Park City + nearby)
   - Pricing anchors section (use these as anchors, not binding quotes): Recurring from $149; Deep clean from $289; STR turnover from $119
   - FAQs (5–8 STR-specific FAQs)
   - Final CTA block (Call/text + quote)
2) Check for heading hygiene (exactly one H1) and suggest internal links:
   - link to STR service page
   - link to Park City location page
   - link to pricing page if/when it exists
3) Propose SEO title (<60 chars when practical) + meta description (~140–160 chars) + OG fields.
4) If there is an FAQ section on-page, propose FAQ schema for only those visible FAQs (ask before inserting).

Ask before applying any edits or creating the page.
Return a concise change log and a manual review checklist.
```
