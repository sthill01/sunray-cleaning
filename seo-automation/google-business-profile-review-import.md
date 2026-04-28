# Google Business Profile Review Import Automation

This automation imports Sun Ray Cleaning reviews from the official Google Business Profile Reviews API into `data/reviews.json`, then the Cloudflare build renders review cards, aggregate-rating schema, individual review schema, and reviewer profile photos when Google provides them.

## What It Imports

- `averageRating` and `totalReviewCount`
- review ID, text, star rating, create/update timestamps
- reviewer display name when the reviewer is not anonymous
- reviewer profile photo URL when Google returns one
- owner reply text and review media metadata when available

## What It Does Not Do

- It does not scrape Google Maps.
- It does not invent review text.
- It does not reveal anonymous reviewer names or photos.
- It does not download/profile-cache reviewer photos; it references the public URL returned by Google.

## Required Secrets

Set these in GitHub Actions secrets or local environment variables:

- `GBP_ACCOUNT_ID`
- `GBP_LOCATION_ID`
- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `GOOGLE_REFRESH_TOKEN`

Optional:

- `GBP_PROFILE_URL`
- `GBP_FEATURED_REVIEW_LIMIT`, default `12`
- `GBP_FEATURED_MIN_RATING`, default `5`
- `GBP_MAX_PAGES`, default `5`

## Commands

Local import:

```bash
npm run import:google-reviews
```

Rebuild clean Cloudflare preview:

```bash
npm run build:cloudflare
```

## Scheduled Automation

The GitHub Actions workflow at `.github/workflows/import-google-reviews.yml` runs daily and can also be run manually. It imports reviews, rebuilds the Cloudflare preview, and commits changed `data/reviews.json` plus generated preview files.

## Source Docs Checked

- Google Business Profile Reviews list endpoint: retrieves verified-location reviews with pagination, average rating, total review count, and OAuth business-management scopes.
- Google Business Profile Review resource: includes reviewer display name/profile photo only when the reviewer is not anonymous, plus comment, star rating, timestamps, reply, and review media items.
