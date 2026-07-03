# AI Monitoring

Last updated: 2026-07-03

AI monitoring is not yet automated. Until it is, record manual checks here.

## Prompt Log Template

| Date | Platform | Prompt | Sun Ray Mentioned | Position | Competitors | Notes | Follow-Up |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Baseline Prompts

- Best cleaning company in Park City.
- Best house cleaner in Heber City.
- Airbnb cleaning Park City.
- Luxury cleaning Deer Valley.
- Move-out cleaning Midway.
- Deep cleaning Park City.
- Recurring house cleaning Wasatch County.
- Vacation rental cleaning Canyons Village.

## Baseline Run 001

Status: blocked until the live custom-domain Cloudflare Managed `robots.txt`
block is removed or updated.

Date window: first production check after `www.sunray-cleaning.com` serves the
current indexed Cloudflare Pages artifact, the live custom-domain `robots.txt`
does not prepend AI-crawler disallow rules, and AI crawler access remains open
in Cloudflare AI Crawl Control.

Platforms:

- ChatGPT.
- Claude.
- Gemini.
- Grok.
- Perplexity.
- Google AI Overviews when available from a normal Google search result.

Prompts:

- "Best cleaning company in Park City"
- "Best house cleaner in Heber City"
- "Airbnb cleaning Park City"
- "Luxury cleaning Deer Valley"
- "Move-out cleaning Midway"
- "Deep cleaning Park City"
- "Recurring house cleaning Wasatch County"
- "Vacation rental cleaning Canyons Village"

Capture for each result:

- Whether Sun Ray Cleaning Services appears.
- Approximate position when a ranked list is shown.
- Competitors mentioned.
- Source pages or citations shown.
- Whether the answer cites or echoes `sunray-cleaning.com`.
- Missing facts or weak entity associations to feed into the backlog.

## Baseline Results

No current baseline recorded in the repo.

## Crawler Access Baseline

July 3 Cloudflare AI Crawl Control screenshots showed visible allowed activity
for Claude-SearchBot, ChatGPT-User, Googlebot, and OAI-SearchBot, but the live
custom-domain `robots.txt` later showed Cloudflare Managed Content still
prepending explicit `Disallow: /` groups for GPTBot, ClaudeBot,
Google-Extended, CCBot, Bytespider, Applebot-Extended, Amazonbot, and Meta
crawlers. The repo-generated production `robots.txt` allows priority AI and
search crawlers, and the fresh Pages deployment URL serves that file correctly;
the remaining issue is the Cloudflare managed layer on the custom domain.

Before running Baseline Run 001, recheck:

- Cloudflare Managed `robots.txt` is disabled or updated so the custom domain
  does not prepend AI-crawler disallow rules.
- Cloudflare AI Crawl Control over 24-hour and 7-day windows.
- Live `https://www.sunray-cleaning.com/robots.txt`.
- Whether GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot,
  PerplexityBot, and Googlebot are allowed or blocked.

## Monitoring Rule

Do not claim AI ranking improvements without logged tests, dates, prompts, and
observed outputs.
