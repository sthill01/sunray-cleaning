# Sun Ray Webflow Import Pilot

This folder is a small experiment kit for testing whether Sun Ray should stay in Webflow or continue on the GitHub + Cloudflare Pages path.

## Current Source Of Truth

The production-ready static build is still this repository:

- `index.html`
- `services.html`
- `about.html`
- `service-location/*.html`
- `services/*.html`
- `styles.css`
- `assets/*`

Cloudflare staging:

```text
https://staging.sunray-cleaning-staging.pages.dev/
```

## Recommended Pilot

Use `home-hero-services-pilot.html` first. It is intentionally smaller than the full site and uses single-purpose `sr-` class names so htflow has less class cleanup to do.

1. Create or duplicate a Webflow site for testing.
2. Install/open htflow in the Webflow Designer.
3. Paste the full contents of `home-hero-services-pilot.html` into htflow.
4. Convert it into native Webflow elements.
5. Check desktop and mobile breakpoints.
6. Replace hosted staging image URLs with Webflow assets if the import looks good.
7. Use `webflow-claude-prompt.md` with the Webflow Claude connector to review structure, create page settings, or help refine classes.

## What We Are Testing

- Does htflow preserve layout fidelity well enough?
- Are the converted elements actually pleasant to edit in Webflow?
- Does Webflow Claude understand and modify the imported structure reliably?
- Is SEO metadata and JSON-LD manageable without becoming fragile?
- Does the workflow save time compared with keeping the HTML site in GitHub?

## Decision Rule

Keep Webflow if the import is editable, stable, and client-friendly after one homepage pilot and one service page pilot.

Keep GitHub + Cloudflare Pages if the Webflow import creates messy classes, weak mobile behavior, or too much manual cleanup.

