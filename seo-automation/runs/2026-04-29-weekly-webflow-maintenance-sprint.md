# Sun Ray Weekly Webflow Maintenance Sprint

Run date: 2026-04-29 (America/Denver)

Scope: Prep a prioritized Webflow work-session checklist + copy-ready Claude prompts. This run does **not** change Webflow; items marked "Webflow-required" need Designer/admin access and (sometimes) third-party approvals.

Inputs used:

- `seo-automation/marketing-audit-workplan.md`
- `seo-automation/content-roadmap.md`
- `seo-automation/webflow-publishing-workflow.md`
- `webflow-fix-pack/`
- `webflow-content-drafts/`
- SEO source folder: `C:\Users\sthil\Documents\AI Projects\Projects\Sunray Clean Services SEO Market`

---

## Sprint checklist (prioritized)

### P0 - Indexing + redirect safety (highest leverage, lowest risk)

**Webflow-required**

1) Sitemap status check (Webflow setting)
   - Webflow: `Site settings -> SEO -> Indexing` (or equivalent)
   - Confirm auto-generated sitemap is enabled.
   - Confirm the live sitemap URL (Webflow often serves either `https://www.sunray-cleaning.com/sitemap.xml` or `https://sunray-cleaning.com/sitemap.xml` depending on canonical domain).
   - After any change: publish, then verify sitemap loads in browser.
2) Robots.txt status check
   - Webflow: `Site settings -> SEO -> Robots.txt`
   - Confirm robots content includes a valid `Sitemap:` line matching the canonical domain.
   - If the live robots.txt is empty/weak, paste the recommended baseline from `webflow-fix-pack/robots.txt` and adjust domain if needed.
3) Redirects: export-first + merge + import
   - Export existing redirects from Webflow **before** importing anything (Webflow imports overwrite).
   - Merge existing export with `webflow-fix-pack/redirects.csv` (7 rows).
   - Import merged redirects CSV back into Webflow and verify a few spot-checks.
4) Dedupe cleanup (prevent thin/duplicate URLs)
   - Delete/unpublish the known duplicates:
     - `/untitled`
     - `/service-location/salt-lake-county-copy`

**Codex-prep**

- Keep `webflow-fix-pack/redirects.csv` as the "must-add" redirect set; during the Webflow session, export and merge rather than importing this file directly.

---

### P1 - Broken links + titles/meta + heading hygiene

**Webflow-required**

1) Broken-link check (fast pass)
   - Run Webflow's Audit/SEO panel for: broken links, missing alt text, duplicate IDs, skipped heading levels.
   - Spot-check nav/footer links across: Home, Services, Park City, Heber City, Midway, and at least 1 blog post.
2) SEO titles/meta audit + fix (high-impact pages first)
   - Priority pages:
     - Home (`/`)
     - Services hub (`/services`)
     - Service pages: STR turnover, deep cleaning, move-in/out, recurring
     - Location pages: Park City, Heber City, Midway (then Salt Lake County)
     - The 3 ready-to-publish blog drafts (from `seo-automation/content-roadmap.md`)
   - Ensure:
     - title ~<60 chars when practical
     - meta description ~140-160 chars
     - Open Graph title/description/image filled on key pages
3) H1/heading fixes
   - Enforce exactly one H1 per page.
   - Fix the known H1 typo on the Recurring Cleaning service page:
     - `Reccuring Cleaning for your Home` -> `Recurring Cleaning for Your Home`

**Codex-prep**

- Use the prompt pack in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md` for structured audits and copy generation (titles/meta, heading hierarchy).

---

### P2 - Trust + conversion quick wins (testimonials, reviews, forms, pricing anchors)

**Webflow-required**

1) Testimonials: remove empties + add real proof
   - If there are empty testimonial sections anywhere, remove or replace with real content.
   - Minimum target: 6-10 reviews/testimonials across homepage + services + 1-2 key service pages.
   - Do **not** invent testimonials. Use owner-approved excerpts only.
2) Google Reviews widget decision + implementation
   - Choose approach:
     - embed a reviews widget (requires vendor account + configuration), OR
     - manually add selected reviews into Webflow CMS/components.
3) Form friction reduction (quote form)
   - Target: 4 required fields (everything else optional)
     - Name
     - Phone
     - Address (or city + ZIP if full address is too heavy)
     - Service Type
   - Optional: square footage, timing, notes, access details, add-ons.
4) Pricing anchors
   - Place "starting at" anchors where users decide:
     - Recurring from $149
     - Deep clean from $289
     - STR turnover from $119
   - Add a short "how quotes work" note to avoid mismatch expectations.

**Third-party/admin approval likely required**

- Google Business Profile access (for review export/API), widget vendor subscription, Google Workspace (if email is still Gmail in production), payment/booking integrations.

**Codex-prep**

- If/when GBP API access is available, use `seo-automation/google-business-profile-review-import.md` to populate `data/reviews.json` for approved excerpts (no scraping/inventing).

---

### P3 - Schema + internal links (compound SEO gains)

**Webflow-required**

1) Sitewide LocalBusiness schema
   - Add the schema block from `webflow-fix-pack/sitewide-localbusiness-schema.html` into Webflow global custom code (usually `Site settings -> Custom code -> Head`).
   - Replace placeholders (domain, socials, GBP URL).
   - Ensure `@id`, `url`, and any sitemap links match canonical domain (www vs non-www).
2) FAQ schema on pages that have visible FAQs
   - Add FAQ schema only for FAQs that are **visible on-page**.
   - Start with:
     - STR turnover page
     - Move-in/out page
     - Park City location page
     - New blog posts as they publish
3) Internal-link updates (bidirectional rule)
   - For any new/updated blog post:
     - add at least 1 service-page link + 1 location-page link
     - edit 2-3 older related posts to link forward to the new post
   - Use the patterns in the SEO source's `08 - Internal Linking Map.md`.

**Codex-prep**

- Keep internal-link target suggestions in each `webflow-content-drafts/` markdown file so staging is mechanical.

---

## Next CMS draft to stage (this week)

Target: "Getting Your Park City Home Ready for Summer Guests" (educational) - scheduled for 2026-04-29 in the source calendar.

**Codex-prep**

- Draft created: `webflow-content-drafts/2026-04-29-getting-your-park-city-home-ready-for-summer-guests.md`

**Webflow-required**

- Create CMS draft (Blog) and stage the content, SEO title/meta, internal links, and FAQ section.
- Run the "Stage CMS draft" prompt from `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md` and review any manual items before publishing.

