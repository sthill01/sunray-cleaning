export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.pathname === "/api/quote") {
      if (request.method === "GET" || request.method === "HEAD") {
        return Response.redirect(new URL("/", request.url).toString(), 302);
      }

      if (request.method === "POST") {
        return handleQuotePost(request, env);
      }

      return new Response("Method not allowed", {
        status: 405,
        headers: {
          allow: "GET, HEAD, POST",
        },
      });
    }

    return env.ASSETS.fetch(request);
  },
};

async function handleQuotePost(request, env) {
  const wantsJson = request.headers.get("accept")?.includes("application/json");
  const quote = await parseQuoteRequest(request);
  const payload = {
    ...quote,
    submittedAt: new Date().toISOString(),
    source: "sunray-cloudflare-worker",
    pageUrl: request.headers.get("referer") || "",
  };

  if (env.SUNRAY_QUOTE_WEBHOOK_URL) {
    const webhookResponse = await fetch(env.SUNRAY_QUOTE_WEBHOOK_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!webhookResponse.ok) {
      return quoteResponse({
        wantsJson,
        status: 502,
        ok: false,
        title: "Quote request could not be forwarded",
        message:
          "Something went wrong while forwarding your request. Please call or text (801) 604-2189 and we will help right away.",
      });
    }

    return quoteResponse({
      wantsJson,
      status: 200,
      ok: true,
      title: "Quote request received",
      message:
        "Thanks. Sun Ray has your cleaning details and will follow up using the contact information you shared.",
    });
  }

  if (!env.RESEND_API_KEY) {
    return quoteResponse({
      wantsJson,
      status: 503,
      ok: false,
      title: "Quote forwarding is not configured yet",
      message:
        "This form is ready, but email forwarding needs RESEND_API_KEY or SUNRAY_QUOTE_WEBHOOK_URL in Cloudflare. Please call or text (801) 604-2189 for live scheduling.",
    });
  }

  const emailResponse = await sendQuoteEmail(env, payload);

  if (!emailResponse.ok) {
    console.error("Sun Ray quote email failed", emailResponse.status, await safeResponseText(emailResponse));
    return quoteResponse({
      wantsJson,
      status: 502,
      ok: false,
      title: "Quote request could not be forwarded",
      message:
        "Something went wrong while forwarding your request. Please call or text (801) 604-2189 and we will help right away.",
    });
  }

  return quoteResponse({
    wantsJson,
    status: 200,
    ok: true,
    title: "Quote request received",
    message:
      "Thanks. Sun Ray has your cleaning details and will follow up using the contact information you shared.",
  });
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
  const to = env.SUNRAY_QUOTE_TO_EMAIL || "cyntyahill@gmail.com";
  const from = env.SUNRAY_QUOTE_FROM_EMAIL || "Sun Ray Cleaning <quotes@sunray-cleaning.com>";
  const subject = buildSubject(payload);
  const emailBody = buildEmailBody(payload);
  const body = {
    from,
    to: [to],
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
    pageUrl: "Page URL",
    submittedAt: "Submitted at",
  };

  const rows = Object.entries(payload)
    .filter(([, value]) => String(value || "").trim())
    .map(([key, value]) => {
      const label = labels[key] || toTitleCase(key);
      return { label, value: String(value) };
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

async function safeResponseText(response) {
  const text = await response.text().catch(() => "");
  return text.slice(0, 800);
}

function toTitleCase(value) {
  return String(value)
    .replace(/[-_]+/g, " ")
    .replace(/\b\w/g, (letter) => letter.toUpperCase());
}

function quoteResponse({ wantsJson, status, ok, title, message }) {
  if (wantsJson) {
    return Response.json(
      {
        ok,
        message,
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

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}
