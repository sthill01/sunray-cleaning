# Blockers

Last updated: 2026-07-03

## Immediate Blockers

- Turno.com marketplace registration is a high-ROI external task from
  `SEO-90-PLUS-ACTION-PLAN.md`. Product Owner must create or verify the
  business profile. Codex can document and link the profile after the public
  profile URL exists.
- Cloudflare Managed `robots.txt` is still prepending a managed AI-crawler
  block on the custom domain. The repo-generated production `robots.txt` allows
  GPTBot, ChatGPT-User, OAI-SearchBot, ClaudeBot, Claude-SearchBot,
  PerplexityBot, Googlebot, and Google-Extended, and the fresh Pages deployment
  URL serves that file correctly. However, `https://www.sunray-cleaning.com/robots.txt`
  still includes Cloudflare Managed Content above the repo file with explicit
  `Disallow: /` groups for GPTBot, ClaudeBot, Google-Extended, CCBot,
  Bytespider, Applebot-Extended, Amazonbot, and Meta crawlers. This must be
  changed in Cloudflare AI Crawl Control / Managed `robots.txt` before Baseline
  Run 001 can treat AI crawler access as open.

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
- Cloudflare AI Crawl Control and live `robots.txt` should be rechecked after
  the managed `robots.txt` block is removed, then again over 24-hour and 7-day
  windows before recording Baseline Run 001.

## Rule

Codex should write blockers here instead of interrupting the Product Owner
unless the blocker prevents all meaningful progress.
