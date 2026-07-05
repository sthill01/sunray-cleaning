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

## Prompt J - Stage Red Ledges CMS blog draft

```text
Create or update a Webflow CMS blog draft for Sun Ray Cleaning using the Red Ledges markdown I paste next.
Do not publish production.

Use this slug:
red-ledges-home-cleaning-guide-luxury-heber-homeowners

Before applying changes:
- Confirm the Webflow site and CMS collection item you are editing.
- Confirm whether a live or draft item already exists for this slug.
- Preserve the brand name exactly: Sun Ray Cleaning.

CMS requirements:
- Preserve the H1, H2s, FAQs, internal links, and phone CTA.
- Add the SEO title and meta description from the draft.
- Add or confirm the hero image and alt text.
- Add FAQ schema only for the visible FAQ section.
- Ensure exactly one H1.
- Keep links pointed at current Webflow routes, especially /services/recurring-cleaning, /services/deep-cleaning, /services/short-term-rental-cleaning, /service-location/heber-city, and /service-location/wasatch-county.

After staging:
- Report whether the item is draft or published.
- List missing CMS fields, broken links, schema issues, and manual review items.
- Do not publish production unless I explicitly approve it.
```

---

## Prompt K - Prepare Park City deep vs recurring draft decision

```text
Audit the next Sun Ray Cleaning blog item: Park City Deep Cleaning vs. Recurring Cleaning.
Do not publish production.

Current planning title:
Park City Deep Cleaning vs. Recurring Cleaning: Which Service Do You Need?

Before making changes:
- Confirm whether Webflow already has a CMS item for this topic.
- Report the current slug if it exists.
- Compare it against these possible slugs:
  - /blog/park-city-deep-cleaning-vs-recurring-cleaning/
  - /blog/recurring-vs-deep-cleaning-which-service-need/

Recommend whether to keep the existing slug or update it for Park City search intent. If a slug change is recommended, ask before changing and include the redirect needed from the old slug to the new slug.

Then prepare the draft fields:
- SEO title under about 60 characters when practical.
- Meta description around 140-160 characters.
- Internal links to /services/deep-cleaning, /services/recurring-cleaning, /service-location/park-city, /service-location/heber-city, and /service-location/midway where natural.
- FAQ schema only if visible FAQs exist.

Return a concise staging checklist and do not publish production unless I explicitly approve it.
```

---

## Prompt L - Stage Park City deep vs recurring CMS draft

```text
Create or update a Webflow CMS blog draft for Sun Ray Cleaning using the Park City deep-cleaning-vs-recurring markdown I paste next.
Do not publish production.

Before applying changes:
- Confirm the Webflow site and CMS collection item you are editing.
- Confirm whether a live or draft item already exists for either of these routes:
  - /blog/park-city-deep-cleaning-vs-recurring-cleaning/
  - /blog/recurring-vs-deep-cleaning-which-service-need/
- If both exist, stop and report the duplicate-risk before editing.
- Preserve the brand name exactly: Sun Ray Cleaning.

Preferred calendar slug:
park-city-deep-cleaning-vs-recurring-cleaning

Existing repo/live route found during the 2026-06-24 prep run:
recurring-vs-deep-cleaning-which-service-need

If changing the slug, ask before applying it and list the needed 301 redirect from the old route to the new route.

CMS requirements:
- Preserve the H1, H2s, FAQs, internal links, and phone CTA.
- Add the SEO title and meta description from the draft.
- Use or confirm the hero image: assets/park-city-deep-cleaning-bathroom-detail-sun-ray.jpg.
- Add FAQ schema only for the visible FAQ section.
- Ensure exactly one H1.
- Keep links pointed at current Webflow routes, especially /services/deep-cleaning, /services/recurring-cleaning, /services/move-in-move-out-cleaning, /service-location/park-city, /service-location/heber-city, and /service-location/midway.

After staging:
- Report whether the item is draft or published.
- List missing CMS fields, broken links, schema issues, redirect needs, and manual review items.
- Do not publish production unless I explicitly approve it.
```

---

## Prompt A - Indexing (sitemap + robots) + redirect safety

```text
Audit this Webflow site's indexing setup and redirect hygiene:

1) Confirm whether the auto-generated sitemap is enabled. Report the exact live sitemap URL (www vs non-www).
   - Also confirm whether core service pages appear in the sitemap (example targets: /services/deep-cleaning, /services/short-term-rental-cleaning).
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

Do not fabricate testimonials, star ratings, review counts, or dates. Ask before adding any review text.
If you propose displaying a rating or review count, ask me to confirm the exact current values from Google Business Profile first.
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

---

## Prompt M - Production crawl-control repair

```text
Audit and repair the production crawl-control setup for Sun Ray Cleaning.

Known live issues from the 2026-07-01 read-only check:
- https://www.sunray-cleaning.com/ returned x-robots-tag: noindex, follow.
- https://www.sunray-cleaning.com/robots.txt included a final User-agent: * / Disallow: / block.
- robots.txt pointed the Sitemap line to https://sunray-cleaning-preview.pages.dev/sitemap.xml.
- https://www.sunray-cleaning.com/sitemap.xml returned preview-domain loc values.
- Cloudflare Managed Content rules disallowed ClaudeBot, GPTBot, Google-Extended, CCBot, and related crawlers.

Tasks:
1) Confirm whether the noindex header is coming from Webflow, Cloudflare Pages, Cloudflare Rules, _headers, or another layer.
2) Confirm the intended canonical domain is https://www.sunray-cleaning.com.
3) Replace production robots/sitemap behavior so normal search crawlers can index the site and sitemap loc values use the www production domain.
4) Separate the AI-crawler policy decision from ordinary search indexing; do not change Cloudflare Managed Content rules until I approve the policy.
5) After any approved change, purge or bypass cache and recheck:
   - curl -I https://www.sunray-cleaning.com/
   - curl https://www.sunray-cleaning.com/robots.txt
   - curl https://www.sunray-cleaning.com/sitemap.xml

Do not publish production, change Cloudflare settings, or purge cache until I explicitly approve each action.
Return the exact setting changed, the before/after evidence, and any remaining blocker.
```

---

## Prompt N - Convert new summer turnover source into a CMS draft

```text
Prepare a Webflow CMS draft from the source article I paste next:
"Behind the Scenes: How Sun Ray Handles Peak Summer Turnover Season in Park City"

Do not publish production.

Suggested slug:
behind-the-scenes-summer-turnover-cleaning-park-city

Before applying changes:
- Confirm whether a CMS item already exists for this slug.
- Confirm the Webflow site and CMS collection item you are editing.
- Preserve the brand name exactly: Sun Ray Cleaning.

CMS requirements:
- Preserve the H1, H2s, body copy, internal links, and CTA.
- Add an SEO title under about 60 characters when practical.
- Add a meta description around 140-160 characters.
- Recommend one hero image concept and alt text from approved Sun Ray assets.
- Add FAQ schema only if visible FAQs exist in the pasted copy.
- Ensure exactly one H1.

After staging:
- Report whether the item is draft or published.
- List missing CMS fields, broken links, schema issues, redirect needs, and manual review items.
- Do not publish production unless I explicitly approve it.
```
