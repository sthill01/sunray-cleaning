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

The generated preview intentionally uses `noindex` headers and robots rules until it is promoted from preview to production.

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

- `index.html`
- `about.html`
- `services.html`
- `service-location/park-city.html`
- `service-location/heber-city.html`
- `service-location/midway.html`
- `service-location/salt-lake-county.html`
- `services/short-term-rental-cleaning.html`
- `services/deep-cleaning.html`
- `services/recurring-cleaning.html`
- `services/move-in-move-out-cleaning.html`

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
