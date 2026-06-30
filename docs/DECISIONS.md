# Decisions

Date: 2026-06-30

This file records durable project decisions. Add new decisions when they affect
architecture, governance, standards, automation, or long-term direction.

## Decision 0001: Repository As Digital Twin

Status: accepted.

The repository is the authoritative digital representation of Sun Ray Cleaning.
Business knowledge, service definitions, locations, images, reviews, content
relationships, reports, and automation should increasingly live in structured,
reusable forms inside the repository.

Reason:

AI systems and future engineers need a durable source of truth that does not
depend on conversation history.

## Decision 0002: Website Remains The Product

Status: accepted.

The Repository Intelligence Layer is internal infrastructure. It exists to
improve the public website, AI authority, and customer conversion. It is not the
primary product.

Reason:

Internal tooling can easily absorb effort without improving customer outcomes.
The program must keep shipping public improvements.

## Decision 0003: Preserve The Cloudflare Pages Pipeline

Status: accepted.

The current static build through `tools/build-cloudflare-preview.py` and
`cloudflare-preview/` remains the deployment foundation unless a future decision
replaces it.

Reason:

The existing pipeline already generates clean routes, sitemap, robots,
structured data, headers, redirects, and `llms.txt`. Replacing it prematurely
would add risk.

## Decision 0004: Generated Reports Are Committed

Status: accepted.

Repository Intelligence reports should be committed unless they become too large
or noisy. Machine-readable report data should live under `/reports/data`.

Reason:

Reports are project memory. Future sessions should be able to inspect them
without regenerating first.

## Decision 0005: AI Recommendation Support Lives In The Build Pipeline

Status: accepted.

Recommendation-focused page links, `llms.txt` output, and structured data should
be generated or enhanced through the existing Cloudflare build pipeline whenever
possible.

Reason:

The site already centralizes clean routes, sitemap generation, canonical URLs,
structured data, internal answer-network links, and `llms.txt` in
`tools/build-cloudflare-preview.py`. Keeping AI recommendation support in that
pipeline prevents a second source of truth and makes future authority pages
easier to validate.
