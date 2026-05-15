# Sun Ray Instagram and Facebook Gallery Import

This repo now supports an official Meta Graph API import path for Sun Ray social photos. It does not scrape Instagram or Facebook.

## Manual job-photo gallery batch

The May 2026 uploaded job-photo batch is staged in two website/social-ready locations:

- Website gallery images: `assets/job-gallery-2026-05/`
- Social crops: `assets/social-ready-2026-05/square/` and `assets/social-ready-2026-05/portrait/`
- Website metadata and local SEO schema source: `data/job-gallery.json`
- Draft Facebook, Instagram, and Google Business Profile posting queue: `data/photo-post-queue.json`

Keep new real-job photos as drafts first. Review each photo for privacy, customer approval, room/service/location accuracy, and caption quality before publishing it on the website or pushing it to Facebook, Instagram, or Google Business Profile.

## What the importer does

- Pulls recent Instagram business media and Facebook Page uploaded photos.
- Downloads image files into `assets/social/` with local SEO filenames.
- Writes approval-ready records to `data/social-gallery.json`.
- Adds inferred local SEO metadata: room, cleaning service, city, county, alt text, captions, keywords, and page routes.
- Publishes only records with `"approved": true`.
- Reuses the existing gallery and `ImageObject` schema pipeline during `npm run build:cloudflare`.

## Meta setup

1. Confirm `@sunraycleaningservices` is an Instagram Business or Creator account.
2. Confirm that Instagram account is connected to the correct Facebook Page in Meta Business Suite.
3. Create or use a Meta Developers app for Sun Ray.
4. Add the Instagram and Facebook Graph/API products needed by the current Meta dashboard.
5. Generate a long-lived access token for a user or Page that can read the connected Instagram account and Facebook Page.
6. Use Graph API Explorer or the importer discovery command to identify:
   - `INSTAGRAM_BUSINESS_ACCOUNT_ID`
   - `FACEBOOK_PAGE_ID`

Meta permission names change by product path. For this use case, the token must be able to read your own Instagram business media and Facebook Page photos. In current Meta setups this commonly involves Instagram business basic/media access plus Page list/read engagement access. The practical test is whether these endpoints work for your app token:

- `/{INSTAGRAM_BUSINESS_ACCOUNT_ID}/media?fields=id,caption,media_type,media_url,permalink,timestamp`
- `/{FACEBOOK_PAGE_ID}/photos?type=uploaded&fields=id,created_time,name,link,images`

Official references:

- Instagram Platform docs: https://developers.facebook.com/docs/instagram-platform/
- Graph API Page photos reference: https://developers.facebook.com/docs/graph-api/reference/page/photos/
- Meta Basic Display deprecation notice: https://developers.facebook.com/blog/post/2024/09/04/update-on-instagram-basic-display-api/

## Local environment variables

Put secrets in `.env`, `.dev.vars`, Cloudflare secrets, or your terminal session. Do not commit tokens.

```powershell
$env:META_ACCESS_TOKEN="your-long-lived-meta-token"
$env:INSTAGRAM_BUSINESS_ACCOUNT_ID="your-instagram-business-account-id"
$env:FACEBOOK_PAGE_ID="your-facebook-page-id"
```

Optional:

```powershell
$env:META_GRAPH_VERSION="v24.0"
$env:SOCIAL_GALLERY_ALLOW_PARTIAL="1"
$env:SOCIAL_GALLERY_DEFAULT_CITY="Park City"
$env:SOCIAL_GALLERY_DEFAULT_COUNTY="Summit County"
$env:SOCIAL_GALLERY_DEFAULT_REGION="Utah"
```

## Commands

Discover connected Pages and Instagram accounts:

```powershell
npm run import:social-gallery -- --discover
```

Import recent Instagram and Facebook photos as drafts:

```powershell
npm run import:social-gallery -- --source=all --limit=24
```

Import Instagram only:

```powershell
npm run import:social-gallery -- --source=instagram --limit=24
```

Import Facebook Page photos only:

```powershell
npm run import:social-gallery -- --source=facebook --limit=24
```

If you want newly imported photos to publish immediately:

```powershell
npm run import:social-gallery -- --source=all --limit=24 --approve
```

## Approval workflow

1. Open `data/social-gallery.json`.
2. Review each imported item.
3. Edit `room`, `service`, `location`, `city`, `county`, `alt`, `caption`, `keywords`, and `routes` if needed.
4. Set `"approved": true` only for photos you want on the website.
5. Run:

```powershell
npm run build:cloudflare
```

The approved photos appear in the same local photo gallery sections and structured data as the existing curated job photos.

## GitHub workflow

After the secrets are saved in GitHub, you can run the import without opening VS Code:

1. Go to the GitHub repo.
2. Open **Settings > Secrets and variables > Actions**.
3. Add these repository secrets:
   - `META_ACCESS_TOKEN`
   - `INSTAGRAM_BUSINESS_ACCOUNT_ID`
   - `FACEBOOK_PAGE_ID`
4. Optional, if you use separate tokens:
   - `INSTAGRAM_ACCESS_TOKEN`
   - `FACEBOOK_PAGE_ACCESS_TOKEN`
5. Open **Actions > Import Instagram and Facebook Gallery Photos**.
6. Click **Run workflow**.
7. Choose `all`, `instagram`, or `facebook`.
8. Keep `approve` off for the first run so imported photos are saved as drafts.

The workflow commits updates to `data/social-gallery.json` and `assets/social/`. Cloudflare Pages can then deploy from the GitHub branch using the repo build command:

```text
npm run build:cloudflare
```

If the workflow says `Object with ID ... does not exist, cannot be loaded due to missing permissions`, regenerate the Meta token from Graph API Explorer with the Sun Ray app selected and these permissions: `pages_show_list`, `pages_read_engagement`, `instagram_basic`, and `business_management` if available. The importer can use `META_ACCESS_TOKEN` to discover the Page access token from `/me/accounts`, but the token still needs permission to see the Sun Ray Page and its connected Instagram business account.

If Instagram media fails but Facebook media works, run the workflow with `source=facebook` to validate the site pipeline while you fix the Instagram permission. To test Instagram directly in Graph API Explorer, use:

```text
17841474426769699/media?fields=id,caption,media_type,media_url,permalink,timestamp
```
