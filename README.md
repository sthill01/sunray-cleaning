# Sun Ray Cleaning Static Website

Static staging build for Sun Ray Cleaning Services.

## Pages

- `index.html`
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
