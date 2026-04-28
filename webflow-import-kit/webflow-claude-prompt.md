# Webflow Claude Pilot Prompt

Use this after connecting the official Webflow connector/MCP in Claude.

```text
We are testing a Webflow rebuild/import for Sun Ray Cleaning Services.

Important guardrails:
- Work only in a duplicate or staging Webflow site, not the production site.
- Do not publish to production.
- Before editing, identify the site/project you are connected to and ask me to confirm it.
- Preserve the brand: warm yellow, navy, cream, clean residential service feel.
- Preserve SEO intent for Park City, Heber City, Midway, Salt Lake County, Airbnb/VRBO cleaning, recurring cleaning, deep cleaning, and move cleaning.
- Prefer editable native Webflow elements over code embeds.

Task:
1. Review the page/imported structure I created with htflow.
2. Identify any messy classes, inaccessible headings, missing alt text, or mobile layout issues.
3. Normalize class names around a simple Sun Ray system:
   - sr-section
   - sr-container
   - sr-grid
   - sr-card
   - sr-button
   - sr-eyebrow
4. Keep the homepage sections in this order:
   - utility/nav
   - hero
   - trust strip
   - services
   - service areas
   - CTA
5. Set or recommend page SEO:
   - Title: Professional Home Cleaning in Park City & Heber, UT | Sun Ray Cleaning
   - Description: Trusted residential cleaning in Park City, Heber City, Midway and Salt Lake County. Female-owned, insured, eco-friendly cleaners for deep cleans, recurring service and Airbnb turnovers.
   - Canonical: https://www.sunray-cleaning.com/
6. Add JSON-LD only as page-level custom code if it cannot be represented natively.

After reviewing, give me:
- what you changed
- what still needs manual cleanup
- whether this is a good candidate to continue in Webflow
```

