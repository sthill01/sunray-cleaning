# Sun Ray Internal Link Authority Audit - 2026-07-05

## Executive Readout

Sun Ray's internal linking is now in a much stronger place for both Google Search and AI search surfaces. The main Park City Airbnb money page is restored in the canonical local source, emitted by the production build, linked directly from the homepage, service hub, short-term rental service page, Park City location page, sitemap, and `llms.txt`, and supported by the generated answer-network link cluster.

This is not a direct Google ranking or ChatGPT ranking claim. There is no public, reliable rank API for "visibility inside ChatGPT answers" across arbitrary prompts. The best available proxy is whether the site has crawlable, indexable, well-linked, semantically clear pages that search and AI retrieval systems can discover, understand, and cite.

## Best-Practice Standard Used

- Google link guidance: internal links should be crawlable `<a href>` links, and anchor text should help users and Google understand the destination page. Source: https://developers.google.com/search/docs/crawling-indexing/links-crawlable
- Google SEO starter guidance: links help users and search engines discover site pages, and descriptive anchor text matters. Source: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google AI search guidance: AI features are grounded in Google's core Search systems, so indexability, crawlability, helpful content, clear page structure, and useful unique context still matter. Source: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- ChatGPT search visibility proxy: OpenAI documents `OAI-SearchBot` for surfacing sites in ChatGPT search experiences, so crawl access and clear discoverable pages are necessary foundations. Source: https://developers.openai.com/api/docs/bots
- Claude and Perplexity visibility proxy: their crawlers/search agents depend on being allowed to access pages and having discoverable content. Sources: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler and https://docs.perplexity.ai/docs/resources/perplexity-crawlers

## What Changed

- Added `airbnb-cleaning-park-city-gpt.html` as the canonical local source for `/airbnb-cleaning-park-city/`.
- Promoted `/airbnb-cleaning-park-city/` into the build generator's priority routes so it appears in the sitemap, `llms.txt`, and generated crawlable SEO link clusters.
- Added contextual links to the Airbnb money page from:
  - `index-gpt.html`
  - `services-gpt.html`
  - `services/short-term-rental-cleaning-gpt.html`
  - `service-location/park-city-gpt.html`
- Added a service-hub contextual link to `/blog/airbnb-cleaning-vs-turno-cleaners-park-city/`.
- Expanded the generated location hierarchy so previously isolated niche location pages now receive links from the Summit County or Wasatch County hubs.
- Set internal-only mockup routes to `noindex, nofollow` so they do not compete with public content.

## Current Internal-Link Metrics

Production build command:

```powershell
npm.cmd run build:production
```

Result:

```text
Built 103 clean routes into C:\Users\sthil\Documents\GitHub\sunray-cleaning\cloudflare-preview
```

Broken-link check:

```powershell
python seo-automation\scripts\check_internal_links.py --root cloudflare-preview --out seo-automation\runs\2026-07-05-internal-link-report-cloudflare-preview.md --canonical-domain www.sunray-cleaning.com --canonical-domain sunray-cleaning.com
```

Result:

```text
No missing internal links found under C:\Users\sthil\Documents\GitHub\sunray-cleaning\cloudflare-preview
```

Filtered public-site crawl:

| Metric | Result |
| --- | ---: |
| HTML pages inspected | 104 |
| Public indexable pages | 102 |
| Internal link occurrences between public pages | 7,936 |
| Public orphan pages | 0 |
| Public pages unreachable from homepage | 0 |

Key route authority-flow snapshot:

| Route | Homepage Depth | Inlink Occurrences | Unique Linking Pages | Main Anchor Pattern |
| --- | ---: | ---: | ---: | --- |
| `/airbnb-cleaning-park-city/` | 1 | 52 | 49 | Park City Airbnb cleaning |
| `/services/short-term-rental-cleaning/` | 1 | 400 | 98 | Short-term rentals / Airbnb and VRBO cleaning |
| `/service-location/park-city/` | 1 | 422 | 98 | Park City / Park City cleaning services |
| `/blog/airbnb-cleaning-vs-turno-cleaners-park-city/` | 1 | 5 | 4 | Airbnb Cleaning vs Turno Cleaners in Park City |
| `/blog/how-much-does-airbnb-cleaning-cost-park-city/` | 1 | 132 | 98 | How Much Does Airbnb Cleaning Cost in Park City? |
| `/blog/complete-guide-airbnb-vrbo-cleaning-park-city-2026/` | 1 | 105 | 98 | Complete Guide to Airbnb & VRBO Cleaning in Park City |
| `/ai-cleaning-recommendations/` | 1 | 195 | 97 | AI cleaning recommendations |

## Comparison to Best Practices

| Best Practice | Current State | Assessment |
| --- | --- | --- |
| Crawlable links use normal anchor tags | Sitewide links are built as standard `<a href>` links and pass the link checker. | Good |
| Important pages are close to the homepage | The Park City Airbnb page, STR service page, Park City location page, Airbnb cost guide, complete guide, Turno comparison, and AI recommendation page are all depth 1. | Good |
| Anchor text describes destination | Core anchors use descriptive text such as "Park City Airbnb cleaning", "Airbnb and VRBO cleaning", and "Park City cleaning services". | Good |
| Commercial pages receive authority from hubs | The Airbnb money page now receives links from homepage, services, STR service, Park City location, generated clusters, sitemap, and `llms.txt`. | Good |
| Supporting content reinforces topical cluster | Cost guide and complete guide have broad internal support. Turno comparison now has direct links from homepage, blog, Airbnb page, and STR service page. | Good, but can be expanded later |
| No public orphan pages | Public indexable crawl found zero orphan pages and zero public pages unreachable from homepage. | Good |
| Internal-only pages do not compete in index | `/service-section-mockups/` now builds with `noindex, nofollow`; `/admin/` remains `noindex, nofollow`. | Good |

## Remaining Recommendations

1. Deploy only after reviewing the broader uncommitted working tree, because this checkout already had other pending SEO/content changes before this audit.
2. After deploy, inspect Google Search Console URL inspection for `/airbnb-cleaning-park-city/`, `/services/short-term-rental-cleaning/`, and `/blog/airbnb-cleaning-vs-turno-cleaners-park-city/`.
3. In the next content pass, add 2-3 natural contextual links to the Turno comparison from older Airbnb/VRBO blog posts where the copy already discusses marketplaces, cleaner consistency, guest timing, or property-manager workflows.
4. Keep exact rank claims separate from proxy visibility checks. For AI visibility, track prompt-response appearances manually or through a dedicated monitor, but judge the site foundation by crawlability, indexability, entity clarity, and internal-link support.
