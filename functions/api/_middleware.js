const SUCCESS_MESSAGE =
  "Thanks. Sun Ray has your cleaning details and will follow up using the contact information you shared.";

const SCAM_TERMS = [
  "balance",
  "coinbase",
  "withdraw",
  "withdrawal",
  "crypto",
  "cryptocurrency",
  "bitcoin",
  "btc",
  "ethereum",
  "wallet",
  "claim funds",
  "claim reward",
  "claim bonus",
  "account balance",
  "available balance",
  "cash out",
  "cashout",
  "investment return",
  "investment profit",
  "payment pending",
  "verify account",
  "verify wallet",
  "airdrop",
  "usdt",
  "binance",
  "telegram",
  "telegra.ph",
];

const KNOWN_SPAM_EMAIL_DOMAINS = new Set(["emalupe.com"]);

const ENGLISH_WORDS = new Set([
  "a", "about", "and", "are", "at", "bathroom", "bathrooms", "bedroom", "bedrooms", "clean", "cleaning",
  "could", "deep", "for", "have", "help", "home", "house", "i", "in", "is", "kitchen", "like", "looking",
  "move", "my", "need", "of", "on", "one", "please", "quote", "regular", "service", "the", "this", "to",
  "tomorrow", "want", "we", "week", "weekly", "with", "would", "you"
]);

const SPANISH_WORDS = new Set([
  "a", "baño", "baños", "casa", "cocina", "con", "cotización", "de", "el", "en", "esta", "este", "favor",
  "gracias", "habitacion", "habitación", "habitaciones", "hola", "la", "las", "limpiar", "limpieza", "los", "me",
  "mi", "necesito", "para", "por", "profunda", "que", "quiero", "servicio", "semana", "semanal", "una", "un",
  "y", "yo"
]);

const SHORT_MESSAGE_ALLOWLIST = new Set([
  "asap", "call me", "text me", "need quote", "need cleaning", "deep clean", "move out", "move in", "weekly",
  "biweekly", "monthly", "hola", "gracias", "limpieza", "cotizacion", "cotización"
]);

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

function getHighConfidenceSpamReasons(quote) {
  const reasons = [];
  const email = normalized(quote.email);
  const emailDomain = email.includes("@") ? email.split("@").pop() : "";

  if (KNOWN_SPAM_EMAIL_DOMAINS.has(emailDomain)) {
    reasons.push("known_spam_email_domain");
  }

  const customerFields = [
    quote["first-name"],
    quote.name,
    quote["service-area"],
    quote.city,
    quote.location,
    quote["service-type"],
    quote.service,
    quote["home-size"],
    quote["preferred-timing"],
    quote.notes,
    quote.message,
  ];

  if (customerFields.some((value) => hasUrlOrDomain(String(value || "")))) {
    reasons.push("url_in_customer_field");
  }

  const combined = normalized(customerFields.join(" "));
  if (SCAM_TERMS.some((term) => combined.includes(term))) {
    reasons.push("financial_or_crypto_scam_terms");
  }

  const message = String(quote.notes || quote.message || "").trim();
  if (message && !looksLikeEnglishOrSpanish(message)) {
    reasons.push("message_not_english_or_spanish");
  }

  return [...new Set(reasons)];
}

function looksLikeEnglishOrSpanish(value) {
  const text = normalized(value);
  if (!text) return true;

  if (containsNonLatinScript(text)) return false;

  const compact = text.replace(/[^a-záéíóúüñ0-9\s'-]/g, " ").replace(/\s+/g, " ").trim();
  if (!compact) return false;

  if (SHORT_MESSAGE_ALLOWLIST.has(compact)) return true;

  const words = compact.split(" ").filter(Boolean);
  const letterWords = words.filter((word) => /[a-záéíóúüñ]/i.test(word));
  if (!letterWords.length) return false;

  // Reject common bot gibberish such as random alphanumeric tokens in the message field.
  if (letterWords.length <= 2) {
    if (letterWords.some((word) => /\d/.test(word) && /[a-z]/i.test(word) && word.length >= 5)) return false;
    if (letterWords.some((word) => /^[bcdfghjklmnpqrstvwxyz]{5,}$/i.test(word))) return false;
    return true;
  }

  let languageHits = 0;
  for (const rawWord of letterWords) {
    const word = rawWord.replace(/^[^a-záéíóúüñ]+|[^a-záéíóúüñ]+$/gi, "");
    if (ENGLISH_WORDS.has(word) || SPANISH_WORDS.has(word)) languageHits += 1;
  }

  if (languageHits >= 1) return true;

  // Longer Latin-script text with no recognizable English/Spanish words is treated as non-target-language spam.
  return letterWords.length < 4;
}

function containsNonLatinScript(value) {
  return /[\u0370-\u03FF\u0400-\u052F\u0590-\u08FF\u0900-\u0DFF\u0E00-\u0FFF\u1000-\u109F\u3040-\u30FF\u3400-\u9FFF\uAC00-\uD7AF]/u.test(value);
}

function normalized(value) {
  return String(value || "")
    .toLowerCase()
    .replace(/\s+/g, " ")
    .trim();
}

function hasUrlOrDomain(value) {
  return /(?:https?:\/\/|www\.|\b[a-z0-9](?:[a-z0-9-]{0,62}[a-z0-9])?\.(?:com|net|org|io|co|biz|info|ru|cn|xyz|top|site|online|click|link|me|ph)(?:\/|\?|#|\b))/i.test(value);
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
