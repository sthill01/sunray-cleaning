# Marketing Audit Workplan

Source: `C:\Users\sthil\Documents\GitHub\desktop-tutorial\MARKETING-AUDIT.md`

Audit date: April 23, 2026

Current date: April 25, 2026

## Main Diagnosis

The audit grades Sun Ray Cleaning at 37/100 because the website has trust, conversion, and technical SEO gaps:

- Empty testimonial sections
- Long 13-field quote form
- No visible pricing anchor
- Gmail business email
- Sitemap issue
- Empty or weak robots.txt
- Missing schema
- Multi-H1 page structure
- Missing or weak meta titles/descriptions
- Broken internal links
- Weak visible Google review/GBP trust signals

## What We Can Automate Or Semi-Automate

### Can Automate From This Repo / Codex

These are safe to run as recurring checks or generated files:

- Crawl pages for broken internal links.
- Generate SEO title/meta descriptions for pages.
- Generate FAQ schema and LocalBusiness/Service JSON-LD.
- Generate robots.txt content.
- Generate 301 redirect CSVs for Webflow import.
- Draft Webflow CMS posts and landing-page copy.
- Create htflow-ready page prototypes.
- Compare competitors and keyword opportunities weekly.
- Maintain a content calendar and next-draft queue.
- Produce Webflow Claude prompts for each task.

### Can Automate With Webflow Claude / MCP After Connection

These should be possible or partly possible once the Webflow connector is connected and authorized:

- Audit Webflow page metadata.
- Update SEO titles, meta descriptions, Open Graph fields, and slugs with approval.
- Review CMS items for missing fields, thin content, missing FAQs, and weak internal links.
- Create or update CMS blog drafts.
- Assist with class cleanup and layout review after htflow imports.
- Apply bulk CMS updates with approval.
- Create or manage redirects where the Webflow plan/API permissions allow it.

### Best Done Manually In Webflow Designer

These involve visual judgment, third-party widgets, or account/admin settings:

- Turn Webflow auto-generated sitemap on.
- Publish the site after SEO setting changes.
- Install and configure a Google Reviews widget.
- Replace testimonial placeholders with approved real reviews.
- Change the quote form layout and required fields.
- Add sticky mobile CTA bar.
- Fix multi-H1 structure in visual layouts.
- Connect booking software such as Housecall Pro, Jobber, or BookingKoala.
- Set up Google Workspace email.
- Verify Google Business Profile, Local Services Ads, and directory accounts.

## Priority Schedule

### Sprint 1: Technical Indexing And Trust Basics

Target: next 2-3 working days.

1. Re-enable Webflow sitemap:
   - Webflow Site settings > SEO > Indexing
   - Turn auto-generated sitemap on
   - Publish
   - Verify `https://sunray-cleaning.com/sitemap.xml`
2. Add robots.txt:
   - `User-agent: *`
   - `Allow: /`
   - `Sitemap: https://sunray-cleaning.com/sitemap.xml`
3. Add required redirects from the SEO strategy.
4. Fix broken internal links in flagship posts.
5. Run Webflow Audit panel for missing alt text, skipped headings, duplicate IDs, and link labels.

### Sprint 2: Conversion Quick Wins

Target: same week.

1. Replace empty testimonials with 6-10 real reviews.
2. Add Google Reviews widget.
3. Reduce quote form to 4 required fields:
   - Name
   - Phone
   - Address
   - Service Type
4. Move square footage and notes to optional.
5. Add pricing anchors:
   - Recurring from $149
   - Deep clean from $289
   - STR turnover from $119
6. Standardize CTAs:
   - Primary: `Get My Free Quote`
   - Secondary: `Call or text (801) 604-2189`

### Sprint 3: Schema And Local Search

Target: following week.

1. Add LocalBusiness schema sitewide.
2. Add Service schema to service pages.
3. Add FAQ schema to pages with FAQs.
4. Add BlogPosting schema to blog posts.
5. Update page titles and meta descriptions.
6. Add founder/team proof to About page.

### Sprint 4: STR And Neighborhood Growth

Target: next month.

1. Build STR-focused landing page.
2. Create first 12 programmatic neighborhood/service pages.
3. Create property-manager partnership page.
4. Build quote calculator prototype.
5. Launch weekly blog cadence around pricing, STR cleaning, and hyper-local neighborhoods.

## Automation Candidates

Already created:

- `Sun Ray Local SEO and LLM Visibility Monitor` runs every Monday at 8:00 AM.

Recommended next automation:

- Weekly Webflow maintenance sprint report every Wednesday:
  - Review pending Webflow tasks
  - Generate next content draft
  - Check sitemap/robots/redirects/broken links
  - Suggest Webflow Claude actions

