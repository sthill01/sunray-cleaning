# AI Monitoring

Last updated: 2026-06-30

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

Status: ready to run after the custom-domain cache blocker is cleared.

Date window: first production check after `www.sunray-cleaning.com` serves the
current indexed Cloudflare Pages artifact.

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

## Monitoring Rule

Do not claim AI ranking improvements without logged tests, dates, prompts, and
observed outputs.
