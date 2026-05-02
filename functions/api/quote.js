export async function onRequestPost(context) {
  const wantsJson = context.request.headers.get("accept")?.includes("application/json");
  const formData = await context.request.formData();
  const quote = Object.fromEntries(formData.entries());
  const payload = {
    ...quote,
    submittedAt: new Date().toISOString(),
    source: "sunray-cloudflare-preview",
    pageUrl: context.request.headers.get("referer") || "",
  };

  if (!context.env.SUNRAY_QUOTE_WEBHOOK_URL) {
    return quoteResponse({
      wantsJson,
      status: 503,
      ok: false,
      title: "Quote forwarding is not configured yet",
      message:
        "This preview form is ready, but email forwarding needs SUNRAY_QUOTE_WEBHOOK_URL in Cloudflare Pages. Please call or text (801) 604-2189 for live scheduling.",
    });
  }

  const webhookResponse = await fetch(context.env.SUNRAY_QUOTE_WEBHOOK_URL, {
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

export async function onRequestGet() {
  return Response.redirect("/", 302);
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
