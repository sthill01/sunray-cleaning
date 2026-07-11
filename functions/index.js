const DISCOVERY_LINKS = [
  '</llms.txt>; rel="alternate"; type="text/markdown"; title="Sun Ray Cleaning LLM summary"',
  '</.well-known/agent-resources.json>; rel="service-desc"; type="application/json"',
  '</.well-known/api-catalog>; rel="api-catalog"; type="application/linkset+json"',
  '</auth.md>; rel="authorization-server"; type="text/markdown"',
  '</.well-known/mcp/server-card.json>; rel="service-desc"; type="application/json"; title="MCP server card"',
  '</.well-known/agent-card.json>; rel="service-desc"; type="application/json"; title="A2A agent card"',
  '</.well-known/agent-skills/index.json>; rel="service-desc"; type="application/json"; title="Agent skills index"'
].join(", ");

const HOME_MARKDOWN = `# Sun Ray Cleaning Services

Sun Ray Cleaning Services is a female-owned residential cleaning company serving Park City, Heber City, Midway, Summit County, Wasatch County, and nearby Utah mountain communities.

## Services

- Residential house cleaning
- Airbnb and VRBO turnover cleaning
- Deep cleaning
- Weekly, biweekly, and monthly recurring cleaning
- Move-in and move-out cleaning
- Eco-friendly and pet-safe cleaning options

## Service Areas

- Park City, including Old Town, Deer Valley, Canyons Village, Park Meadows, Prospector, Pinebrook, Jeremy Ranch, Promontory, and Kimball Junction
- Heber City and Heber Valley, including Red Ledges, Jordanelle, Timber Lakes, Old Town Heber, and Center Creek
- Midway, Kamas, Oakley, Coalville, Daniel, Summit County, and Wasatch County mountain-home communities

## Agent Resources

- [llms.txt](https://www.sunray-cleaning.com/llms.txt)
- [Agent resources](https://www.sunray-cleaning.com/.well-known/agent-resources.json)
- [API catalog](https://www.sunray-cleaning.com/.well-known/api-catalog)
- [auth.md](https://www.sunray-cleaning.com/auth.md)
- [Sitemap](https://www.sunray-cleaning.com/sitemap.xml)

## Contact

- Quote page: [Get a cleaning quote](https://www.sunray-cleaning.com/contact/)
- Phone or SMS: (801) 604-2189
`;

export async function onRequest(context) {
  const { request, env } = context;
  const method = request.method.toUpperCase();
  const accept = request.headers.get("accept") || "";

  if ((method === "GET" || method === "HEAD") && wantsMarkdown(accept)) {
    const headers = discoveryHeaders("text/markdown; charset=utf-8");
    headers.set("vary", "Accept");
    headers.set("x-markdown-source", "/");
    headers.set("x-markdown-tokens", String(Math.ceil(HOME_MARKDOWN.length / 4)));
    return new Response(method === "HEAD" ? null : HOME_MARKDOWN, { status: 200, headers });
  }

  const response = await env.ASSETS.fetch(request);
  const headers = new Headers(response.headers);
  addDiscoveryHeaders(headers);
  return new Response(method === "HEAD" ? null : response.body, {
    status: response.status,
    statusText: response.statusText,
    headers
  });
}

function wantsMarkdown(accept) {
  const markdownIndex = accept.indexOf("text/markdown");
  if (markdownIndex === -1) return false;

  const htmlIndex = accept.indexOf("text/html");
  return htmlIndex === -1 || markdownIndex < htmlIndex;
}

function discoveryHeaders(contentType) {
  const headers = new Headers({
    "content-type": contentType,
    "x-content-type-options": "nosniff",
    "referrer-policy": "strict-origin-when-cross-origin",
    "permissions-policy": "camera=(), microphone=(), geolocation=()"
  });
  addDiscoveryHeaders(headers);
  return headers;
}

function addDiscoveryHeaders(headers) {
  headers.set("link", DISCOVERY_LINKS);
}
