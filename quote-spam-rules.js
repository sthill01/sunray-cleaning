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
  "a", "about", "after", "afternoon", "and", "are", "asap", "at", "availability", "available", "basement",
  "bath", "bathroom", "bathrooms", "bed", "bedroom", "bedrooms", "before", "biweekly", "call", "can", "clean",
  "cleaning", "could", "deep", "estimate", "evening", "floor", "floors", "for", "friday", "garage", "have",
  "help", "hello", "home", "house", "i", "in", "interested", "is", "kitchen", "laundry", "like", "looking",
  "monday", "month", "monthly", "morning", "move", "my", "need", "next", "none", "of", "on", "one", "pet",
  "pets", "please", "pm", "price", "pricing", "quote", "regular", "saturday", "schedule", "scheduling", "service",
  "soon", "stairs", "sunday", "thank", "thanks", "the", "this", "thursday", "to", "today", "tomorrow",
  "tonight", "tuesday", "turnover", "want", "we", "wednesday", "week", "weekly", "what", "when", "with",
  "would", "you", "your"
]);

const SPANISH_WORDS = new Set([
  "a", "baño", "baños", "casa", "cita", "cocina", "con", "cotizacion", "cotización", "cuando", "cuándo", "de",
  "disponibilidad", "disponible", "el", "en", "esta", "este", "estimado", "favor", "gracias", "habitacion",
  "habitación", "habitaciones", "hola", "interesa", "interesado", "la", "las", "limpiar", "limpieza", "llamar",
  "los", "lunes", "mañana", "martes", "me", "miércoles", "miercoles", "mi", "mensual", "necesito", "para",
  "por", "precio", "profunda", "presupuesto", "que", "quiero", "quisiera", "sábado", "sabado", "saber",
  "semana", "semanal", "servicio", "si", "sí", "tarde", "una", "un", "viernes", "y", "yo"
]);

const SHORT_MESSAGE_ALLOWLIST = new Set([
  "asap", "call me", "text me", "need quote", "need cleaning", "deep clean", "move out", "move in", "weekly",
  "biweekly", "monthly", "hello", "thanks", "thank you", "no", "none", "n a", "na", "hola", "gracias",
  "limpieza", "cotizacion", "cotización", "si", "sí"
]);

export function getHighConfidenceSpamReasons(quote) {
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
    reasons.push("url_in_quote");
  }

  const combined = normalized(customerFields.join(" "));
  if (SCAM_TERMS.some((term) => combined.includes(term))) {
    reasons.push("financial_or_crypto_scam_terms");
  }

  const message = String(quote.notes || quote.message || "").trim();
  if (message && !looksLikeEnglishOrSpanish(message)) {
    reasons.push("message_not_english_or_spanish");
  }

  if (!isValidUsPhoneNumber(quote.phone)) {
    reasons.push("invalid_us_phone");
  }

  return [...new Set(reasons)];
}

export function isValidUsPhoneNumber(value) {
  const digits = String(value || "").replace(/\D/g, "");
  return digits.length === 10 || (digits.length === 11 && digits.startsWith("1"));
}

export function looksLikeEnglishOrSpanish(value) {
  const text = normalized(value);
  if (!text) return true;

  if (containsNonLatinScript(text)) return false;

  const compact = text.replace(/[^a-záéíóúüñ0-9\s'-]/g, " ").replace(/\s+/g, " ").trim();
  if (!compact) return false;

  if (SHORT_MESSAGE_ALLOWLIST.has(compact)) return true;

  const words = compact.split(" ").filter(Boolean);
  const letterWords = words.filter((word) => /[a-záéíóúüñ]/i.test(word));
  if (!letterWords.length) return false;

  if (letterWords.some((word) => /\d/.test(word) && /[a-z]/i.test(word) && word.length >= 5)) return false;
  if (letterWords.some((word) => /^[bcdfghjklmnpqrstvwxyz]{5,}$/i.test(word))) return false;

  let languageHits = 0;
  let meaningfulHits = 0;
  for (const rawWord of letterWords) {
    const word = rawWord.replace(/^[^a-záéíóúüñ]+|[^a-záéíóúüñ]+$/gi, "");
    if (ENGLISH_WORDS.has(word) || SPANISH_WORDS.has(word)) {
      languageHits += 1;
      if (word.length >= 3) meaningfulHits += 1;
    }
  }

  if (letterWords.length <= 3) {
    return meaningfulHits >= 1 || languageHits >= 2;
  }

  return meaningfulHits >= 2;
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
