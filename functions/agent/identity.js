export async function onRequestGet({ request }) {
  const base = originBase(request);
  return jsonResponse({
    endpoint: `${base}/agent/identity`,
    identity_types_supported: ["anonymous", "service_auth"],
    scopes_supported: ["quote:create"],
    instructions: "POST an anonymous or service_auth quote-handoff request. Sun Ray Cleaning does not issue bearer API credentials."
  });
}

export async function onRequestPost({ request }) {
  const base = originBase(request);
  const body = await readJson(request);
  const registrationId = `sunray_quote_${Date.now()}`;

  return jsonResponse(
    {
      registration_id: registrationId,
      registration_type: "service_auth",
      status: "manual_handoff_required",
      scopes: normalizeScopes(body.scopes),
      claim_url: `${base}/agent/identity/claim`,
      claim_token: registrationId,
      claim_token_expires: new Date(Date.now() + 24 * 60 * 60 * 1000).toISOString(),
      claim: {
        user_code: "SUNRAY",
        expires_in: 900,
        verification_uri: `${base}/contact/`,
        interval: 30
      },
      instructions: "Send the user to the verification_uri to complete Sun Ray Cleaning's quote request. No bearer token or API credential is issued."
    },
    202
  );
}

async function readJson(request) {
  try {
    return await request.json();
  } catch {
    return {};
  }
}

function normalizeScopes(scopes) {
  return Array.isArray(scopes) && scopes.includes("quote:create") ? ["quote:create"] : ["quote:create"];
}

function originBase(request) {
  const url = new URL(request.url);
  const protocol = url.hostname.endsWith("sunray-cleaning.com") ? "https:" : url.protocol;
  return `${protocol}//${url.host}`;
}

function jsonResponse(body, status = 200) {
  return new Response(`${JSON.stringify(body, null, 2)}\n`, {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=60",
      "x-content-type-options": "nosniff"
    }
  });
}
