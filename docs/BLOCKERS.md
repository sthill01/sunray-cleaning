# Blockers

Last updated: 2026-07-03

## Immediate Blockers

- Cloudflare Managed Content / AI Crawl Control currently writes `robots.txt`
  rules that disallow several major AI crawlers, including GPTBot, ClaudeBot,
  Google-Extended, CCBot, Bytespider, and Applebot-Extended. Product Owner
  should decide whether Sun Ray wants these crawlers allowed for AI authority
  work, then update the Cloudflare setting or confirm that the restriction is
  intentional.
- Turno.com marketplace registration is a high-ROI external task from
  `SEO-90-PLUS-ACTION-PLAN.md`. Product Owner must create or verify the
  business profile. Codex can document and link the profile after the public
  profile URL exists.

## Recently Cleared

- The old custom-domain stale-cache blocker appears cleared. July 2 live probes
  showed priority pages on `www.sunray-cleaning.com` returning current
  production pages with canonical `www.sunray-cleaning.com` URLs and no
  `x-robots-tag` header in the checked responses.

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
