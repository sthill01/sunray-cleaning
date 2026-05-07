# Sun Ray Weekly Webflow Maintenance Sprint

Run date: 2026-05-06 (America/Denver)

Scope: Prep a prioritized Webflow work-session checklist + copy-ready Claude prompts. This run does **not** change Webflow. Anything marked **Webflow-required** needs Designer/admin access (and sometimes third-party approvals).

Inputs used:

- `seo-automation/marketing-audit-workplan.md`
- `seo-automation/content-roadmap.md`
- `seo-automation/webflow-publishing-workflow.md`
- `webflow-fix-pack/`
- `webflow-content-drafts/`
- SEO source folder (reference): `C:\Users\sthil\Documents\AI Projects\Projects\Sunray Clean Services SEO Market`

Repo-only checks run (do not imply live Webflow status):

- Internal link check on `cloudflare-preview/`: `seo-automation/runs/2026-05-06-internal-link-report.md` (result: no missing internal links in that static build)

---

## Sprint checklist (prioritized)

### P0 - Indexing + redirect safety (highest leverage, lowest risk)

**Webflow-required**

1) Sitemap status check (Webflow setting)
   - Webflow: `Site settings -> SEO -> Indexing` (or equivalent)
   - Confirm auto-generated sitemap is enabled.
   - Confirm the live sitemap URL (www vs non-www). Record which is canonical in Webflow.
2) Robots.txt status check (Webflow setting)
   - Webflow: `Site settings -> SEO -> Robots.txt`
   - Confirm robots.txt allows crawling and includes a `Sitemap:` line that matches the canonical domain.
   - If robots.txt is empty/weak, paste baseline from `webflow-fix-pack/robots.txt` and adjust `Sitemap:` domain to match canonical.
3) Redirects: export-first + merge + import
   - Export existing redirects from Webflow **before** importing anything (Webflow imports overwrite).
   - Merge the export with `webflow-fix-pack/redirects.csv` (7 rows).
   - Import the merged CSV back into Webflow.
   - Spot-check 3 redirects (one Park City, one Heber, one "vacation seasonal").
4) Dedupe cleanup (prevent thin/duplicate URLs)
   - Delete/unpublish known duplicates if still present:
     - `/untitled`
     - `/service-location/salt-lake-county-copy`

**Codex-prep**

- Redirect rows already staged in `webflow-fix-pack/redirects.csv`; only import after exporting and merging Webflow's current redirects.
- Robots baseline staged in `webflow-fix-pack/robots.txt`.

**Copy-ready Webflow Claude prompt**

- Use Prompt A in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P1 - Broken links + SEO titles/meta + heading hygiene

**Webflow-required**

1) Broken-link check (fast pass)
   - Run Webflow's Audit/SEO panel for: broken links, missing alt text, duplicate IDs, skipped heading levels.
   - Spot-check nav/footer links across: Home, Services, Park City, Heber City, Midway, and at least 1 blog post.
2) SEO titles/meta audit + fix (high-impact pages first)
   - Pages to hit first:
     - Home (`/`)
     - Services hub (`/services`)
     - Service pages: STR turnover, deep cleaning, move-in/move-out, recurring
     - Location pages: Park City, Heber City, Midway
   - Ensure:
     - title ~<60 chars when practical
     - meta description ~140-160 chars
     - Open Graph title/description/image filled on key pages
3) H1/heading fixes
   - Enforce exactly one H1 per page.
   - Fix the known H1 typo on the Recurring Cleaning service page:
     - `Reccuring Cleaning for your Home` -> `Recurring Cleaning for Your Home`

**Codex-prep**

- Repo-only internal link scan completed for the static build: `seo-automation/runs/2026-05-06-internal-link-report.md`.
- Use the metadata pack below as a starting point (adjust in Webflow for the canonical domain and actual page names).

**Suggested SEO titles/meta (starting point)**

- Home
  - Title: `House Cleaning in Park City, Heber City & Midway | Sun Ray Cleaning`
  - Meta: `Female-owned cleaning for Park City and Heber Valley homes. Recurring, deep cleans, move-in/out, and STR turnovers. Call/text (801) 604-2189.`
- Services hub
  - Title: `Cleaning Services in Park City & Heber Valley | Sun Ray Cleaning`
  - Meta: `Compare recurring cleaning, deep cleaning, move-in/out, and short-term rental turnovers. Local team serving Park City, Heber City, and Midway.`
- STR turnover service
  - Title: `STR Turnover Cleaning (Airbnb/VRBO) | Park City & Heber`
  - Meta: `Guest-ready turnovers for Park City, Jordanelle, Heber City, and Midway rentals. Consistent checklists, linens support, and fast resets. (801) 604-2189.`
- Deep cleaning service
  - Title: `Deep Cleaning in Park City, Heber City & Midway | Sun Ray`
  - Meta: `Detailed resets for kitchens, bathrooms, baseboards, and buildup. Great for seasonal homes, move-ins, and guest prep across the Wasatch Back.`
- Move-in/out service
  - Title: `Move-In & Move-Out Cleaning in Heber City & Park City | Sun Ray`
  - Meta: `Move-ready cleans for buyers, renters, landlords, and real estate walkthroughs. Appliance and cabinet detail available by request.`
- Recurring service
  - Title: `Recurring House Cleaning (Weekly/Biweekly/Monthly) | Sun Ray`
  - Meta: `Keep your Park City, Heber City, or Midway home guest-ready with a consistent schedule. Clear checklists, local team, easy quoting.`
- Park City location
  - Title: `House Cleaning in Park City, UT | Sun Ray Cleaning`
  - Meta: `Local cleaning for Park City homes, second homes, and STRs. Deep cleans, recurring, and turnover service. Call/text (801) 604-2189.`
- Heber City location
  - Title: `House Cleaning in Heber City, UT | Sun Ray Cleaning`
  - Meta: `Heber Valley cleaning for families, new builds, and seasonal homes. Recurring, deep, move-in/out, and turnovers. (801) 604-2189.`
- Midway location
  - Title: `House Cleaning in Midway, UT | Sun Ray Cleaning`
  - Meta: `Cabins, vacation homes, and residential cleaning in Midway. Deep cleans, recurring schedules, and guest-ready resets. (801) 604-2189.`

**Copy-ready Webflow Claude prompt**

- Use Prompt B in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P2 - Trust + conversion quick wins (testimonials, reviews, forms, pricing anchors)

**Webflow-required**

1) Testimonials: remove empties + add real proof
   - If any testimonial sections are empty, remove or replace.
   - Minimum target: 6-10 real reviews/testimonials across homepage + services + 1-2 key service pages.
   - Do **not** invent testimonials. Use owner-approved excerpts only.
2) Google Reviews widget decision + implementation
   - Choose approach:
     - embed a reviews widget (requires vendor account + configuration), OR
     - manually add selected reviews into Webflow CMS/components.
3) Form friction reduction (quote form)
   - Target: 4 required fields:
     - Name
     - Phone
     - Address (or City + ZIP if preferred)
     - Service Type
   - Move square footage and notes to optional.
4) Pricing anchors + CTA consistency
   - Place anchors where users decide:
     - Recurring from $149
     - Deep clean from $289
     - STR turnover from $119
   - Standardize CTAs:
     - Primary: `Get My Free Quote`
     - Secondary: `Call or text (801) 604-2189`

**Third-party/admin approval likely required**

- Google Business Profile access (for exporting reviews / verifying counts)
- Widget vendor subscription/configuration (if used)
- Any booking/payment integration changes

**Codex-prep**

- Review proof baseline exists in `data/reviews.json` but `profileUrl` is blank; fill only after GBP URL is confirmed.
- GBP import workflow reference: `seo-automation/google-business-profile-review-import.md` (official API path, no scraping).

**Copy-ready Webflow Claude prompts**

- Use Prompt C (form), Prompt D (reviews), and Prompt E (pricing) in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P3 - Schema + internal links (compound SEO gains)

**Webflow-required**

1) Sitewide LocalBusiness schema
   - Add `webflow-fix-pack/sitewide-localbusiness-schema.html` into Webflow global custom code (usually `Site settings -> Custom code -> Head`).
   - Replace placeholders:
     - `REPLACE_WITH_CANONICAL_DOMAIN` (www vs non-www)
     - GBP profile URL
     - Instagram/Facebook URL(s)
2) FAQ schema on pages that have visible FAQs
   - Add FAQ schema only for FAQs that are visible on-page.
   - Start with: STR turnover, move-in/out, Park City location, and any newly published blog post.
3) Internal-link updates (bidirectional rule)
   - For any new/updated blog post:
     - add at least 1 service-page link + 1 location-page link
     - edit 2-3 older related posts to link forward to the new post
   - Use the SEO source's internal linking map:
     - `C:\Users\sthil\Documents\AI Projects\Projects\Sunray Clean Services SEO Market\Sunray SEO Obsidian Vault\On-Page-SEO\08 - Internal Linking Map.md`

**Codex-prep**

- Schema starter staged in `webflow-fix-pack/sitewide-localbusiness-schema.html` (placeholder-safe; requires domain + social URLs in Webflow).

**Copy-ready Webflow Claude prompts**

- Use Prompt F (schema) and Prompt H (internal links) in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

## Next CMS draft to stage (this session)

Pick one to stage during the Webflow session (draft first; do not publish until reviewed):

1) Heber City move-in/move-out cleaning (ready)
   - `webflow-content-drafts/2026-04-27-heber-city-move-in-move-out-cleaning.md`
2) Park City summer guest-prep checklist (ready)
   - `webflow-content-drafts/2026-04-29-getting-your-park-city-home-ready-for-summer-guests.md`
3) Jordanelle turnover cleaning (new draft; commercial intent)
   - `webflow-content-drafts/2026-05-06-jordanelle-vacation-rental-turnover.md`

**Webflow-required**

- Create/update the CMS draft (Blog), paste content, set slug, set SEO title/meta, add internal links, and ensure only one H1.
- Add FAQ schema based only on the visible FAQ section.
- Run Prompt G in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md` after staging.

