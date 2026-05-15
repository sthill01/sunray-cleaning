# Sun Ray Weekly Webflow Maintenance Sprint

Run date: 2026-05-13 (America/Denver)

Scope: Prep a prioritized Webflow work-session checklist + copy-ready Claude prompts. This run does **not** change Webflow. Anything marked **Webflow-required** needs Designer/admin access (and sometimes third-party approvals).

Inputs used:

- `seo-automation/marketing-audit-workplan.md`
- `seo-automation/content-roadmap.md`
- `seo-automation/webflow-publishing-workflow.md`
- `seo-automation/runs/2026-05-11-local-seo-llm-visibility-check.md`
- `webflow-fix-pack/`
- `webflow-content-drafts/`
- SEO source folder reference (internal linking): `C:\Users\sthil\Documents\AI Projects\Projects\Sunray Clean Services SEO Market\Sunray SEO Obsidian Vault\On-Page-SEO\08 - Internal Linking Map.md`

Repo-only checks run (do not imply live Webflow status):

- Internal link check on `cloudflare-preview/`: `seo-automation/runs/2026-05-13-internal-link-report.md` (result: no missing internal links in that static build)

---

## Sprint checklist (prioritized)

### P0 - Indexing + redirect safety (highest leverage, lowest risk)

**Webflow-required**

1) Sitemap status check (Webflow setting)
   - Webflow: `Site settings -> SEO -> Indexing` (or equivalent)
   - Confirm auto-generated sitemap is enabled.
   - Confirm the live sitemap URL and canonical domain choice (www vs non-www).
   - Note: the prior route audit indicated `/sitemap.xml` returned 404 at crawl time (see `webflow-fix-pack/webflow-migration-route-audit.md`). Treat this as a must-verify.
2) Robots.txt status check (Webflow setting)
   - Webflow: `Site settings -> SEO -> Robots.txt`
   - Confirm robots.txt allows crawling and includes a `Sitemap:` line that matches the canonical domain.
   - If robots.txt is empty/weak, paste baseline from `webflow-fix-pack/robots.txt` and adjust the `Sitemap:` domain to match canonical.
3) Redirects: export-first + merge + import (Webflow imports overwrite)
   - Export existing redirects from Webflow **before** importing anything.
   - Merge the export with:
     - `webflow-fix-pack/redirects.csv` (7 rows from the SEO strategy)
     - `webflow-fix-pack/webflow-launch-redirects.csv` (migration coverage; 47 rows)
   - Import the merged CSV back into Webflow.
   - Spot-check 5 redirects (one Park City, one Heber, one Midway, one blog, one “weird” URL).
4) Dedupe cleanup (prevent thin/duplicate URLs)
   - Delete/unpublish known duplicates if still present:
     - `/untitled`
     - `/service-location/salt-lake-county-copy`

**Codex-prep (ready now)**

- Robots baseline: `webflow-fix-pack/robots.txt` (edit only the domain).
- Redirect rows staged:
  - Strategy redirects: `webflow-fix-pack/redirects.csv`
  - Migration redirects: `webflow-fix-pack/webflow-launch-redirects.csv`
- Route audit reference: `webflow-fix-pack/webflow-migration-route-audit.md`

**Copy-ready Webflow Claude prompt**

- Use Prompt A in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P1 - Broken links + SEO titles/meta + heading hygiene (traffic capture)

**Webflow-required**

1) Broken-link check (fast pass)
   - Run Webflow’s Audit/SEO panel for: broken links, missing alt text, duplicate IDs, skipped heading levels.
   - Spot-check nav/footer links across: Home, Services, Park City, Heber City, Midway/Wasatch County, and at least 1 blog post.
2) Page SEO audit + fix (titles/meta/OG + canonical)
   - Pages to hit first:
     - Home (`/`)
     - Services hub (`/services`)
     - Service pages: STR turnover, deep cleaning, move-in/out, recurring
     - Location pages: Park City, Heber City, Midway/Wasatch County
   - Ensure:
     - Title <~60 chars when practical
     - Meta description ~140–160 chars
     - Open Graph title/description/image filled on key pages
     - Canonical URL uses the same domain (www vs non-www) consistently
3) H1/heading fixes
   - Enforce exactly one H1 per page.
   - Fix the known H1 typo on Recurring Cleaning service page:
     - `Reccuring Cleaning for your Home` -> `Recurring Cleaning for Your Home`

**Codex-prep**

- Repo-only internal-link scan (static build): `seo-automation/runs/2026-05-13-internal-link-report.md` (0 missing).

**Copy-ready Webflow Claude prompt**

- Use Prompt B in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P2 - Trust + conversion quick wins (testimonials/reviews, forms, pricing anchors)

**Webflow-required**

1) Testimonials cleanup + replacements (no invented content)
   - Remove empty testimonial sections (or hide them) until real proof is added.
   - Target: 6–10 real, owner-approved review excerpts across homepage + services + 1–2 key service pages.
2) Reviews widget / trust module decision
   - Decide approach:
     - A) embed a reviews widget (vendor + approvals needed), OR
     - B) add a small “Google Reviews” proof module with manually selected excerpts (owner-approved) + link to GBP.
3) Form friction reduction (quote form)
   - Target: 4 required fields:
     - Name
     - Phone
     - Address (or City + ZIP)
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

- Google Business Profile access (for confirming profile URL and selecting real reviews)
- Widget vendor subscription/configuration (if used)
- Any booking software changes (Housecall Pro / Jobber / BookingKoala, etc.)

**Codex-prep**

- Review import workflow reference (official API, no scraping): `seo-automation/google-business-profile-review-import.md`.
- LocalBusiness schema starter has placeholders for `sameAs` links: `webflow-fix-pack/sitewide-localbusiness-schema.html` (do not paste until GBP profile URL is confirmed).

**Copy-ready Webflow Claude prompts**

- Use Prompt C (form), Prompt D (reviews), and Prompt E (pricing) in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

### P3 - Schema + internal links (compounding SEO + AI visibility)

**Webflow-required**

1) Sitewide LocalBusiness schema (entity disambiguation priority)
   - Add `webflow-fix-pack/sitewide-localbusiness-schema.html` into Webflow global custom code (usually `Site settings -> Custom code -> Head`).
   - Replace placeholders:
     - `REPLACE_WITH_CANONICAL_DOMAIN` (www vs non-www)
     - GBP profile URL (real, verified)
     - Facebook/Instagram URL(s) (real)
   - Expand `areaServed` over time (Park City, Heber City, Midway, Summit County, Wasatch County, plus key neighborhoods).
2) FAQ schema on pages with visible FAQs
   - Add FAQ schema only for FAQs visible on-page.
   - Prioritize: STR turnover service, Park City location, any pricing page, and the next published blog post.
3) Internal linking pass (bidirectional rule)
   - Every blog post links to at least 1 service page + 1 location page.
   - Every service and location page links to 2–3 relevant blog posts.
   - Use the internal linking map from the SEO source folder (linked above).

**Codex-prep**

- Internal linking map reference: `C:\Users\sthil\Documents\AI Projects\Projects\Sunray Clean Services SEO Market\Sunray SEO Obsidian Vault\On-Page-SEO\08 - Internal Linking Map.md`

**Copy-ready Webflow Claude prompts**

- Use Prompt F (schema) and Prompt H (internal links) in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

## Next CMS draft to stage (this session)

Commercial-intent focus (matches the 2026-05-11 visibility recommendations): stage **one** blog draft in Webflow as a draft (do not publish production until reviewed).

Recommended next draft to stage:

1) Jordanelle vacation rental turnover (ready)
   - `webflow-content-drafts/2026-05-06-jordanelle-vacation-rental-turnover.md`

Backup options (also ready):

2) Park City summer guest-prep checklist
   - `webflow-content-drafts/2026-04-29-getting-your-park-city-home-ready-for-summer-guests.md`
3) Heber City move-in/move-out cleaning
   - `webflow-content-drafts/2026-04-27-heber-city-move-in-move-out-cleaning.md`

**Webflow-required**

- Create/update the CMS draft (Blog), paste content, set slug, set SEO title/meta, add internal links, and ensure only one H1.
- Add FAQ schema based only on the visible FAQ section.
- After staging, run Prompt G in `webflow-fix-pack/webflow-weekly-maintenance-claude-prompt.md`.

---

## Optional stretch (if time remains)

These are higher-effort but align with the 2026-05-11 visibility findings.

**Webflow-required**

1) Draft a dedicated Park City STR landing page (city + service match)
   - Suggested slug: `/park-city-airbnb-vrbo-turnover-cleaning`
   - Link from Park City location page and STR service page.
2) Draft county hub pages (thin MVP first)
   - `/summit-county-house-cleaning`
   - `/wasatch-county-house-cleaning`

