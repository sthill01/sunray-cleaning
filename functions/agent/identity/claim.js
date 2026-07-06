export async function onRequestGet({ request }) {
  const base = originBase(request);
  return jsonResponse({
    endpoint: `${base}/agent/identity/claim`,
    status: "manual_handoff",
    verification_uri: `${base}/contact/`,
    instructions: "Use the contact page to complete the quote handoff with the user."
  });
}

export async function onRequestPost({ request }) {
  const base = originBase(request);
  return jsonResponse({
    status: "manual_handoff",
    claim_attempt: {
      user_code: "SUNRAY",
      expires_in: 900,
      verification_uri: `${base}/contact/`,
      interval: 30
    },
    instructions: "Ask the user to complete Sun Ray Cleaning's quote form or call/text (801) 604-2189."
  });
}

function originBase(request) {
  const url = new URL(request.url);
  const protocol = url.hostname.endsWith("sunray-cleaning.com") ? "https:" : url.protocol;
  return `${protocol}//${url.host}`;
}

function jsonResponse(body) {
  return new Response(`${JSON.stringify(body, null, 2)}\n`, {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=60",
      "x-content-type-options": "nosniff"
    }
  });
}
