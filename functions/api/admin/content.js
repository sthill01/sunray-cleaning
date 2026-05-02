export async function onRequestGet(context) {
  const contentStatus = {
    status: "admin-api-ready",
    message: "Protect /admin/* with Cloudflare Access before enabling writes.",
    storage: {
      kvBindingConfigured: Boolean(context.env.SUNRAY_CONTENT),
      d1BindingConfigured: Boolean(context.env.SUNRAY_DB),
    },
    nextSteps: [
      "Create Cloudflare Access policy for /admin/*.",
      "Add D1 tables for pages, posts, service areas, testimonials, and FAQs.",
      "Use GitHub or a deploy hook to rebuild static pages after approved content changes.",
    ],
  };

  return Response.json(contentStatus);
}
