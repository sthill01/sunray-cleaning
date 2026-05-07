# Sun Ray Cleaning Static Website

Static staging build for Sun Ray Cleaning Services.

## Cloudflare preview build

This repo now includes a Cloudflare-ready preview build pipeline. Source pages use the GPT-suffixed static preview files, then the build script generates clean extensionless URLs into `cloudflare-preview/`.

```powershell
npm install
npm run build:cloudflare
```

Cloudflare Pages settings:

- Build command: `npm run build:cloudflare`
- Build output directory: `cloudflare-preview`
- Preview project name: `sunray-cleaning-preview`
- Quote form webhook variable: `SUNRAY_QUOTE_WEBHOOK_URL`

The generated preview intentionally uses `noindex` headers and robots rules until it is promoted from preview to production.

## Cloudflare production launch build

Use the production build only for the live Cloudflare Pages project after QA passes:

```powershell
npm run build:production
```

Production Cloudflare Pages settings:

- Build command: `npm run build:production`
- Build output directory: `cloudflare-preview`
- Production canonical base URL: `https://www.sunray-cleaning.com`
- Required environment variable for quote forwarding: `SUNRAY_QUOTE_WEBHOOK_URL`

The production build sets crawlable robots metadata, removes the preview `X-Robots-Tag: noindex` header, writes a crawlable `robots.txt`, and generates sitemap/canonical URLs for `https://www.sunray-cleaning.com`. Attach `www.sunray-cleaning.com` as the primary Cloudflare Pages custom domain and redirect `sunray-cleaning.com` to `www.sunray-cleaning.com`.

## Quote form routing

Cloudflare preview forms post to `/api/quote`. The form only forwards submissions to email/CRM automation after `SUNRAY_QUOTE_WEBHOOK_URL` is added in Cloudflare Pages environment variables. Use a Make or Zapier webhook that sends the submitted JSON payload to the preferred Sun Ray email inbox.

If the webhook is missing or unavailable, the form shows an error and keeps the phone/SMS fallback visible: `(801) 604-2189`.

## Google review automation

The Google Business Profile review importer updates `data/reviews.json` and the build renders aggregate-rating schema, review cards, reviewer photos when available, and local trust sections.

```powershell
npm run import:google-reviews
```

Required GitHub Actions secrets:

- `GBP_ACCOUNT_ID`
- `GBP_LOCATION_ID`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`

Optional:

- `GBP_PROFILE_URL`

## Pages

- `/`
- `/about/`
- `/services/`
- `/specials/`
- `/discounts/`
- `/service-areas/`
- `/service-location/park-city/`
- `/service-location/snyderville/`
- `/service-location/deer-valley/`
- `/service-location/canyons-village/`
- `/service-location/old-town-park-city/`
- `/service-location/heber-city/`
- `/service-location/midway/`
- `/service-location/kamas/`
- `/service-location/oakley/`
- `/service-location/daniel/`
- `/service-location/coalville/`
- `/service-location/summit-county/`
- `/service-location/wasatch-county/`
- `/services/short-term-rental-cleaning/`
- `/services/deep-cleaning/`
- `/services/recurring-cleaning/`
- `/services/move-in-move-out-cleaning/`

`/service-location/old-town/` is a legacy Cloudflare redirect alias for `/service-location/old-town-park-city/`.

## Cloudflare Pages staging

Recommended Pages project name:

```powershell
sunray-cleaning-staging
```

Direct upload preview deployment:

```powershell
cmd /c npx wrangler pages project create sunray-cleaning-staging --production-branch=main
cmd /c npx wrangler pages deploy . --project-name=sunray-cleaning-staging --branch=staging
```

Wrangler must be authenticated first:

```powershell
cmd /c npx wrangler login
```

The preview URL will use this pattern:

```text
staging.sunray-cleaning-staging.pages.dev
```
