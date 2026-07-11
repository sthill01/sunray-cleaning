export async function onRequest(context) {
  const { request, env } = context;
  const assetUrl = new URL("/__sunray_custom_404__", request.url);
  const assetRequest = new Request(assetUrl, request);
  const assetResponse = await env.ASSETS.fetch(assetRequest);
  const headers = new Headers(assetResponse.headers);
  headers.set("x-robots-tag", "noindex, nofollow");

  return new Response(request.method === "HEAD" ? null : assetResponse.body, {
    status: 404,
    headers,
  });
}
