#!/usr/bin/env node

const GRAPH_VERSION = process.env.META_GRAPH_VERSION || "v24.0";
const GRAPH_BASE = `https://graph.facebook.com/${GRAPH_VERSION}`;
const OUTPUT_PATH = "data/social-gallery.json";
const ASSET_DIR = "assets/social";
const DEFAULT_LIMIT = 24;

function argValue(name, fallback = "") {
  const prefix = `--${name}=`;
  const match = process.argv.find((arg) => arg.startsWith(prefix));
  return match ? match.slice(prefix.length) : fallback;
}

function hasFlag(name) {
  return process.argv.includes(`--${name}`);
}

function printHelp() {
  console.log(`
Import Sun Ray Instagram and Facebook photos into a local approval gallery.

Usage:
  npm run import:social-gallery -- --source=all --limit=24
  npm run import:social-gallery -- --discover

Required for import:
  META_ACCESS_TOKEN or INSTAGRAM_ACCESS_TOKEN / FACEBOOK_PAGE_ACCESS_TOKEN

Instagram import:
  INSTAGRAM_BUSINESS_ACCOUNT_ID

Facebook Page photo import:
  FACEBOOK_PAGE_ID

Optional:
  META_GRAPH_VERSION=v24.0
  SOCIAL_GALLERY_ALLOW_PARTIAL=1
  SOCIAL_GALLERY_APPROVED=1
  SOCIAL_GALLERY_DEFAULT_CITY=Park City
  SOCIAL_GALLERY_DEFAULT_COUNTY=Summit County
  SOCIAL_GALLERY_DEFAULT_REGION=Utah

Notes:
  Imported records are written to ${OUTPUT_PATH}.
  Images are downloaded into ${ASSET_DIR}/ with SEO filenames.
  New photos default to approved=false unless --approve or SOCIAL_GALLERY_APPROVED=1 is used.
  When importing --source=all, SOCIAL_GALLERY_ALLOW_PARTIAL=1 lets Facebook photos import even if Instagram needs another permission fix.
`);
}

function required(name) {
  const value = process.env[name];
  if (!value) throw new Error(`Missing required environment variable: ${name}`);
  return value;
}

function optionalNumber(name, fallback, { min = 1, max = Number.POSITIVE_INFINITY } = {}) {
  const raw = argValue(name.toLowerCase().replaceAll("_", "-"), process.env[name] || "");
  if (!raw) return fallback;
  const value = Number(raw);
  if (!Number.isFinite(value) || value < min) {
    throw new Error(`${name} must be a number greater than or equal to ${min}.`);
  }
  return Math.min(value, max);
}

function cleanText(value = "") {
  return String(value).replace(/\s+/g, " ").trim();
}

function slugify(value) {
  return cleanText(value)
    .toLowerCase()
    .replace(/&/g, " and ")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 120);
}

function shortId(value) {
  return String(value).replace(/[^a-zA-Z0-9]/g, "").slice(-8) || "photo";
}

function extensionForContentType(contentType = "") {
  if (contentType.includes("png")) return "png";
  if (contentType.includes("webp")) return "webp";
  return "jpg";
}

function pickLargestFacebookImage(images = []) {
  return [...images].sort((left, right) => {
    const leftPixels = Number(left.width || 0) * Number(left.height || 0);
    const rightPixels = Number(right.width || 0) * Number(right.height || 0);
    return rightPixels - leftPixels;
  })[0];
}

function maskedId(value) {
  const text = String(value || "");
  if (text.length <= 6) return "***";
  return `${text.slice(0, 3)}...${text.slice(-3)}`;
}

async function fetchJson(url, token, context = "Meta Graph API request") {
  const response = await fetch(url, {
    headers: { authorization: `Bearer ${token}` },
  });
  if (!response.ok) {
    throw new Error(`${context} failed: ${response.status} ${await response.text()}`);
  }
  return response.json();
}

async function discoverMetaAssets(token) {
  const fields = "id,name,access_token,instagram_business_account{id,username,name}";
  const url = `${GRAPH_BASE}/me/accounts?${new URLSearchParams({ fields, limit: "50" })}`;
  const payload = await fetchJson(url, token, "Discover Facebook Pages and connected Instagram accounts");
  const pages = payload.data ?? [];
  if (!pages.length) {
    console.log("No Facebook Pages returned for this token.");
    return;
  }
  for (const page of pages) {
    console.log(`Facebook Page: ${page.name} (${page.id})`);
    if (page.instagram_business_account?.id) {
      console.log(`  Instagram business account: @${page.instagram_business_account.username || "unknown"} (${page.instagram_business_account.id})`);
    }
  }
}

async function pageAccessTokenFor({ userToken, pageId }) {
  if (!userToken || !pageId) return "";
  const fields = "id,name,access_token,instagram_business_account{id,username,name}";
  const url = `${GRAPH_BASE}/me/accounts?${new URLSearchParams({ fields, limit: "100" })}`;
  const payload = await fetchJson(url, userToken, "Find Page access token from /me/accounts");
  const page = (payload.data ?? []).find((item) => String(item.id) === String(pageId));
  return page?.access_token || "";
}

async function instagramAccountForPage({ token, pageId }) {
  if (!token || !pageId) return null;
  const fields = "instagram_business_account{id,username,name}";
  const url = `${GRAPH_BASE}/${pageId}?${new URLSearchParams({ fields })}`;
  const payload = await fetchJson(url, token, `Load connected Instagram account for Facebook Page ${maskedId(pageId)}`);
  return payload.instagram_business_account || null;
}

async function listInstagramMedia({ token, instagramId, limit }) {
  const fields = [
    "id",
    "caption",
    "media_type",
    "media_url",
    "thumbnail_url",
    "permalink",
    "timestamp",
    "username",
    "children{media_type,media_url,thumbnail_url,permalink}",
  ].join(",");
  const params = new URLSearchParams({ fields, limit: String(limit) });
  const payload = await fetchJson(
    `${GRAPH_BASE}/${instagramId}/media?${params}`,
    token,
    `Import Instagram media for IG business account ${maskedId(instagramId)}`
  );
  const photos = [];
  for (const media of payload.data ?? []) {
    if (media.media_type === "IMAGE") {
      photos.push({
        source: "Instagram",
        sourceId: media.id,
        sourceUrl: media.permalink || "",
        sourceMediaUrl: media.media_url || media.thumbnail_url || "",
        captionOriginal: cleanText(media.caption || ""),
        publishedAt: media.timestamp || "",
        username: media.username || "",
      });
    }
    if (media.media_type === "CAROUSEL_ALBUM") {
      for (const child of media.children?.data ?? []) {
        if (child.media_type === "IMAGE") {
          photos.push({
            source: "Instagram",
            sourceId: child.id,
            parentSourceId: media.id,
            sourceUrl: child.permalink || media.permalink || "",
            sourceMediaUrl: child.media_url || child.thumbnail_url || "",
            captionOriginal: cleanText(media.caption || ""),
            publishedAt: media.timestamp || "",
            username: media.username || "",
          });
        }
      }
    }
  }
  return photos.filter((photo) => photo.sourceMediaUrl);
}

async function listFacebookPhotos({ token, pageId, limit }) {
  const fields = "id,created_time,name,link,images,album{name},place";
  const params = new URLSearchParams({ type: "uploaded", fields, limit: String(limit) });
  const payload = await fetchJson(
    `${GRAPH_BASE}/${pageId}/photos?${params}`,
    token,
    `Import Facebook Page photos for Page ${maskedId(pageId)}`
  );
  return (payload.data ?? [])
    .map((photo) => {
      const image = pickLargestFacebookImage(photo.images ?? []);
      return {
        source: "Facebook",
        sourceId: photo.id,
        sourceUrl: photo.link || "",
        sourceMediaUrl: image?.source || "",
        captionOriginal: cleanText(photo.name || photo.album?.name || ""),
        publishedAt: photo.created_time || "",
        facebookPlaceName: photo.place?.name || "",
      };
    })
    .filter((photo) => photo.sourceMediaUrl);
}

function inferRoom(text) {
  const value = text.toLowerCase();
  if (/\b(kitchen|island|counter|stove|oven|sink|backsplash|pantry)\b/.test(value)) return "Kitchen";
  if (/\b(bathroom|bath|shower|tub|toilet|vanity|mirror)\b/.test(value)) return "Bathroom";
  if (/\b(bedroom|bed|bunk|linen|sheets)\b/.test(value)) return "Bedroom";
  if (/\b(living|family room|sofa|couch|fireplace|great room)\b/.test(value)) return "Living room";
  if (/\b(entry|mudroom|foyer|hallway)\b/.test(value)) return "Entry";
  if (/\b(laundry|washer|dryer)\b/.test(value)) return "Laundry room";
  return "Home";
}

function inferService(text) {
  const value = text.toLowerCase();
  if (/\b(airbnb|vrbo|short[- ]term|vacation rental|turnover|guest|checkout|check-in|rental)\b/.test(value)) return "Airbnb and VRBO turnover cleaning";
  if (/\b(move[- ]?in|move[- ]?out|moving)\b/.test(value)) return "Move-in and move-out cleaning";
  if (/\b(deep|detail|spring clean|seasonal|post[- ]ski|reset)\b/.test(value)) return "Deep cleaning";
  if (/\b(recurring|weekly|biweekly|monthly|maintenance)\b/.test(value)) return "Recurring residential cleaning";
  return "Residential house cleaning";
}

function inferLocation(text) {
  const value = text.toLowerCase();
  const region = process.env.SOCIAL_GALLERY_DEFAULT_REGION || "Utah";
  if (/\b(midway|homestead|interlaken)\b/.test(value)) {
    return { location: `Midway, ${region}`, city: "Midway", county: "Wasatch County", region };
  }
  if (/\b(heber|red ledges|timber lakes|charleston|daniels)\b/.test(value)) {
    return { location: `Heber City, ${region}`, city: "Heber City", county: "Wasatch County", region };
  }
  if (/\b(deer valley|canyons|old town|park meadows|prospector|silver springs|jeremy ranch|promontory|park city)\b/.test(value)) {
    return { location: `Park City, ${region}`, city: "Park City", county: "Summit County", region };
  }
  if (/\bsummit county\b/.test(value)) {
    return { location: `Summit County, ${region}`, city: "Park City", county: "Summit County", region };
  }
  if (/\bwasatch county\b/.test(value)) {
    return { location: `Wasatch County, ${region}`, city: "Heber City", county: "Wasatch County", region };
  }
  const city = process.env.SOCIAL_GALLERY_DEFAULT_CITY || "Park City";
  const county = process.env.SOCIAL_GALLERY_DEFAULT_COUNTY || (city === "Park City" ? "Summit County" : "Wasatch County");
  return { location: `${city}, ${region}`, city, county, region };
}

function routesFor({ service, city, county }) {
  const routes = new Set(["/"]);
  if (service.includes("Airbnb") || service.includes("VRBO")) routes.add("/services/short-term-rental-cleaning/");
  if (service.includes("Move-in")) routes.add("/services/move-in-move-out-cleaning/");
  if (service.includes("Deep")) routes.add("/services/deep-cleaning/");
  if (service.includes("Recurring")) routes.add("/services/recurring-cleaning/");
  if (service.includes("Residential")) routes.add("/services/recurring-cleaning/");
  if (city === "Park City") routes.add("/service-location/park-city/");
  if (city === "Heber City") routes.add("/service-location/heber-city/");
  if (city === "Midway") routes.add("/service-location/midway/");
  if (county === "Summit County") routes.add("/service-location/summit-county/");
  if (county === "Wasatch County") routes.add("/service-location/wasatch-county/");
  return [...routes];
}

function seoKeywords({ service, room, city, county }) {
  return [
    `${city} ${service}`.trim(),
    `${room} cleaning`.trim(),
    `${county} house cleaning`.trim(),
    "Sun Ray Cleaning Services photos",
  ];
}

function normalizeImportedPhoto(photo, existing, approvedByDefault) {
  const sourceText = `${photo.captionOriginal} ${photo.facebookPlaceName || ""}`;
  const room = existing?.room || inferRoom(sourceText);
  const service = existing?.service || inferService(sourceText);
  const location = inferLocation(sourceText);
  const publishedDate = photo.publishedAt ? photo.publishedAt.slice(0, 10) : new Date().toISOString().slice(0, 10);
  const basename = [
    slugify(location.city || location.county || "utah"),
    slugify(service),
    slugify(room),
    "sun-ray",
    slugify(photo.source),
    publishedDate,
    shortId(photo.sourceId),
  ].filter(Boolean).join("-");
  const asset = existing?.asset || `${ASSET_DIR}/${basename}.jpg`;
  const caption = existing?.caption || photo.captionOriginal || `${room} cleaning photo from Sun Ray Cleaning Services.`;
  return {
    id: `${photo.source.toLowerCase()}:${photo.sourceId}`,
    source: photo.source,
    sourceId: photo.sourceId,
    ...(photo.parentSourceId ? { parentSourceId: photo.parentSourceId } : {}),
    sourceUrl: photo.sourceUrl,
    captionOriginal: photo.captionOriginal,
    importedAt: existing?.importedAt || new Date().toISOString(),
    publishedAt: photo.publishedAt,
    asset,
    name: existing?.name || `${location.city || location.county} ${service} ${room} photo`,
    room,
    service,
    location: existing?.location || location.location,
    city: existing?.city || location.city,
    county: existing?.county || location.county,
    region: existing?.region || location.region,
    alt: existing?.alt || `${room} after ${service.toLowerCase()} by Sun Ray Cleaning Services in ${location.location}`,
    caption,
    keywords: existing?.keywords || seoKeywords({ service, room, city: location.city, county: location.county }),
    routes: existing?.routes || routesFor({ service, city: location.city, county: location.county }),
    approved: Boolean(existing?.approved ?? approvedByDefault),
    needsReview: existing?.needsReview ?? true,
  };
}

async function readJson(path, fallback) {
  const fs = await import("node:fs/promises");
  try {
    return JSON.parse(await fs.readFile(path, "utf8"));
  } catch (error) {
    if (error.code === "ENOENT") return fallback;
    throw error;
  }
}

async function downloadImage(url, assetPath) {
  const fs = await import("node:fs/promises");
  const path = await import("node:path");
  try {
    await fs.access(assetPath);
    return assetPath;
  } catch {
    // Continue to download.
  }
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error(`Image download failed: ${response.status} ${url}`);
  }
  const contentType = response.headers.get("content-type") || "";
  const ext = extensionForContentType(contentType);
  const finalPath = assetPath.replace(/\.(jpg|jpeg|png|webp)$/i, `.${ext}`);
  await fs.mkdir(path.dirname(finalPath), { recursive: true });
  const buffer = Buffer.from(await response.arrayBuffer());
  await fs.writeFile(finalPath, buffer);
  return finalPath.replaceAll("\\", "/");
}

async function main() {
  if (hasFlag("help") || hasFlag("h")) {
    printHelp();
    return;
  }

  const token = process.env.META_ACCESS_TOKEN || process.env.INSTAGRAM_ACCESS_TOKEN || process.env.FACEBOOK_PAGE_ACCESS_TOKEN;
  if (hasFlag("discover")) {
    await discoverMetaAssets(token || required("META_ACCESS_TOKEN"));
    return;
  }

  const fs = await import("node:fs/promises");
  const source = argValue("source", process.env.SOCIAL_GALLERY_SOURCE || "all").toLowerCase();
  const limit = optionalNumber("SOCIAL_GALLERY_LIMIT", DEFAULT_LIMIT, { min: 1, max: 100 });
  const approvedByDefault = hasFlag("approve") || process.env.SOCIAL_GALLERY_APPROVED === "1";
  const allowPartial = process.env.SOCIAL_GALLERY_ALLOW_PARTIAL !== "0";
  const existingData = await readJson(OUTPUT_PATH, { items: [] });
  const existingById = new Map((existingData.items ?? []).map((item) => [item.id, item]));
  const imported = [];
  const sourceErrors = [];
  const metaAccessToken = process.env.META_ACCESS_TOKEN || "";
  const pageId = process.env.FACEBOOK_PAGE_ID || "";
  const explicitPageToken = process.env.FACEBOOK_PAGE_ACCESS_TOKEN || "";
  const discoveredPageToken = explicitPageToken || (metaAccessToken && pageId ? await pageAccessTokenFor({ userToken: metaAccessToken, pageId }) : "");
  const pageCapableToken = discoveredPageToken || explicitPageToken || metaAccessToken;

  if (source === "all" || source === "instagram") {
    try {
      let instagramToken = process.env.INSTAGRAM_ACCESS_TOKEN || pageCapableToken || required("META_ACCESS_TOKEN");
      let instagramId = process.env.INSTAGRAM_BUSINESS_ACCOUNT_ID || "";
      if (!instagramId && pageId) {
        const connectedInstagram = await instagramAccountForPage({ token: pageCapableToken, pageId });
        instagramId = connectedInstagram?.id || "";
        if (instagramId) {
          console.log(`Discovered connected Instagram account @${connectedInstagram.username || "unknown"} (${maskedId(instagramId)}).`);
        }
      }
      if (!instagramId) {
        throw new Error("Missing required environment variable: INSTAGRAM_BUSINESS_ACCOUNT_ID. You can also provide FACEBOOK_PAGE_ID with a token that can read the connected Instagram business account.");
      }
      if (discoveredPageToken && !process.env.INSTAGRAM_ACCESS_TOKEN) {
        instagramToken = discoveredPageToken;
      }
      imported.push(...await listInstagramMedia({ token: instagramToken, instagramId, limit }));
    } catch (error) {
      if (source !== "all" || !allowPartial) throw error;
      sourceErrors.push(`Instagram import skipped: ${error.message}`);
      console.warn(`WARNING: Instagram import skipped: ${error.message}`);
    }
  }

  if (source === "all" || source === "facebook") {
    try {
      const facebookToken = pageCapableToken || required("META_ACCESS_TOKEN");
      if (!pageId) {
        throw new Error("Missing required environment variable: FACEBOOK_PAGE_ID.");
      }
      imported.push(...await listFacebookPhotos({ token: facebookToken, pageId, limit }));
    } catch (error) {
      if (source !== "all" || !allowPartial) throw error;
      sourceErrors.push(`Facebook import skipped: ${error.message}`);
      console.warn(`WARNING: Facebook import skipped: ${error.message}`);
    }
  }

  if (!imported.length && sourceErrors.length) {
    throw new Error(`No photos imported. ${sourceErrors.join(" ")}`);
  }

  const normalized = [];
  for (const photo of imported) {
    const id = `${photo.source.toLowerCase()}:${photo.sourceId}`;
    const item = normalizeImportedPhoto(photo, existingById.get(id), approvedByDefault);
    item.asset = await downloadImage(photo.sourceMediaUrl, item.asset);
    normalized.push(item);
  }

  const importedIds = new Set(normalized.map((item) => item.id));
  const preserved = (existingData.items ?? []).filter((item) => !importedIds.has(item.id));
  const items = [...normalized, ...preserved].sort((left, right) => String(right.publishedAt || "").localeCompare(String(left.publishedAt || "")));
  const output = {
    sourceName: "Sun Ray Instagram and Facebook photos",
    importNote: "Imported with the official Meta Graph API. New records default to approved=false so captions, routes, alt text, and local SEO metadata can be reviewed before publishing.",
    lastImportedAt: new Date().toISOString(),
    graphVersion: GRAPH_VERSION,
    sourceWarnings: sourceErrors,
    items,
  };

  await fs.mkdir("data", { recursive: true });
  await fs.writeFile(OUTPUT_PATH, `${JSON.stringify(output, null, 2)}\n`, "utf8");
  console.log(`Imported ${normalized.length} Meta photos into ${OUTPUT_PATH}. Approved for display: ${items.filter((item) => item.approved).length}.`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
