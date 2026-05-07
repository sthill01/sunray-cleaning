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
- `google-tag-manager.html` - Google Tag Manager container snippet for Webflow head and body code
- `google-tag-manager-head.html` - GTM head code only
- `google-tag-manager-body.html` - GTM noscript body code only
- `google-ads-lead-form-conversion.html` - Google Ads lead-submit conversion snippet for quote forms
- `webflow-quick-wins-claude-prompt.md` - prompt for Webflow Claude
- `sitewide-localbusiness-schema.html` - starter schema block with placeholders

Note: use either the direct Google tag or Google Tag Manager as the main install path. If GTM is installed and contains the Google tag, do not also paste `google-tag.html` sitewide.
