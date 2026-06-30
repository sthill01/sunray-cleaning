# Technical Debt

Last updated: 2026-06-30

## Known Debt

### Build Script Size

`tools/build-cloudflare-preview.py` handles many responsibilities. This is
useful for the current static pipeline but will become harder to maintain.

Potential future action:

- Extract route discovery, schema generation, platform file generation, gallery
  rendering, and link rewriting into focused modules after reports and tests are
  strong enough to protect behavior.

### GPT-Suffixed Source Pages

The source page naming convention still reflects the GPT preview phase.

Potential future action:

- Keep the convention until a safer content source model exists.
- Avoid renaming routes unless tests prove output parity.

### Documentation Was External

The project constitution and initialization protocol existed outside the repo.

Potential future action:

- Keep all governance docs in `/docs`.
- Update docs at the end of every sprint.

### Reporting Was Not First-Class

Before Operational Readiness, route, entity, schema, FAQ, image, and link
coverage were not generated as dedicated reports.

Potential future action:

- Keep report generation deterministic.
- Add CI or pre-commit checks only when report noise is under control.

### External Measurement State Is Unclear

The repo does not yet fully document GA4, Google Search Console, Cloudflare, or
AI monitoring state.

Potential future action:

- Add a measurement architecture doc after credentials and property IDs are
  confirmed.
