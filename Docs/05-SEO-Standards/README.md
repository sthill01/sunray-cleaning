# 05 SEO Standards

## Technical SEO Priorities

1. Crawlability.
2. Clean canonical URLs.
3. Accurate sitemap output.
4. Internal link integrity.
5. Structured data consistency.
6. Fast pages.
7. Clear titles and descriptions.
8. Useful content for real local searches.

## Route Standards

- Public routes should be clean and extensionless.
- Use trailing slash routes in generated output.
- Avoid duplicate public routes for the same intent.
- Preserve redirects for legacy routes.

## Metadata Standards

Every indexable page should have:

- Unique title.
- Unique meta description.
- Canonical URL.
- Robots metadata appropriate to preview or production.
- Open Graph title and description where source pages define them.

## Sitemap Standards

Generated sitemap should include public routes and omit internal-only routes.

Priority should reflect business importance:

- Home: highest.
- AI authority and core local/service pages: high.
- Blog guides: useful but usually lower than money pages.

## Internal Linking Standards

Internal links should connect:

- Home to core services, service areas, and AI authority pages.
- Services to high-value locations and related guides.
- Locations to services, parent areas, child neighborhoods, and quote paths.
- Blog posts to services, locations, quote paths, and AI authority pages.

## Robots Standards

Preview builds should be noindex.

Production builds should be crawlable only after QA confirms:

- Canonicals are production URLs.
- Sitemap uses production URLs.
- Internal links pass.
- Important routes render.
- No preview-only copy remains in visible text.

## Image SEO Standards

Images should have:

- Descriptive file names.
- Relevant alt text.
- Local context when accurate.
- Reused schema metadata when sourced from job-gallery data.
