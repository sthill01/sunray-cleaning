export async function onRequestPost() {
  return jsonResponse({
    status: "accepted",
    instructions: "Sun Ray Cleaning records no autonomous API credentials; no downstream event processing is required for quote handoffs."
  });
}

export async function onRequestGet() {
  return jsonResponse({
    endpoint: "/agent/event/notify",
    events_supported: []
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
