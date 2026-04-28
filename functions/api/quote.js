export async function onRequestPost(context) {
  const formData = await context.request.formData();
  const quote = Object.fromEntries(formData.entries());
  quote.submittedAt = new Date().toISOString();
  quote.source = "sunray-cloudflare-preview";

  if (context.env.SUNRAY_QUOTE_WEBHOOK_URL) {
    await fetch(context.env.SUNRAY_QUOTE_WEBHOOK_URL, {
      method: "POST",
      headers: { "content-type": "application/json" },
      body: JSON.stringify(quote),
    });
  }

  return new Response(
    `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <title>Quote request received | Sun Ray Cleaning</title>
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="eyebrow">Quote request received</p>
        <h1>Thanks. Sun Ray has your cleaning details.</h1>
        <p class="lead">This preview endpoint accepted the form. Add SUNRAY_QUOTE_WEBHOOK_URL in Cloudflare Pages settings to forward quote requests to your CRM, email automation, or Zapier/Make webhook.</p>
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
      headers: { "content-type": "text/html; charset=utf-8" },
    },
  );
}

export async function onRequestGet() {
  return Response.redirect("/", 302);
}
