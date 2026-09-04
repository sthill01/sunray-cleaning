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
- Optional Google Sheets export webhook variable: `SUNRAY_QUOTE_SHEETS_WEBHOOK_URL`
- Optional filtered-spam audit webhook variable: `SUNRAY_QUOTE_SPAM_WEBHOOK_URL`
- Optional comma-separated quote recipients: `SUNRAY_QUOTE_TO_EMAILS`
- Optional Pushover credentials: `SUNRAY_PUSHOVER_APP_TOKEN` and `SUNRAY_PUSHOVER_GROUP_KEY`
- Optional Brevo SMS configuration: `BREVO_API_KEY` and `BREVO_SMS_SENDER`

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
- Required delivery configuration for quote forwarding: Resend, Pushover, Brevo SMS, or a quote webhook
- Optional comma-separated quote recipients: `SUNRAY_QUOTE_TO_EMAILS`
- Optional Pushover credentials: `SUNRAY_PUSHOVER_APP_TOKEN` and `SUNRAY_PUSHOVER_GROUP_KEY`
- Optional Brevo SMS configuration: `BREVO_API_KEY` and `BREVO_SMS_SENDER`
- Optional Google Sheets export webhook variable: `SUNRAY_QUOTE_SHEETS_WEBHOOK_URL`
- Optional filtered-spam audit webhook variable: `SUNRAY_QUOTE_SPAM_WEBHOOK_URL`
- Google Tag Manager container: `GTM-W78H8S3C`

The production build sets crawlable robots metadata, removes the preview `X-Robots-Tag: noindex` header, writes a crawlable `robots.txt`, and generates sitemap/canonical URLs for `https://www.sunray-cleaning.com`. Attach `www.sunray-cleaning.com` as the primary Cloudflare Pages custom domain and redirect `sunray-cleaning.com` to `www.sunray-cleaning.com`.

## Quote form routing

Cloudflare preview forms post to `/api/quote`. The form forwards valid submissions through the configured delivery paths:

- `RESEND_API_KEY` sends the quote notification email.
- `SUNRAY_QUOTE_TO_EMAILS` accepts comma-, semicolon-, or newline-separated recipients. Without an override, legitimate leads email `quotes@sunray-cleaning.com`, `cyntya@sunray-cleaning.com`, `cyntyahill@gmail.com`, `sunrayservices17@gmail.com`, and `sthill01@gmail.com`.
- `SUNRAY_PUSHOVER_APP_TOKEN` and `SUNRAY_PUSHOVER_GROUP_KEY` send a high-priority Pushover alert to the Sun Ray delivery group. Use `SUNRAY_PUSHOVER_PRIORITY` and `SUNRAY_PUSHOVER_SOUND` to override the defaults of `1` and `cashregister`.
- `BREVO_API_KEY` and `BREVO_SMS_SENDER` send the same ordered alert through Brevo Transactional SMS. `SUNRAY_SMS_TO_NUMBERS` optionally accepts comma-, semicolon-, or newline-separated E.164 numbers; it defaults to Cynthia at `+18016042189` and Steve at `+18018501253`.
- `SUNRAY_QUOTE_WEBHOOK_URL` sends the full JSON payload to CRM or automation.
- `SUNRAY_QUOTE_SHEETS_WEBHOOK_URL` sends the same JSON payload to the Google Sheets lead log webhook.
- `SUNRAY_QUOTE_SPAM_WEBHOOK_URL` sends filtered spam to an audit webhook without emailing, notifying sales, or firing conversion tracking.

Webhook delivery is additive, so a Sheets export can run alongside inbox notifications.
The Sheets target must acknowledge JSON `{ "ok": true, "leadId": "..." }`; a plain 2xx response or `{ "ok": false }` is treated as failure and retried once with the same Lead ID. If email, push, SMS, or another webhook delivered the lead but Sheets still failed, the form remains successful and returns `sheetRecorded: false` so logs and monitoring do not claim ledger durability.

Pushover setup:

1. Install Pushover on each phone and activate each user's license.
2. Register a `Sun Ray Leads` Pushover application and copy its API token.
3. Create a delivery group containing each Sun Ray recipient and copy the group key.
4. Store the token and group key in the Cloudflare project as encrypted secrets named `SUNRAY_PUSHOVER_APP_TOKEN` and `SUNRAY_PUSHOVER_GROUP_KEY`.
5. Submit one labeled test lead and verify delivery to the five configured email recipients, the `Leads` row, and the group push. Submit a honeypot test separately and verify that it appears only in `Filtered Spam`.

The notification paths run only after the quote passes the spam checks. Filtered submissions never call Resend, Pushover, or Brevo.

Quote payloads retain their server-generated UTC `submittedAt` value and immutable `leadId` for webhook, spreadsheet, and conversion reconciliation. Email notifications display the timestamp in `America/Denver` Mountain Time, including the correct `MST` or `MDT` daylight-saving abbreviation. The Sheets template stores `Submitted At` as a native date, preserves the raw UTC ISO value, and adds Mountain-time timestamp, date, and time columns for analysis.

The phone alert message begins with `New website lead`, followed by name, phone, email, service, UTM source, location, and notes in that exact order. Pushover delivers this as an app notification to its delivery group. When Brevo credentials are configured, the same content is sent as carrier SMS to Cynthia at `+1 801-604-2189` and Steve at `+1 801-850-1253` by default.

Brevo SMS setup:

1. In Brevo, buy SMS credits and complete the required US toll-free-number registration. Wait until the sender is approved before treating SMS as available.
2. Open `SMTP & API` in Brevo settings and create an API key for the website integration.
3. Store the API key in Cloudflare as the encrypted secret `BREVO_API_KEY`. Do not commit it or paste it into issue/chat history.
4. Set `BREVO_SMS_SENDER` to the approved Brevo Sender ID or toll-free sender value associated with the account.
5. Optionally set `SUNRAY_SMS_TO_NUMBERS` when more recipients are needed. Use full E.164 numbers such as `+18016042189`.
6. Submit one labeled test lead and confirm both Brevo transactional logs and delivery on each recipient phone before treating SMS as live.

Long alert text can be billed as multiple SMS message parts. Keep form notes concise where possible.

If all delivery paths are missing or unavailable, the form shows an error and keeps the phone/SMS fallback visible: `(801) 604-2189`.

The runtime quote script captures `gclid`, `gbraid`, `wbraid`, `msclkid`, `fbclid`, `ttclid`, `li_fat_id`, UTM fields, and the explicit ValueTrack fields `campaign_id`, `ad_group_id`, `asset_group_id`, `creative_id`, `match_type`, `network`, and `device`. Attribution is retained for 90 days, tagged with a browser-session ID, and stored as separate first-touch and latest-touch values. A new tagged click replaces the complete latest-touch marketing set so missing parameters cannot inherit stale values from an earlier campaign.

The Google Sheets Apps Script template lives at `integrations/google-sheets-lead-webhook.gs`. Before deployment, replace `SET_IN_DEPLOYED_CODE_GS` with the target spreadsheet ID in the private Apps Script editor; do not commit the live ID. Run `setupLeadSheets()` once to create or extend headers without rewriting existing columns, then deploy the script as a web app and save the `/exec` URL as `SUNRAY_QUOTE_SHEETS_WEBHOOK_URL` in Cloudflare. A side-effect-free `GET` to the deployment reports the schema and whether the target sheet exists. Lead writes are locked and deduplicated by Lead ID, with a 10-minute normalized contact/detail fingerprint as a secondary guard.

Filtered spam is blocked from normal delivery but can be audited. Paste the updated Apps Script template, redeploy the Apps Script web app, then save the same `/exec` URL as `SUNRAY_QUOTE_SPAM_WEBHOOK_URL` in Cloudflare. The script routes new normal leads to the canonical `Lead Ledger` tab and filtered spam to `Filtered Spam` with score, reasons and a review note; the legacy `Leads` tab and its historical rows remain untouched.

## Google Tag Manager conversion tracking

The Cloudflare Pages build injects GTM sitewide from `tools/build-cloudflare-preview.py`. The runtime quote/CTA script pushes `dataLayer` events for quote opens, call clicks, text clicks, submit clicks, and successful lead form submissions. Keep GA4 and Google Ads conversion tags inside GTM so reporting and conversion changes can be managed in one place.

Setup details are in `tracking/google-tag-manager-conversions.md`.

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

## Instagram and Facebook photo import

The Meta photo importer downloads approved Sun Ray Instagram/Facebook images into `assets/social/`, writes local SEO metadata to `data/social-gallery.json`, and lets the build reuse those photos in gallery sections and image schema.

```powershell
npm run import:social-gallery -- --source=all --limit=24
npm run build:cloudflare
```

Setup details are in `social-gallery-import.md`.

GitHub Actions can also run the importer from the repo after these Actions secrets are saved:

- `META_ACCESS_TOKEN`
- `INSTAGRAM_BUSINESS_ACCOUNT_ID`
- `FACEBOOK_PAGE_ID`

Run **Actions > Import Instagram and Facebook Gallery Photos** to import draft photos, then approve selected records in `data/social-gallery.json`.

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
