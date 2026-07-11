export async function onRequestPost() {
  return jsonResponse({
    status: "revoked",
    instructions: "Quote handoff registration is closed. No bearer token or API credential existed."
  });
}

export async function onRequestGet() {
  return jsonResponse({
    endpoint: "/agent/revoke",
    method: "POST",
    instructions: "POST a registration id to acknowledge quote-handoff revocation."
  });
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
