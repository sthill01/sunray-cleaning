# Webflow Fix Pack

This folder contains small, copy-ready pieces for the Sun Ray Webflow cleanup.

Use these with caution:

- Export existing Webflow redirects before importing a CSV. Webflow redirect CSV imports overwrite existing redirects.
- Only add AggregateRating schema if the rating and review count are real and current.
- Publish to Webflow staging first when possible.

## Files

- `robots.txt` - recommended robots content
- `redirects.csv` - redirect rows from the SEO strategy
- `google-tag.html` - Google tag snippet for Webflow site-wide head code
- `webflow-quick-wins-claude-prompt.md` - prompt for Webflow Claude
- `sitewide-localbusiness-schema.html` - starter schema block with placeholders
