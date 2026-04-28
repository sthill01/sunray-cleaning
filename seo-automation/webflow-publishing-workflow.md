# Webflow Publishing Workflow

Use this workflow for every new Sun Ray page, blog post, or location/service update.

## 1. Draft In This Repo

Create a draft in `webflow-content-drafts/` with:

- SEO title
- meta description
- slug
- target keyword
- search intent
- internal links
- image/alt recommendations
- FAQ section
- JSON-LD schema block when needed
- Webflow Claude prompt notes

## 2. Stage In Webflow

Preferred path:

1. Create the page or CMS item as a Webflow draft.
2. Paste the draft content.
3. Add Webflow-native headings, rich text, images, buttons, and related links.
4. Use Webflow Claude to inspect structure, alt text, class consistency, metadata, and mobile issues.
5. Do not publish production until review is complete.

For designed landing pages:

1. Use `webflow-import-kit/` or a page-specific htflow HTML file.
2. Import with htflow into a duplicate/staging Webflow page.
3. Replace externally hosted staging images with Webflow assets.
4. Check tablet and mobile breakpoints manually.
5. Use Webflow Claude to identify cleanup work.

## 3. Pre-Publish Checklist

- H1 appears once.
- SEO title is under 60 characters when practical.
- Meta description is around 140-160 characters.
- Canonical URL matches final URL.
- Open Graph title/image are set.
- FAQ section is visible on-page.
- JSON-LD validates conceptually and matches visible content.
- At least 3 internal links are present.
- Phone CTA is above the fold or near the first CTA.
- Images have descriptive alt text.
- Webflow preview works on desktop and mobile.

## 4. Publish And Record

After publishing:

- Copy the live URL into the draft file.
- Add the page to the internal linking map.
- Update 2-3 older related posts/pages to link forward to the new content.
- Add one Google Business Profile post that links or refers to the new page.
- Add a backlink/outreach follow-up if the topic supports it.

## 5. Webflow Claude Guardrail Prompt

```text
Before making changes, confirm the Webflow site and page/CMS item you are connected to.
Work only in draft/staging unless I explicitly approve production publishing.
Review this page for Sun Ray Cleaning SEO, local-search strength, AI-search extractability, accessibility, internal links, schema alignment, and mobile layout.
Preserve the brand voice: local, warm, practical, transparent, and specific to Park City, Heber City, Midway, Summit County, and Wasatch County.
Return a concise change log and any manual review items.
```

