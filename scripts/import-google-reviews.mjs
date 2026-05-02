#!/usr/bin/env node

const API_BASE = "https://mybusiness.googleapis.com/v4";
const TOKEN_URL = "https://oauth2.googleapis.com/token";
const STAR_RATINGS = {
  ONE: 1,
  TWO: 2,
  THREE: 3,
  FOUR: 4,
  FIVE: 5,
};

function required(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required environment variable: ${name}`);
  }
  return value;
}

function numberEnv(name, fallback, { min = 1, max = Number.POSITIVE_INFINITY } = {}) {
  const raw = process.env[name];
  if (!raw) return fallback;
  const value = Number(raw);
  if (!Number.isFinite(value) || value < min) {
    throw new Error(`${name} must be a number greater than or equal to ${min}.`);
  }
  return Math.min(value, max);
}

async function getAccessToken() {
  if (process.env.GOOGLE_BUSINESS_PROFILE_ACCESS_TOKEN) {
    return process.env.GOOGLE_BUSINESS_PROFILE_ACCESS_TOKEN;
  }

  const clientId = required("GOOGLE_CLIENT_ID");
  const clientSecret = required("GOOGLE_CLIENT_SECRET");
  const refreshToken = required("GOOGLE_REFRESH_TOKEN");
  const response = await fetch(TOKEN_URL, {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      client_id: clientId,
      client_secret: clientSecret,
      refresh_token: refreshToken,
      grant_type: "refresh_token",
    }),
  });

  if (!response.ok) {
    throw new Error(`OAuth refresh failed: ${response.status} ${await response.text()}`);
  }

  const payload = await response.json();
  if (!payload.access_token) {
    throw new Error("OAuth refresh did not return an access token.");
  }
  return payload.access_token;
}

async function fetchJson(url, token) {
  const response = await fetch(url, {
    headers: { authorization: `Bearer ${token}` },
  });
  if (!response.ok) {
    throw new Error(`Google Business Profile request failed: ${response.status} ${await response.text()}`);
  }
  return response.json();
}

function ratingNumber(starRating) {
  return STAR_RATINGS[starRating] ?? null;
}

function normalizeReview(review, profileUrl) {
  const reviewer = review.reviewer ?? {};
  const isAnonymous = Boolean(reviewer.isAnonymous);
  const author = isAnonymous ? "Google reviewer" : reviewer.displayName || "Google reviewer";
  const normalized = {
    reviewId: review.reviewId,
    author,
    isAnonymous,
    rating: ratingNumber(review.starRating),
    text: review.comment || "",
    createTime: review.createTime,
    updateTime: review.updateTime,
    profilePhotoUrl: isAnonymous ? "" : reviewer.profilePhotoUrl || "",
    sourceUrl: profileUrl,
  };

  if (Array.isArray(review.reviewMediaItems) && review.reviewMediaItems.length) {
    normalized.reviewMediaItems = review.reviewMediaItems;
  }
  if (review.reviewReply?.comment) {
    normalized.ownerReply = {
      text: review.reviewReply.comment,
      updateTime: review.reviewReply.updateTime,
      state: review.reviewReply.reviewReplyState,
    };
  }
  return normalized;
}

async function listAllReviews({ token, accountId, locationId, pageSize, maxPages }) {
  const parent = `accounts/${accountId}/locations/${locationId}`;
  let pageToken = "";
  const reviews = [];
  let averageRating = null;
  let totalReviewCount = null;

  for (let page = 0; page < maxPages; page += 1) {
    const params = new URLSearchParams({ pageSize: String(pageSize), orderBy: "updateTime desc" });
    if (pageToken) params.set("pageToken", pageToken);
    const url = `${API_BASE}/${parent}/reviews?${params}`;
    const payload = await fetchJson(url, token);
    reviews.push(...(payload.reviews ?? []));
    averageRating = payload.averageRating ?? averageRating;
    totalReviewCount = payload.totalReviewCount ?? totalReviewCount;
    pageToken = payload.nextPageToken || "";
    if (!pageToken) break;
  }

  return { reviews, averageRating, totalReviewCount };
}

async function main() {
  const fs = await import("node:fs/promises");
  const accountId = required("GBP_ACCOUNT_ID");
  const locationId = required("GBP_LOCATION_ID");
  const profileUrl = process.env.GBP_PROFILE_URL || "";
  const pageSize = numberEnv("GBP_PAGE_SIZE", 50, { min: 1, max: 50 });
  const maxPages = numberEnv("GBP_MAX_PAGES", 5, { min: 1 });
  const featuredLimit = numberEnv("GBP_FEATURED_REVIEW_LIMIT", 12, { min: 1 });
  const minRating = numberEnv("GBP_FEATURED_MIN_RATING", 5, { min: 1, max: 5 });
  const token = await getAccessToken();
  const { reviews, averageRating, totalReviewCount } = await listAllReviews({ token, accountId, locationId, pageSize, maxPages });

  const normalized = reviews.map((review) => normalizeReview(review, profileUrl));
  const featuredReviews = normalized
    .filter((review) => review.text && review.rating >= minRating)
    .slice(0, featuredLimit);

  const output = {
    sourceName: "Google Business Profile",
    locationName: `accounts/${accountId}/locations/${locationId}`,
    reviewCount: totalReviewCount ?? normalized.length,
    ratingValue: averageRating ?? null,
    bestRating: 5,
    worstRating: 1,
    profileUrl,
    lastImported: new Date().toISOString(),
    displayNote: "Imported from the official Google Business Profile Reviews API. Anonymous reviewers are displayed without names or profile photos; exact excerpts come only from imported review text.",
    featuredReviews,
    allReviews: normalized,
  };

  await fs.mkdir("data", { recursive: true });
  await fs.writeFile("data/reviews.json", `${JSON.stringify(output, null, 2)}\n`, "utf8");
  console.log(`Imported ${normalized.length} reviews from Google Business Profile. Featured: ${featuredReviews.length}.`);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
