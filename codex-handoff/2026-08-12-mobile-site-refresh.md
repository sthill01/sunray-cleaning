# Sun Ray Cleaning — Codex Handoff

Date: 2026-08-12
Branch: `codex/mobile-site-refresh-2026-08-12`
Repository: `sthill01/sunray-cleaning`

## Objective

Use Codex to take over the Sun Ray Cleaning website refresh from this branch. The work has three linked goals:

1. Fix the mobile navigation defect currently visible on production.
2. Audit the entire site for similar mobile/responsive issues and correct them.
3. Refresh the site copy for clearer human readability while preserving strong local SEO and making the content easy for AI systems to understand and cite.

Do not redesign the brand or substantially change the visual identity unless required to fix usability.

## Confirmed mobile bug

On mobile, the `Services` / `Service areas` dropdown can render partly off-screen to the left. The current responsive CSS changes `.nav-dropdown` to `position: static`, but the more-specific desktop hover/focus selector can still reapply `transform: translate(-50%, 0)`. This is consistent with the production screenshot where the submenu content is shifted roughly half a panel width off-screen.

Relevant source: `styles-gpt.css`.

Current desktop behavior includes selectors similar to:

```css
.nav-item:hover .nav-dropdown,
.nav-item:focus-within .nav-dropdown {
  opacity: 1;
  pointer-events: auto;
  transform: translate(-50%, 0);
}
```

Mobile currently switches the dropdown to static layout, but the mobile hover/focus override does not explicitly neutralize the desktop transform.

Expected minimal fix inside the mobile breakpoint:

```css
.nav-item:hover .nav-dropdown,
.nav-item:focus-within .nav-dropdown {
  display: grid;
  transform: none;
}
```

Validate the final implementation rather than blindly applying this snippet if surrounding CSS has changed.

## Site architecture / build note

The production Cloudflare build is generated from GPT source files. `tools/build-cloudflare-preview.py` copies `styles-gpt.css` to production output as `styles.css` and rewrites source links. Do not patch only generated output. Make fixes in the canonical source files used by the build.

The site uses a cache-busting constant in `tools/build-cloudflare-preview.py` named `STYLE_ASSET_VERSION`. If CSS changes are shipped, update that version so production browsers do not continue using the old stylesheet.

## Mobile audit scope

Test the full site at representative mobile widths, including at minimum 320, 360, 375, 390, 414, and 430 CSS px, plus a tablet width around 768 px. Check portrait first; then spot-check landscape.

Audit all major page families, not only the homepage:

- Home
- Services hub
- Individual service pages
- Service areas hub
- County pages
- City / neighborhood location pages
- Blog hub
- Representative blog posts
- About
- Contact / quote form
- Gallery and AI recommendation pages if public

Look specifically for:

- horizontal overflow / clipped content
- dropdowns or modals leaving the viewport
- sticky header collisions
- touch targets that are too small or too close together
- text wrapping under icons / buttons
- images exceeding viewport width
- cards with fixed widths or min-widths that break small screens
- long headings creating overflow
- forms that require sideways scrolling
- iframe / Trustindex embeds overflowing
- fixed or absolute elements covering content
- quote CTA collisions
- footer badge / review widget overflow
- anchor links hidden behind sticky header
- broken focus states and keyboard navigation
- mobile nav submenu behavior on touch devices, not just hover

Correct systemic CSS issues in shared styles before adding page-specific exceptions.

## Human readability + AI readability content refresh

Review public copy across the site and improve it without turning it into generic SEO text.

Priorities:

- shorter paragraphs and cleaner sentence structure
- clear service names in headings
- answer user questions early on each page
- reduce repetitive location / keyword phrasing
- preserve useful local specificity for Park City, Heber City, Midway, Summit County, Wasatch County, Deer Valley, Canyons Village, Kamas, Oakley, etc.
- make key facts easy to extract: what the service is, who it is for, where it is available, what is included, how quotes work, how scheduling works
- use descriptive H1/H2 hierarchy instead of promotional filler
- keep FAQ answers concise and factual
- avoid unsupported superlatives or claims
- keep phone and quote CTAs obvious
- preserve schema/structured data accuracy
- avoid duplicate page intent or near-duplicate paragraphs across city pages

The goal is copy that reads naturally to a homeowner while also being structurally clear for search engines and AI assistants.

## AI / machine-readability checks

Review and preserve or improve:

- title tags and meta descriptions
- canonical URLs
- LocalBusiness / FAQ structured data where present
- internal links between service and location pages
- breadcrumb or page hierarchy where implemented
- `llms.txt` / agent resource files generated by the build
- descriptive image alt text without keyword stuffing
- consistency between visible copy and structured data

Do not create claims in structured data that are not supported by visible content.

## Acceptance criteria

Before requesting merge:

1. The mobile menu renders fully within the viewport at all tested widths.
2. Services and Service areas submenus work reliably by touch and keyboard.
3. No representative public page has horizontal scrolling caused by layout overflow.
4. The quote modal/form works on mobile without clipping.
5. Shared widgets / review embeds stay within viewport bounds.
6. Major page templates pass a responsive visual audit.
7. Copy changes improve readability without removing local SEO coverage.
8. Structured data remains valid and consistent with visible content.
9. Build succeeds using the repository's Cloudflare build process.
10. CSS cache version is updated if shared CSS changes.
11. Changes remain on this branch and are submitted as a PR to `main` after testing.

## Suggested work sequence

1. Reproduce and fix the mobile nav bug.
2. Run a shared CSS/responsive audit and fix systemic overflow issues.
3. Test representative pages across breakpoints.
4. Refresh homepage and shared/navigation copy first.
5. Refresh service hubs and service pages.
6. Refresh location hubs/pages while removing repetitive SEO phrasing.
7. Refresh blog hub / representative posts only where readability needs it; avoid unnecessary rewrites.
8. Run build, link checks, responsive checks, and schema checks.
9. Summarize all changes in the PR with before/after screenshots for the major mobile fixes.

## Production safety

Do not push untested edits directly to `main`. Work on this branch, keep changes reviewable, and open a PR once the audit is complete.
