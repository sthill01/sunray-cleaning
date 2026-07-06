export async function onRequestPost() {
  return jsonResponse(
    {
      error: "unsupported_grant_type",
      error_description: "Sun Ray Cleaning quote handoffs do not issue bearer API tokens. Send the user to /contact/ to complete the request."
    },
    400
  );
}

export async function onRequestGet() {
  return jsonResponse({
    endpoint: "/agent/token",
    method: "POST",
    instructions: "This endpoint is present for auth.md discovery. Sun Ray Cleaning does not issue bearer API credentials."
  });
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
