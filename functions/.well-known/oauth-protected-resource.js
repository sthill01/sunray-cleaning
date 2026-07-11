export async function onRequestGet({ request }) {
  return jsonResponse(protectedResourceMetadata(request));
}

export async function onRequestHead({ request }) {
  const response = jsonResponse(protectedResourceMetadata(request));
  return new Response(null, { status: response.status, headers: response.headers });
}

function protectedResourceMetadata(request) {
  const base = originBase(request);
  return {
    resource: base,
    resource_name: "Sun Ray Cleaning Services public site and quote intake",
    authorization_servers: [base],
    scopes_supported: ["quote:create"],
    bearer_methods_supported: ["header"],
    resource_documentation: `${base}/auth.md`,
    agent_auth: agentAuth(base)
  };
}

function agentAuth(base) {
  return {
    skill: `${base}/auth.md`,
    register_uri: `${base}/agent/identity`,
    claim_uri: `${base}/agent/identity/claim`,
    revocation_uri: `${base}/agent/revoke`,
    identity_endpoint: `${base}/agent/identity`,
    claim_endpoint: `${base}/agent/identity/claim`,
    events_endpoint: `${base}/agent/event/notify`,
    claims_url: `${base}/agent/identity/claim`,
    revocation_url: `${base}/agent/revoke`,
    supported_identity_types: ["anonymous", "service_auth"],
    identity_types_supported: ["anonymous", "service_auth"],
    credential_types_supported: ["quote_handoff"],
    anonymous: { credential_types_supported: ["quote_handoff"] },
    service_auth: { credential_types_supported: ["quote_handoff"] },
    identity_assertion: { assertion_types_supported: [] },
    events_supported: [],
    instructions: "Sun Ray Cleaning supports a public quote-handoff registration method for agents. It does not issue bearer API credentials; use the returned verification URI to send the user to the quote flow."
  };
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
      "cache-control": "public, max-age=300",
      "x-content-type-options": "nosniff"
    }
  });
}
