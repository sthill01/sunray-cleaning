# Blockers

Last updated: 2026-06-30

## Immediate Blockers

- Cloudflare zone cache for `www.sunray-cleaning.com` is serving an older
  preview-style artifact with `x-robots-tag: noindex, follow` and preview-domain
  canonicals even after a successful production Pages deployment. The local
  Wrangler token can list the zone but does not have permission to purge cache
  through the Cloudflare API. Product Owner should purge Cloudflare cache for
  `sunray-cleaning.com` or provide a Cloudflare API token with Zone Cache Purge
  permission.

## External Items To Confirm Later

These are not blocking the current sprint, but they may block future automation
or measurement work:

- Google Search Console property verification.
- GA4 property ID and measurement setup confirmation.
- Cloudflare API token for deployment automation and zone cache purge.
- Google Business Profile API credentials for live review import.
- Meta credentials for ongoing social gallery import.
- Final business confirmation of service areas, business hours, and any service
  exclusions.
- Approval process for sensitive customer-facing claims.

## Rule

Codex should write blockers here instead of interrupting the Product Owner
unless the blocker prevents all meaningful progress.
