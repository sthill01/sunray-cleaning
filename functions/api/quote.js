const SUCCESS_MESSAGE =
  "Thanks. Sun Ray has your cleaning details and will follow up using the contact information you shared.";
const FORWARDING_ERROR_MESSAGE =
  "Something went wrong while forwarding your request. Please call or text (801) 604-2189 and we will help right away.";
const DEFAULT_QUOTE_EMAIL_RECIPIENTS = [
  "quotes@sunray-cleaning.com",
  "cyntya@sunray-cleaning.com",
  "cyntyahill@gmail.com",
  "sunrayservices17@gmail.com",
  "sthill01@gmail.com",
];
const DEFAULT_SMS_RECIPIENTS = ["+18016042189", "+18018501253"];
const MOUNTAIN_TIME_ZONE = "America/Denver";

export async function onRequestPost(context) {
  const wantsJson = context.request.headers.get("accept")?.includes("application/json");
  let quote;

  try {
    quote = await parseQuoteRequest(context.request);
  } catch (error) {
    console.warn("Sun Ray quote parse failed", error?.message || error);
    return quoteResponse({
      wantsJson,
      status: 400,
      ok: false,
      title: "Quote request is missing details",
      message:
        "Please check the form details and try again, or call or text (801) 604-2189 and we will help right away.",
    });
  }

  const spamCheck = await evaluateQuoteRequest(context.request, context.env, quote);
  if (!spamCheck.ok) {
    const spamAudit = await deliverSpamAudit(
      context.env,
      buildSpamAuditPayload(quote, context.request, "sunray-cloudflare-pages", spamCheck),
    );

    if (!spamAudit.ok && !spamAudit.missingConfig) {
      console.error("Sun Ray spam audit delivery failed");
    }

    console.warn("Sun Ray quote blocked", {
      reasons: spamCheck.reasons,
      score: spamCheck.score,
      ip: getClientIp(context.request) ? "present" : "missing",
    });

    return quoteResponse({
      wantsJson,
      status: 200,
      ok: true,
      title: "Quote request received",
      message: SUCCESS_MESSAGE,
      trackConversion: false,
    });
  }

  const payload = buildQuotePayload(quote, context.request, "sunray-cloudflare-pages");

  const delivery = await deliverQuote(context.env, payload);

  if (delivery.missingConfig) {
    return quoteResponse({
      wantsJson,
      status: 503,
      ok: false,
      title: "Quote forwarding is not configured yet",
      message:
        "This form is ready, but quote forwarding needs email, push, SMS, or webhook delivery configured in Cloudflare Pages. Please call or text (801) 604-2189 for live scheduling.",
    });
  }

  if (!delivery.ok) {
    return quoteResponse({
      wantsJson,
      status: 502,
      ok: false,
      title: "Quote request could not be forwarded",
      message: FORWARDING_ERROR_MESSAGE,
    });
  }

  return quoteResponse({
    wantsJson,
    status: 200,
    ok: true,
    title: "Quote request received",
    message: SUCCESS_MESSAGE,
  });
}

export async function onRequestGet(context) {
  return Response.redirect(new URL("/", context.request.url).toString(), 302);
}

function quoteResponse({ wantsJson, status, ok, title, message, trackConversion = ok }) {
  if (wantsJson) {
    return Response.json(
      {
        ok,
        message,
        trackConversion,
      },
      {
        status,
      },
    );
  }

  return new Response(
    `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>${escapeHtml(title)} | Sun Ray Cleaning</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="eyebrow">${ok ? "Quote request received" : "Quote request needs attention"}</p>
        <h1>${escapeHtml(title)}.</h1>
        <p class="lead">${escapeHtml(message)}</p>
        <div class="hero-actions">
          <a class="button button-yellow" href="/">Back to home</a>
          <a class="button button-outline" href="tel:+18016042189">Call (801) 604-2189</a>
        </div>
      </div>
    </section>
  </main>
</body>
</html>`,
    {
      status,
      headers: { "content-type": "text/html; charset=utf-8" },
    },
  );
}

async function parseQuoteRequest(request) {
  const contentType = request.headers.get("content-type") || "";

  if (contentType.includes("application/json")) {
    return await request.json();
  }

  const formData = await request.formData();
  return Object.fromEntries(formData.entries());
}

async function sendQuoteEmail(env, payload) {
  const to = getQuoteEmailRecipients(env);
  const from = env.SUNRAY_QUOTE_FROM_EMAIL || "Sun Ray Cleaning <quotes@sunray-cleaning.com>";
  const subject = buildSubject(payload);
  const emailBody = buildEmailBody(payload);
  const body = {
    from,
    to,
    subject,
    text: emailBody.text,
    html: emailBody.html,
    tags: [
      { name: "source", value: "sunray_quote_form" },
      { name: "site", value: "sunray_cleaning" },
    ],
  };

  if (payload.email) {
    body.reply_to = payload.email;
  }

  return fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      authorization: `Bearer ${env.RESEND_API_KEY}`,
      "content-type": "application/json",
    },
    body: JSON.stringify(body),
  });
}

function getQuoteEmailRecipients(env) {
  const configuredRecipients = String(env.SUNRAY_QUOTE_TO_EMAILS || env.SUNRAY_QUOTE_TO_EMAIL || "")
    .split(/[;,\n]/)
    .map((recipient) => recipient.trim())
    .filter(Boolean);

  return [...new Set(configuredRecipients.length ? configuredRecipients : DEFAULT_QUOTE_EMAIL_RECIPIENTS)];
}

function isPushoverConfigured(env) {
  return Boolean(env.SUNRAY_PUSHOVER_APP_TOKEN && env.SUNRAY_PUSHOVER_GROUP_KEY);
}

function isBrevoConfigured(env) {
  return Boolean(env.BREVO_API_KEY && env.BREVO_SMS_SENDER);
}

async function sendQuotePushNotification(env, payload) {
  const body = new URLSearchParams({
    token: String(env.SUNRAY_PUSHOVER_APP_TOKEN),
    user: String(env.SUNRAY_PUSHOVER_GROUP_KEY),
    message: buildPushMessage(payload),
    priority: String(env.SUNRAY_PUSHOVER_PRIORITY || "1"),
    sound: String(env.SUNRAY_PUSHOVER_SOUND || "cashregister"),
  });

  return fetch("https://api.pushover.net/1/messages.json", {
    method: "POST",
    headers: { "content-type": "application/x-www-form-urlencoded" },
    body,
  });
}

function buildPushMessage(payload) {
  const fields = [
    ["Name", payload["first-name"] || payload.name],
    ["Phone", payload.phone],
    ["Email", payload.email],
    ["Service", payload["service-type"] || payload.service],
    ["UTM source", payload.utm_source],
    ["Location", payload["service-area"] || payload.city || payload.location],
    ["Notes", payload.notes || payload.message],
  ];

  return [
    "New website lead",
    ...fields.map(([label, value]) => `${label}: ${formatAlertValue(value)}`),
  ]
    .join("\n")
    .slice(0, 1024);
}

function formatAlertValue(value) {
  const normalized = String(value || "")
    .replace(/\s+/g, " ")
    .trim();
  return normalized || "Not provided";
}

function getSmsRecipients(env) {
  const configuredRecipients = String(env.SUNRAY_SMS_TO_NUMBERS || "")
    .split(/[;,\n]/)
    .map((recipient) => recipient.trim())
    .filter(Boolean);

  return [...new Set(configuredRecipients.length ? configuredRecipients : DEFAULT_SMS_RECIPIENTS)];
}

async function sendQuoteSms(env, payload) {
  const message = buildPushMessage(payload);
  const responses = await Promise.all(
    getSmsRecipients(env).map((recipient) =>
      fetch("https://api.brevo.com/v3/transactionalSMS/send", {
        method: "POST",
        headers: {
          accept: "application/json",
          "api-key": String(env.BREVO_API_KEY),
          "content-type": "application/json",
        },
        body: JSON.stringify({
          sender: String(env.BREVO_SMS_SENDER),
          recipient: String(recipient).replace(/\D/g, ""),
          content: message,
          type: "transactional",
          tag: "website-lead",
        }),
      }),
    ),
  );

  return responses.find((response) => !response.ok) || Response.json({ ok: true });
}

async function deliverQuote(env, payload) {
  const webhookTargets = getWebhookTargets(env);
  const webhookResults = [];
  let emailOk = false;
  const emailConfigured = Boolean(env.RESEND_API_KEY);
  const pushConfigured = isPushoverConfigured(env);
  const smsConfigured = isBrevoConfigured(env);
  let pushOk = false;
  let smsOk = false;

  if (emailConfigured) {
    const emailResponse = await sendQuoteEmail(env, payload);
    emailOk = emailResponse.ok;

    if (!emailResponse.ok) {
      console.error("Sun Ray quote email failed", emailResponse.status, await safeResponseText(emailResponse));
    }
  }

  if (pushConfigured) {
    try {
      const pushResponse = await sendQuotePushNotification(env, payload);
      pushOk = pushResponse.ok;

      if (!pushResponse.ok) {
        console.error("Sun Ray quote push failed", pushResponse.status, await safeResponseText(pushResponse));
      }
    } catch (error) {
      console.error("Sun Ray quote push failed", error?.message || error);
    }
  }

  if (smsConfigured) {
    try {
      const smsResponse = await sendQuoteSms(env, payload);
      smsOk = smsResponse.ok;

      if (!smsResponse.ok) {
        console.error("Sun Ray quote SMS failed", smsResponse.status, await safeResponseText(smsResponse));
      }
    } catch (error) {
      console.error("Sun Ray quote SMS failed", error?.message || error);
    }
  }

  for (const target of webhookTargets) {
    webhookResults.push(await sendQuoteWebhook(target, payload));
  }

  const webhookOk = webhookResults.some((result) => result.ok);
  webhookResults
    .filter((result) => !result.ok)
    .forEach((result) => {
      console.error("Sun Ray quote webhook failed", result.name, result.status || "", result.error || "");
    });

  return {
    ok: emailOk || pushOk || smsOk || webhookOk,
    missingConfig: !emailConfigured && !pushConfigured && !smsConfigured && webhookTargets.length === 0,
  };
}

async function deliverSpamAudit(env, payload) {
  const webhookTargets = getSpamAuditTargets(env);
  const webhookResults = [];

  for (const target of webhookTargets) {
    webhookResults.push(await sendQuoteWebhook(target, payload));
  }

  const webhookOk = webhookResults.some((result) => result.ok);
  webhookResults
    .filter((result) => !result.ok)
    .forEach((result) => {
      console.error("Sun Ray spam audit webhook failed", result.name, result.status || "", result.error || "");
    });

  return {
    ok: webhookOk,
    missingConfig: webhookTargets.length === 0,
  };
}

function getSpamAuditTargets(env) {
  const seen = new Set();
  return [{ name: "SUNRAY_QUOTE_SPAM_WEBHOOK_URL", url: env.SUNRAY_QUOTE_SPAM_WEBHOOK_URL }].filter((target) => {
    const url = String(target.url || "").trim();
    if (!url || seen.has(url)) return false;
    seen.add(url);
    target.url = url;
    return true;
  });
}

function getWebhookTargets(env) {
  const seen = new Set();
  return [
    { name: "SUNRAY_QUOTE_WEBHOOK_URL", url: env.SUNRAY_QUOTE_WEBHOOK_URL },
    { name: "SUNRAY_QUOTE_SHEETS_WEBHOOK_URL", url: env.SUNRAY_QUOTE_SHEETS_WEBHOOK_URL },
  ].filter((target) => {
    const url = String(target.url || "").trim();
    if (!url || seen.has(url)) return false;
    seen.add(url);
    target.url = url;
    return true;
  });
}

async function sendQuoteWebhook(target, payload) {
  try {
    const response = await fetch(target.url, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });

    return response.ok
      ? { ok: true, name: target.name, status: response.status }
      : { ok: false, name: target.name, status: response.status, error: await safeResponseText(response) };
  } catch (error) {
    return { ok: false, name: target.name, error: error?.message || String(error) };
  }
}

async function evaluateQuoteRequest(request, env, quote) {
  const reasons = [];
  let score = 0;

  if (hasFilledHoneypot(quote)) {
    return { ok: false, score: 10, reasons: ["honeypot"] };
  }

  if (!hasTrustedReferer(request)) {
    score += 2;
    reasons.push("untrusted_referer");
  }

  const turnstile = await verifyTurnstileIfConfigured(request, env, quote);
  if (!turnstile.ok) {
    return { ok: false, score: 10, reasons: [turnstile.reason] };
  }

  const rateLimit = await checkRateLimit(request, env);
  if (!rateLimit.ok) {
    return { ok: false, score: 10, reasons: [rateLimit.reason] };
  }

  const content = scoreQuoteContent(quote);
  score += content.score;
  reasons.push(...content.reasons);

  return {
    ok: score < 4,
    score,
    reasons,
  };
}

function cleanQuotePayload(quote) {
  const internalFields = new Set([
    "_gotcha",
    "bot-field",
    "business-url",
    "cf-turnstile-response",
    "company-website",
    "form-started-at",
    "submission-elapsed-ms",
    "turnstileToken",
    "url",
    "website",
  ]);

  return Object.fromEntries(Object.entries(quote).filter(([key]) => !internalFields.has(key)));
}

function buildQuotePayload(quote, request, source) {
  return {
    ...cleanQuotePayload(quote),
    submittedAt: new Date().toISOString(),
    source,
    pageUrl: request.headers.get("referer") || "",
  };
}

function buildSpamAuditPayload(quote, request, source, spamCheck) {
  return {
    ...buildQuotePayload(quote, request, source),
    filteredAsSpam: true,
    spamStatus: "Filtered before email or conversion tracking",
    spamScore: spamCheck.score,
    spamReasons: spamCheck.reasons.join(", "),
    spamReviewNote: "Review this row before treating it as confirmed spam.",
  };
}

function hasFilledHoneypot(quote) {
  return ["_gotcha", "bot-field", "business-url", "company-website", "url", "website"].some((key) =>
    String(quote[key] || "").trim(),
  );
}

function hasTrustedReferer(request) {
  const referer = request.headers.get("referer") || "";
  if (!referer) return true;

  try {
    const hostname = new URL(referer).hostname.toLowerCase();
    return (
      hostname === "sunray-cleaning.com" ||
      hostname === "www.sunray-cleaning.com" ||
      hostname.endsWith(".pages.dev") ||
      hostname === "localhost" ||
      hostname === "127.0.0.1"
    );
  } catch {
    return false;
  }
}

async function verifyTurnstileIfConfigured(request, env, quote) {
  if (!env.TURNSTILE_SECRET_KEY) {
    return { ok: true };
  }

  const token = String(quote["cf-turnstile-response"] || quote.turnstileToken || "").trim();
  if (!token) {
    return { ok: false, reason: "missing_turnstile" };
  }

  const formData = new FormData();
  formData.append("secret", env.TURNSTILE_SECRET_KEY);
  formData.append("response", token);

  const clientIp = getClientIp(request);
  if (clientIp) {
    formData.append("remoteip", clientIp);
  }

  try {
    const response = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", {
      method: "POST",
      body: formData,
    });
    const result = await response.json();
    return result.success ? { ok: true } : { ok: false, reason: "failed_turnstile" };
  } catch (error) {
    console.error("Sun Ray Turnstile verification failed", error?.message || error);
    return { ok: false, reason: "turnstile_error" };
  }
}

async function checkRateLimit(request, env) {
  const store = env.SUNRAY_QUOTE_RATE_LIMIT;
  if (!store || typeof store.get !== "function" || typeof store.put !== "function") {
    return { ok: true };
  }

  const clientIp = getClientIp(request);
  if (!clientIp) {
    return { ok: true };
  }

  const bucket = Math.floor(Date.now() / 3600000);
  const key = `quote:${bucket}:${await sha256(clientIp)}`;
  const current = Number.parseInt((await store.get(key)) || "0", 10);

  if (current >= 3) {
    return { ok: false, reason: "rate_limited" };
  }

  await store.put(key, String(current + 1), { expirationTtl: 7200 });
  return { ok: true };
}

function getClientIp(request) {
  return request.headers.get("cf-connecting-ip") || request.headers.get("x-forwarded-for")?.split(",")[0]?.trim() || "";
}

async function sha256(value) {
  const input = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", input);
  return Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("")
    .slice(0, 24);
}

function scoreQuoteContent(quote) {
  const reasons = [];
  let score = 0;
  const serviceArea = normalizedValue(quote["service-area"] || quote.city || quote.location);
  const notes = normalizedValue(quote.notes || quote.message);
  const homeSize = normalizedValue(quote["home-size"]);
  const combinedText = normalizedValue(Object.values(quote).join(" "));
  const marketingHits = [
    "ai visibility",
    "backlink",
    "digital marketing",
    "guest post",
    "hire seo geek",
    "lead generation",
    "more leads",
    "quick seo questionnaire",
    "rank higher",
    "sales",
    "search traffic",
    "seo",
    "supersupportstaff",
    "traffic growth",
    "visibility and targeting",
  ].filter((term) => combinedText.includes(term));

  if (hasUrl(notes) || hasUrl(homeSize) || hasUrl(serviceArea)) {
    score += 4;
    reasons.push("url_in_quote");
  }

  if (marketingHits.length >= 2) {
    score += 4;
    reasons.push("marketing_pitch");
  } else if (marketingHits.length === 1) {
    score += 1;
    reasons.push("marketing_keyword");
  }

  if (serviceArea && !isLikelyServiceArea(serviceArea) && (marketingHits.length || hasUrl(notes))) {
    score += 2;
    reasons.push("non_local_marketing");
  }

  if (notes.length > 1200) {
    score += 1;
    reasons.push("long_notes");
  }

  const elapsedMs = Number.parseInt(String(quote["submission-elapsed-ms"] || ""), 10);
  if (Number.isFinite(elapsedMs) && elapsedMs > 0 && elapsedMs < 2000) {
    score += 2;
    reasons.push("fast_submit");
  }

  const email = String(quote.email || "").trim();
  if (email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
    score += 2;
    reasons.push("invalid_email");
  }

  const phoneDigits = String(quote.phone || "").replace(/\D/g, "");
  if (phoneDigits && phoneDigits.length < 7) {
    score += 1;
    reasons.push("short_phone");
  }

  return { score, reasons };
}

function normalizedValue(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

function hasUrl(value) {
  return /https?:\/\/|www\.|[a-z0-9-]+\.(com|net|org|io|co|biz|info|ru|cn|xyz|top|site|online|click|link|me)(\/|\b)/i.test(
    value,
  );
}

function isLikelyServiceArea(value) {
  return [
    "canyons",
    "coalville",
    "deer valley",
    "heber",
    "hideout",
    "jordanelle",
    "kamas",
    "kimball junction",
    "midway",
    "oakley",
    "park city",
    "salt lake",
    "snyderville",
    "summit",
    "utah",
    "wasatch",
  ].some((area) => value.includes(area));
}

function buildSubject(payload) {
  const area = payload["service-area"] || payload.city || payload.location || "";
  const service = payload["service-type"] || payload.service || "Quote request";
  return [service, area].filter(Boolean).join(" - ");
}

function buildEmailBody(payload) {
  const labels = {
    "first-name": "First name",
    name: "Name",
    phone: "Phone",
    email: "Email",
    "service-area": "City or neighborhood",
    "service-type": "Service type",
    "home-size": "Home size",
    "preferred-timing": "Preferred timing",
    notes: "Notes",
    message: "Message",
    gclid: "GCLID",
    gbraid: "GBRAID",
    wbraid: "WBRAID",
    msclkid: "Microsoft Click ID",
    fbclid: "Facebook Click ID",
    ttclid: "TikTok Click ID",
    li_fat_id: "LinkedIn Click ID",
    utm_source: "UTM source",
    utm_medium: "UTM medium",
    utm_campaign: "UTM campaign",
    utm_term: "UTM term",
    utm_content: "UTM content",
    utm_id: "UTM ID",
    first_landing_page: "First landing page",
    landing_page: "Landing page",
    referrer: "Referrer",
    attribution_updated_at: "Attribution updated at",
    pageUrl: "Page URL",
    submittedAt: "Submitted at (Mountain Time)",
  };

  const rows = Object.entries(payload)
    .filter(([, value]) => String(value || "").trim())
    .map(([key, value]) => {
      const label = labels[key] || toTitleCase(key);
      const displayValue = key === "submittedAt" ? formatMountainTime(value) : String(value);
      return { label, value: displayValue };
    });

  const text = rows.map(({ label, value }) => `${label}: ${value}`).join("\n");
  const htmlRows = rows
    .map(
      ({ label, value }) =>
        `<tr><th align="left" style="padding:8px 12px;border-bottom:1px solid #e9e3d8;color:#173866;width:180px;">${escapeHtml(label)}</th><td style="padding:8px 12px;border-bottom:1px solid #e9e3d8;">${escapeHtml(value).replace(/\n/g, "<br>")}</td></tr>`,
    )
    .join("");

  const html = `<!doctype html>
<html lang="en">
<body style="font-family:Arial,sans-serif;color:#172033;line-height:1.5;">
  <h1 style="color:#173866;font-size:24px;margin:0 0 12px;">New Sun Ray quote request</h1>
  <p style="margin:0 0 18px;">A visitor submitted the quote form on sunray-cleaning.com.</p>
  <table cellspacing="0" cellpadding="0" style="border-collapse:collapse;width:100%;max-width:720px;border:1px solid #e9e3d8;">${htmlRows}</table>
</body>
</html>`;

  return { text, html };
}

function formatMountainTime(value) {
  if (!value) return "";

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);

  return new Intl.DateTimeFormat("en-US", {
    timeZone: MOUNTAIN_TIME_ZONE,
    year: "numeric",
    month: "short",
    day: "numeric",
    hour: "numeric",
    minute: "2-digit",
    second: "2-digit",
    timeZoneName: "short",
  }).format(date);
}

async function safeResponseText(response) {
  const text = await response.text().catch(() => "");
  return text.slice(0, 800);
}

function toTitleCase(value) {
  return String(value)
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}
