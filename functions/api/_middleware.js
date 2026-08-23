import { getHighConfidenceSpamReasons } from "../../quote-spam-rules.js";

const SUCCESS_MESSAGE =
  "Thanks. Sun Ray has your cleaning details and will follow up using the contact information you shared.";

export async function onRequest(context) {
  const request = context.request;
  const url = new URL(request.url);

  if (request.method !== "POST" || url.pathname !== "/api/quote") {
    return context.next();
  }

  let quote;
  try {
    quote = await parseRequest(request.clone());
  } catch {
    return context.next();
  }

  const reasons = getHighConfidenceSpamReasons(quote);
  if (!reasons.length) {
    return context.next();
  }

  console.warn("Sun Ray quote blocked by API middleware", { reasons });
  return silentSuccessResponse(request);
}

async function parseRequest(request) {
  const contentType = request.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    return await request.json();
  }
  const formData = await request.formData();
  return Object.fromEntries(formData.entries());
}

function silentSuccessResponse(request) {
  const wantsJson = request.headers.get("accept")?.includes("application/json");

  if (wantsJson) {
    return Response.json(
      { ok: true, message: SUCCESS_MESSAGE, trackConversion: false },
      { status: 200 },
    );
  }

  return new Response(
    `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><title>Quote request received | Sun Ray Cleaning</title><link rel="stylesheet" href="/styles.css"></head><body><main><section class="page-hero"><div class="container"><p class="eyebrow">Quote request received</p><h1>Quote request received.</h1><p class="lead">${SUCCESS_MESSAGE}</p><div class="hero-actions"><a class="button button-yellow" href="/">Back to home</a><a class="button button-outline" href="tel:+18016042189">Call (801) 604-2189</a></div></div></section></main></body></html>`,
    { status: 200, headers: { "content-type": "text/html; charset=utf-8" } },
  );
}
