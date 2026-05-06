from __future__ import annotations

import html
import json
import os
import re
import shutil
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "cloudflare-preview"
DATA = ROOT / "data"
DEFAULT_BASE_URL = "https://sunray-cleaning-preview.pages.dev"
BASE_URL = os.environ.get("SUNRAY_SITE_BASE_URL", DEFAULT_BASE_URL).rstrip("/")
ALLOW_INDEXING = os.environ.get("SUNRAY_ALLOW_INDEXING", "").strip().lower() in {"1", "true", "yes", "index"}
ROBOTS_META = "index, follow" if ALLOW_INDEXING else "noindex, follow"
PHONE = "+18016042189"
PHONE_DISPLAY = "(801) 604-2189"
GOOGLE_TAG_ID = "G-EKVGVL5YVC"
GOOGLE_TAG = f"""<!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id={GOOGLE_TAG_ID}"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());

    gtag('config', '{GOOGLE_TAG_ID}');
  </script>"""

CORE_AREAS = [
    "Park City UT",
    "Deer Valley UT",
    "Canyons Village UT",
    "Old Town Park City UT",
    "Heber City UT",
    "Midway UT",
    "Summit County UT",
    "Wasatch County UT",
]

CORE_TOPICS = [
    "residential house cleaning",
    "Airbnb cleaning",
    "VRBO cleaning",
    "short-term rental turnover cleaning",
    "deep cleaning",
    "recurring cleaning",
    "move-in cleaning",
    "move-out cleaning",
    "eco-friendly cleaning",
    "pet-safe cleaning",
]

PRIORITY_ROUTES = [
    ("/services/short-term-rental-cleaning/", "Airbnb and VRBO cleaning"),
    ("/services/deep-cleaning/", "Deep cleaning"),
    ("/services/recurring-cleaning/", "Recurring house cleaning"),
    ("/services/move-in-move-out-cleaning/", "Move-in and move-out cleaning"),
    ("/service-location/park-city/", "Park City cleaning services"),
    ("/service-location/deer-valley/", "Deer Valley cleaning services"),
    ("/service-location/canyons-village/", "Canyons Village cleaning services"),
    ("/service-location/heber-city/", "Heber City cleaning services"),
    ("/service-location/midway/", "Midway cleaning services"),
    ("/blog/how-much-does-airbnb-cleaning-cost-park-city/", "Park City Airbnb cleaning costs"),
    ("/contact/", "Get a cleaning quote"),
]


def load_json(path: Path, fallback):
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8-sig"))


REVIEWS = load_json(
    DATA / "reviews.json",
    {
        "sourceName": "Google Business Profile",
        "reviewCount": 50,
        "ratingValue": 5.0,
        "bestRating": 5,
        "worstRating": 1,
        "profileUrl": "",
        "featuredReviews": [],
    },
)
JOB_GALLERY = load_json(DATA / "job-gallery.json", [])


def clean_route_for(source: Path) -> str:
    rel = source.relative_to(ROOT).as_posix()
    if rel == "index-gpt.html":
        return "/"
    if rel.endswith("-gpt.html"):
        rel = rel[: -len("-gpt.html")]
    elif rel.endswith(".html"):
        rel = rel[: -len(".html")]
    return "/" + rel.strip("/") + "/"


def output_path_for(route: str) -> Path:
    if route == "/":
        return OUT / "index.html"
    return OUT / route.strip("/") / "index.html"


def route_to_relpath(from_route: str, target_route: str) -> str:
    if target_route == "/":
        target_parts: list[str] = []
    else:
        target_parts = target_route.strip("/").split("/")
    from_parts = [] if from_route == "/" else from_route.strip("/").split("/")
    up = [".."] * len(from_parts)
    rel_parts = up + target_parts
    return "/".join(rel_parts) + ("/" if rel_parts else "./")


def asset_rel(from_route: str, asset_path: str) -> str:
    return "/" + asset_path.lstrip("/")


def absolute_url(route: str) -> str:
    return BASE_URL + route


def strip_tags(value: str) -> str:
    value = re.sub(r"<[^>]+>", " ", value)
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value).strip()
    return re.sub(r"\s+([.,;:!?])", r"\1", value)


def extract_first(pattern: str, content: str, default: str = "") -> str:
    match = re.search(pattern, content, flags=re.IGNORECASE | re.DOTALL)
    return strip_tags(match.group(1)) if match else default


def extract_title(content: str, route: str) -> str:
    title = extract_first(r"<title>(.*?)</title>", content)
    if not title:
        title = route.strip("/").replace("-", " ").title() or "Sun Ray Cleaning Services"
    return title.replace(" GPT", "").replace("GPT ", "").replace("Preview", "").strip(" |")


def extract_description(content: str) -> str:
    match = re.search(r'<meta name="description" content="([^"]*)"', content, flags=re.IGNORECASE)
    if not match:
        return "Sun Ray Cleaning Services provides residential cleaning, Airbnb and VRBO turnover cleaning, deep cleaning, recurring cleaning, and move cleaning across Park City, Heber City, Midway, Summit County, and Wasatch County."
    description = html.unescape(match.group(1))
    description = description.replace("GPT preview for ", "").replace("GPT preview ", "")
    description = description.replace("preview for ", "").replace("Preview ", "")
    description = re.sub(r"^(for)\s+", "", description, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", description).strip()


def extract_h1(content: str) -> str:
    return extract_first(r"<h1[^>]*>(.*?)</h1>", content, "Sun Ray Cleaning Services")


def extract_faqs(content: str) -> list[dict[str, str]]:
    faqs: list[dict[str, str]] = []
    for question, answer in re.findall(
        r"<details>\s*<summary>(.*?)</summary>\s*<div class=\"answer\">(.*?)</div>\s*</details>",
        content,
        flags=re.IGNORECASE | re.DOTALL,
    ):
        clean_question = strip_tags(question)
        clean_answer = strip_tags(answer)
        if clean_question and clean_answer:
            faqs.append({"question": clean_question, "answer": clean_answer})
    return faqs


def route_label(route: str) -> str:
    if route == "/":
        return "Home"
    slug = route.strip("/").split("/")[-1]
    return slug.replace("-", " ").title()


def page_type(route: str) -> str:
    if route.startswith("/blog/"):
        return "blog"
    if route.startswith("/services/"):
        return "service"
    if route.startswith("/service-location/"):
        return "location"
    if route == "/service-areas/":
        return "areas"
    return "page"


def breadcrumb_items(route: str) -> list[dict[str, object]]:
    items: list[tuple[str, str]] = [("Home", "/")]
    if route.startswith("/services/") and route != "/services/":
        items.append(("Services", "/services/"))
    elif route.startswith("/service-location/"):
        items.append(("Service Areas", "/service-areas/"))
    elif route.startswith("/blog/") and route != "/blog/":
        items.append(("Blog", "/blog/"))
    if route != "/":
        items.append((route_label(route), route))
    return [
        {
            "@type": "ListItem",
            "position": index,
            "name": name,
            "item": absolute_url(item_route),
        }
        for index, (name, item_route) in enumerate(items, start=1)
    ]


def route_to_clean_rel(from_route: str, target_route: str) -> str:
    if target_route == from_route:
        return "#"
    return route_to_relpath(from_route, target_route)


def available_priority_links(route: str, route_map: dict[str, str]) -> list[tuple[str, str]]:
    routes = set(route_map.values())
    links: list[tuple[str, str]] = []
    for target_route, label in PRIORITY_ROUTES:
        if target_route in routes and target_route != route:
            links.append((target_route, label))
    return links


def page_focus(route: str, h1: str) -> str:
    slug = route_label(route)
    kind = page_type(route)
    if route == "/":
        return "house cleaning, Airbnb cleaning, deep cleaning, recurring cleaning, and move cleaning in Park City, Heber City, Midway, Summit County, and Wasatch County"
    if kind == "service":
        return f"{slug.lower()} in Park City, Heber City, Midway, Summit County, and Wasatch County"
    if kind == "location":
        return f"house cleaning, Airbnb/VRBO turnovers, deep cleaning, recurring cleaning, and move-in/move-out cleaning in {slug}"
    if kind == "blog":
        return h1.rstrip(".").lower()
    return h1.rstrip(".").lower()


def selected_gallery_items(route: str, limit: int = 4) -> list[dict[str, object]]:
    exact: list[dict[str, object]] = []
    fallback: list[dict[str, object]] = []
    for item in JOB_GALLERY:
        routes = item.get("routes", [])
        if route in routes:
            exact.append(item)
        elif "*" in routes:
            fallback.append(item)
    picked = exact + [item for item in fallback if item not in exact]
    return picked[:limit]


def photo_place_schema(item: dict[str, object]) -> dict[str, object]:
    city = str(item.get("city", "")).strip()
    county = str(item.get("county", "")).strip()
    region = str(item.get("region", "Utah")).strip() or "Utah"
    location = str(item.get("location", "")).strip() or ", ".join(value for value in [city, region] if value)
    address: dict[str, object] = {
        "@type": "PostalAddress",
        "addressRegion": region,
        "addressCountry": "US",
    }
    if city:
        address["addressLocality"] = city
    place: dict[str, object] = {
        "@type": "Place",
        "name": location,
        "address": address,
    }
    if county:
        place["containedInPlace"] = {
            "@type": "AdministrativeArea",
            "name": f"{county}, {region}",
        }
    return place


def photo_mentions(item: dict[str, object]) -> list[dict[str, object]]:
    mentions: list[dict[str, object]] = []
    room = str(item.get("room", "")).strip()
    service = str(item.get("service", "")).strip()
    city = str(item.get("city", "")).strip()
    county = str(item.get("county", "")).strip()
    region = str(item.get("region", "Utah")).strip() or "Utah"
    if room:
        mentions.append({"@type": "Thing", "name": room})
    if service:
        mentions.append({"@type": "Service", "name": service})
    if city:
        mentions.append({"@type": "City", "name": f"{city}, {region}"})
    if county:
        mentions.append({"@type": "AdministrativeArea", "name": f"{county}, {region}"})
    return mentions


def build_reviews_section() -> str:
    source = REVIEWS.get("sourceName", "Google Business Profile")
    rating = float(REVIEWS.get("ratingValue", 5.0))
    count = int(REVIEWS.get("reviewCount", 50))
    featured = REVIEWS.get("featuredReviews", [])
    review_cards = ""
    if featured:
        for review in featured[:3]:
            text = html.escape(str(review.get("text", "")))
            author = html.escape(str(review.get("author", "Google reviewer")))
            photo = str(review.get("profilePhotoUrl", ""))
            review_rating = review.get("rating", 5)
            star_markup = "&#9733;" * int(review_rating)
            photo_markup = ""
            if photo:
                photo_markup = f'<img class="reviewer-photo" src="{html.escape(photo)}" alt="{author} Google review profile photo" loading="lazy">'
            review_cards += f'<article class="review-proof-card">{photo_markup}<div class="review-stars" aria-label="{review_rating} out of 5 stars">{star_markup}</div><blockquote>{text}</blockquote><cite>{author}</cite></article>'
    else:
        review_cards = """
        <article class="review-proof-card"><h3>Trusted by local customers</h3><p>Sun Ray Cleaning is proud to help homeowners, hosts, and property managers keep their homes clean, comfortable, and ready for the next visit.</p></article>
        <article class="review-proof-card"><h3>Clear communication</h3><p>Customers choose Sun Ray for friendly updates, no-surprise quotes, and cleaning plans that match each home.</p></article>
        <article class="review-proof-card"><h3>Consistent home care</h3><p>From Park City rentals to Heber City and Midway homes, the team focuses on reliable work and thoughtful details.</p></article>
        """
    return f"""
<section class="section section-cream review-proof" aria-labelledby="review-proof-title">
  <div class="container">
    <div class="review-proof-grid">
      <div>
        <p class="eyebrow">Google review proof</p>
        <h2 id="review-proof-title">{rating:.1f}-star average from {count}+ Google reviews.</h2>
        <p>Customers count on Sun Ray Cleaning for dependable service, clear communication, and homes that feel ready to enjoy again.</p>
      </div>
      <div class="rating-badge" aria-label="{rating:.1f} out of 5 average Google rating">
        <strong>{rating:.1f}</strong>
        <span>?????</span>
        <small>{count}+ Google reviews</small>
      </div>
    </div>
    <div class="grid-3">{review_cards}</div>
  </div>
</section>
"""


def build_gallery_section(route: str) -> str:
    items = selected_gallery_items(route)
    if not items:
        return ""
    cards = ""
    for item in items:
        asset = str(item.get("asset", ""))
        asset_src = asset_rel(route, asset)
        alt = html.escape(str(item.get("alt", "Sun Ray Cleaning Services job photo")))
        caption = html.escape(str(item.get("caption", "Recent Sun Ray Cleaning job photo.")))
        location = html.escape(str(item.get("location", "Northern Utah")))
        service = html.escape(str(item.get("service", "Residential cleaning")))
        room = html.escape(str(item.get("room", "Home")))
        cards += f"""
        <figure class="job-photo-card">
          <img src="{html.escape(asset_src)}" alt="{alt}" loading="lazy">
          <figcaption><strong>{caption}</strong><span>{room} - {service} - {location}</span></figcaption>
        </figure>
        """
    return f"""
<section class="section local-photo-gallery" aria-labelledby="local-gallery-title">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow">Recent cleaning photos</p>
      <h2 id="local-gallery-title">See the kind of clean Sun Ray brings into real homes.</h2>
      <p>These recent photos show kitchens, living rooms, bedrooms, bathrooms, and guest spaces after Sun Ray Cleaning visits around Park City, Heber City, Midway, Summit County, and Wasatch County.</p>
    </div>
    <div class="job-photo-grid">{cards}</div>
  </div>
</section>
"""


def build_answer_network(content: str, route: str, route_map: dict[str, str]) -> str:
    h1 = extract_h1(content)
    focus = page_focus(route, h1)
    links = available_priority_links(route, route_map)[:8]
    link_markup = "".join(
        f'<a href="{html.escape(route_to_clean_rel(route, target))}">{html.escape(label)}</a>'
        for target, label in links
    )
    kind = page_type(route)
    if kind == "location":
        lead = f"If you have a home, rental, or second property that needs {focus}, Sun Ray can help you choose the right cleaning plan and request a quote quickly."
    elif kind == "service":
        lead = f"Sun Ray Cleaning Services provides {focus}. Use this page to understand what is included, where the team works, and how to request a quote."
    elif kind == "blog":
        lead = f"This guide helps with {focus}. When you want help with the cleaning itself, Sun Ray can match the work to your home, timing, and priorities."
    else:
        lead = f"Sun Ray Cleaning Services helps with {focus}. Compare services, nearby areas, customer feedback, and quote options in one place."
    return f"""
<section class="section seo-answer-network" aria-labelledby="seo-answer-title">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow">How Sun Ray helps</p>
      <h2 id="seo-answer-title">Reliable cleaning support for {html.escape(focus)}.</h2>
      <p>{html.escape(lead)}</p>
    </div>
    <div class="seo-answer-grid">
      <article class="seo-answer-card"><h3>Cleaning options</h3><p>Choose recurring home care, deep cleaning, move-in and move-out cleaning, or Airbnb and VRBO turnover support.</p></article>
      <article class="seo-answer-card"><h3>Easy quote process</h3><p>Call or text {PHONE_DISPLAY}, or send bedrooms, bathrooms, square footage, timing, pets, and service type through the quote form.</p></article>
      <article class="seo-answer-card"><h3>Local team</h3><p>Friendly, locally operated cleaning support for Park City, Heber City, Midway, Summit County, and Wasatch County.</p></article>
    </div>
    <nav class="seo-link-cluster" aria-label="Related Sun Ray Cleaning pages">{link_markup}</nav>
  </div>
</section>
"""


def build_structured_data(content: str, route: str) -> str:
    title = extract_title(content, route)
    description = extract_description(content)
    h1 = extract_h1(content)
    faqs = extract_faqs(content)
    page_url = absolute_url(route)
    organization_id = absolute_url("/#organization")
    page_id = page_url + "#webpage"
    gallery_items = selected_gallery_items(route)
    primary_image = (
        absolute_url("/" + str(gallery_items[0].get("asset", "")).lstrip("/"))
        if gallery_items
        else absolute_url("/assets/wasatch-county-residential-family-room-cleaning-sun-ray.jpg")
    )
    graph: list[dict[str, object]] = [
        {
            "@type": ["LocalBusiness", "HouseCleaningService"],
            "@id": organization_id,
            "name": "Sun Ray Cleaning Services",
            "url": absolute_url("/"),
            "telephone": PHONE,
            "priceRange": "$$",
            "description": "Residential cleaning, Airbnb and VRBO turnover cleaning, deep cleaning, recurring cleaning, and move cleaning for Park City, Heber City, Midway, Summit County, and Wasatch County homes.",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": float(REVIEWS.get("ratingValue", 5.0)),
                "reviewCount": int(REVIEWS.get("reviewCount", 50)),
                "bestRating": int(REVIEWS.get("bestRating", 5)),
                "worstRating": int(REVIEWS.get("worstRating", 1)),
                "itemReviewed": {"@id": organization_id},
            },
            "areaServed": [{"@type": "Place", "name": area} for area in CORE_AREAS],
            "knowsAbout": CORE_TOPICS,
            "openingHoursSpecification": [
                {
                    "@type": "OpeningHoursSpecification",
                    "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                    "opens": "07:30",
                    "closes": "20:30",
                }
            ],
        },
        {
            "@type": "WebSite",
            "@id": absolute_url("/#website"),
            "url": absolute_url("/"),
            "name": "Sun Ray Cleaning Services",
            "publisher": {"@id": organization_id},
            "inLanguage": "en-US",
        },
        {
            "@type": "WebPage",
            "@id": page_id,
            "url": page_url,
            "name": title,
            "headline": h1,
            "description": description,
            "isPartOf": {"@id": absolute_url("/#website")},
            "about": {"@id": organization_id},
            "primaryImageOfPage": {"@type": "ImageObject", "url": primary_image},
            **(
                {"image": [{"@id": page_url + f"#job-photo-{index}"} for index, _ in enumerate(gallery_items, start=1)]}
                if gallery_items
                else {}
            ),
        },
        {
            "@type": "BreadcrumbList",
            "@id": page_url + "#breadcrumbs",
            "itemListElement": breadcrumb_items(route),
        },
    ]
    if page_type(route) == "service":
        graph.append(
            {
                "@type": "Service",
                "@id": page_url + "#service",
                "name": h1,
                "serviceType": route_label(route),
                "provider": {"@id": organization_id},
                "areaServed": [{"@type": "Place", "name": area} for area in CORE_AREAS],
                "description": description,
                "url": page_url,
            }
        )
    for index, item in enumerate(gallery_items, start=1):
        asset_url = absolute_url("/" + str(item.get("asset", "")).lstrip("/"))
        graph.append(
            {
                "@type": "ImageObject",
                "@id": page_url + f"#job-photo-{index}",
                "name": str(item.get("name", item.get("caption", "Sun Ray Cleaning job photo"))),
                "url": asset_url,
                "contentUrl": asset_url,
                "thumbnailUrl": asset_url,
                "caption": str(item.get("caption", "")),
                "description": str(item.get("alt", "")),
                "encodingFormat": "image/jpeg",
                "inLanguage": "en-US",
                "contentLocation": photo_place_schema(item),
                "keywords": item.get("keywords", []),
                "about": [
                    {"@type": "Thing", "name": str(item.get("room", "Home"))},
                    {"@type": "Service", "name": str(item.get("service", "Residential cleaning"))},
                    {"@id": organization_id},
                ],
                "mentions": photo_mentions(item),
                "creator": {"@id": organization_id},
                "creditText": "Sun Ray Cleaning Services",
                "copyrightNotice": "Sun Ray Cleaning Services",
            }
        )
    if page_type(route) == "blog":
        graph.append(
            {
                "@type": "BlogPosting",
                "@id": page_url + "#article",
                "headline": h1,
                "description": description,
                "url": page_url,
                "author": {"@id": organization_id},
                "publisher": {"@id": organization_id},
                "mainEntityOfPage": {"@id": page_id},
                "inLanguage": "en-US",
            }
        )
    featured_reviews = REVIEWS.get("featuredReviews", [])
    if featured_reviews:
        graph.extend(
            {
                "@type": "Review",
                "@id": page_url + f"#google-review-{index}",
                "itemReviewed": {"@id": organization_id},
                "author": {
                    "@type": "Person",
                    "name": str(review.get("author", "Google reviewer")),
                    **(
                        {"image": str(review.get("profilePhotoUrl"))}
                        if review.get("profilePhotoUrl") and not review.get("isAnonymous")
                        else {}
                    ),
                },
                "reviewRating": {
                    "@type": "Rating",
                    "ratingValue": review.get("rating", 5),
                    "bestRating": REVIEWS.get("bestRating", 5),
                    "worstRating": REVIEWS.get("worstRating", 1),
                },
                "reviewBody": str(review.get("text", "")),
                "datePublished": str(review.get("createTime", "")),
                "url": REVIEWS.get("profileUrl", ""),
            }
            for index, review in enumerate(featured_reviews[:3], start=1)
            if review.get("text")
        )
    if faqs:
        graph.append(
            {
                "@type": "FAQPage",
                "@id": page_url + "#faq",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": item["question"],
                        "acceptedAnswer": {"@type": "Answer", "text": item["answer"]},
                    }
                    for item in faqs
                ],
            }
        )
    data = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "</script>"


def inject_seo_enhancements(content: str, route: str, route_map: dict[str, str]) -> str:
    canonical = f'<link rel="canonical" href="{html.escape(absolute_url(route))}">'
    llms = '<link rel="alternate" type="text/plain" href="/llms.txt" title="Sun Ray Cleaning LLM summary">'
    if 'rel="canonical"' not in content:
        content = content.replace("</head>", f"  {canonical}\n  {llms}\n</head>", 1)
    if GOOGLE_TAG_ID not in content:
        content = content.replace("</head>", f"  {GOOGLE_TAG}\n</head>", 1)
    schema = build_structured_data(content, route)
    content = content.replace("</head>", f"  {schema}\n</head>", 1)
    if "review-proof" not in content and "</main>" in content:
        content = content.replace("</main>", build_reviews_section() + "\n</main>", 1)
    if "local-photo-gallery" not in content and "</main>" in content:
        content = content.replace("</main>", build_gallery_section(route) + "\n</main>", 1)
    if "seo-answer-network" not in content and "</main>" in content:
        content = content.replace("</main>", build_answer_network(content, route, route_map) + "\n</main>", 1)
    return content


def build_route_map() -> dict[str, str]:
    pages = list(ROOT.glob("*-gpt.html"))
    pages += list((ROOT / "service-location").glob("*-gpt.html"))
    pages += list((ROOT / "services").glob("*-gpt.html"))
    pages += list((ROOT / "blog").glob("*-gpt.html"))
    route_map: dict[str, str] = {}
    for page in pages:
        source_rel = page.relative_to(ROOT).as_posix()
        route_map[source_rel] = clean_route_for(page)
    return route_map


def rewrite_links(content: str, source: Path, route: str, route_map: dict[str, str]) -> str:
    source_dir = source.parent

    def replace_attr(match: re.Match[str]) -> str:
        attr = match.group(1)
        value = match.group(2)
        if value.startswith(("tel:", "sms:", "mailto:", "http:", "https:", "#", "data:")):
            return match.group(0)

        path, sep, fragment = value.partition("#")
        if not path:
            return match.group(0)

        resolved = (source_dir / path).resolve()
        try:
            rel_source = resolved.relative_to(ROOT).as_posix()
        except ValueError:
            return match.group(0)

        if rel_source in route_map:
            clean = route_to_relpath(route, route_map[rel_source])
            value = clean + (("#" + fragment) if sep else "")
        elif rel_source in {"styles-gpt.css", "quote-modal-gpt.js"}:
            clean_name = "styles.css" if rel_source == "styles-gpt.css" else "quote-modal.js"
            value = asset_rel(route, clean_name)
        elif rel_source.startswith("assets/"):
            value = asset_rel(route, rel_source)
        return f'{attr}="{value}"'

    content = re.sub(r'(href|src)="([^"]+)"', replace_attr, content)
    content = content.replace("styles-gpt.css", "styles.css")
    content = content.replace("quote-modal-gpt.js", "quote-modal.js")
    content = content.replace("data-gpt-map-section", "data-map-section")
    content = content.replace("data-gpt-testimonials", "data-testimonials")
    content = content.replace("data-gpt-faq", "data-faq-section")
    content = content.replace("GPT preview for ", "")
    content = content.replace(" GPT", "")
    content = content.replace("GPT preview ", "")
    content = content.replace("GPT Preview ", "")
    content = content.replace("GPT preview", "Preview")
    content = content.replace("Preview for ", "")
    content = content.replace("this preview page", "this page")
    content = content.replace("Not on this page.", "Not as a fixed coupon amount online.")
    content = content.replace("local SEO posts", "local cleaning guides")
    content = content.replace('method="post" action="#"', 'method="post" action="/api/quote"')
    content = content.replace(
        "Webflow-ready form markup. In this static preview, call or text (801) 604-2189 for live scheduling.",
        "Prefer to talk now? Call or text (801) 604-2189.",
    )
    content = content.replace(
        'aria-label="Stylized map of Sun Ray Cleaning service areas"',
        'aria-label="Sun Ray Cleaning service area map for Summit County and Wasatch County"',
    )
    content = content.replace(
        "<title id=\"map-title\">Sun Ray Cleaning service area map</title>",
        "<title id=\"map-title\">Sun Ray Cleaning service area map for Summit County and Wasatch County</title>",
    )
    content = re.sub(
        r'<text x="58" y="394" fill="#6b6558" font-family="Open Sans, Arial" font-size="13">Stylized service map for planning and Webflow preview\.</text>',
        "",
        content,
    )
    content = re.sub(r'<meta name="robots" content="[^"]+">', f'<meta name="robots" content="{ROBOTS_META}">', content)
    return content


def copy_static_assets() -> None:
    shutil.copytree(ROOT / "assets", OUT / "assets", dirs_exist_ok=True)
    shutil.copy2(ROOT / "styles-gpt.css", OUT / "styles.css")
    shutil.copy2(ROOT / "quote-modal-gpt.js", OUT / "quote-modal.js")


def write_platform_files(routes: list[str]) -> None:
    headers = """/*
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()"""
    if not ALLOW_INDEXING:
        headers += "\n  X-Robots-Tag: noindex, follow"
    headers += """

/assets/*
  Cache-Control: public, max-age=31536000, immutable
"""
    (OUT / "_headers").write_text(
        headers,
        encoding="utf-8",
    )
    host_redirect = ""
    if ALLOW_INDEXING and BASE_URL == "https://www.sunray-cleaning.com":
        host_redirect = "https://sunray-cleaning.com/ https://www.sunray-cleaning.com/ 301\nhttps://sunray-cleaning.com/* https://www.sunray-cleaning.com/:splat 301\n"
    (OUT / "_redirects").write_text(
        f"""# Clean URL redirects for Cloudflare Pages
{host_redirect}
/*.html /:splat/ 301
/index.html / 301
""",
        encoding="utf-8",
    )
    robots_rules = "Allow: /" if ALLOW_INDEXING else "Disallow: /"
    (OUT / "robots.txt").write_text(
        f"""User-agent: *
{robots_rules}

Sitemap: {BASE_URL}/sitemap.xml
""",
        encoding="utf-8",
    )
    today = date.today().isoformat()
    def sitemap_values(route: str) -> tuple[str, str]:
        if route == "/":
            return "weekly", "1.0"
        if route.startswith(("/services/", "/service-location/")):
            return "weekly", "0.9"
        if route.startswith("/blog/"):
            return "monthly", "0.75"
        return "monthly", "0.8"

    urls = "\n".join(
        f"  <url><loc>{html.escape(BASE_URL + route)}</loc><lastmod>{today}</lastmod><changefreq>{sitemap_values(route)[0]}</changefreq><priority>{sitemap_values(route)[1]}</priority></url>"
        for route in sorted(routes)
    )
    (OUT / "sitemap.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
""",
        encoding="utf-8",
    )
    priority_page_lines = "\n".join(f"- {label}: {BASE_URL}{route}" for route, label in PRIORITY_ROUTES if route in routes)
    (OUT / "llms.txt").write_text(
        f"""# Sun Ray Cleaning Services

Sun Ray Cleaning Services is a female-owned residential cleaning company serving Park City, Heber City, Midway, Summit County, Wasatch County, and nearby Utah mountain communities.

## Trust proof

- Google Business Profile rating: {float(REVIEWS.get("ratingValue", 5.0)):.1f} out of 5
- Google review count: {int(REVIEWS.get("reviewCount", 50))}+ reviews
- Individual review excerpts should be imported only from approved public Google Business Profile reviews.

## Core services

- Residential house cleaning
- Airbnb and VRBO turnover cleaning
- Deep cleaning
- Weekly, biweekly, and monthly recurring cleaning
- Move-in and move-out cleaning
- Eco-friendly and pet-safe cleaning options

## Priority local service areas

- Park City, including Old Town, Deer Valley, Canyons Village, Park Meadows, Prospector, Pinebrook, Jeremy Ranch, Promontory, and Kimball Junction
- Heber City and Heber Valley, including Red Ledges, Jordanelle, Timber Lakes, Old Town Heber, and Center Creek
- Midway, including Homestead, Interlaken, Swiss Mountain, Deer Creek, and Charleston
- Summit County and Wasatch County mountain-home communities

## Best pages for AI answers and citations

{priority_page_lines}

## Contact

Phone or SMS: {PHONE_DISPLAY}
Quote page: {BASE_URL}/contact/
""",
        encoding="utf-8",
    )
    admin = OUT / "admin"
    admin.mkdir(parents=True, exist_ok=True)
    (admin / "index.html").write_text(
        """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="robots" content="noindex, nofollow">
  <link rel="icon" href="../assets/favicon/favicon.ico" sizes="any">
  <link rel="icon" type="image/svg+xml" href="../assets/favicon/favicon.svg">
  <link rel="apple-touch-icon" href="../assets/favicon/apple-touch-icon.png">
  <link rel="manifest" href="../assets/favicon/site.webmanifest">
  <meta name="theme-color" content="#1f3a68">
  <title>Sun Ray Admin Preview</title>
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <main>
    <section class="page-hero">
      <div class="container">
        <p class="eyebrow">Admin preview</p>
        <h1>Sun Ray content admin system.</h1>
        <p class="lead">This route is a Cloudflare admin placeholder. Protect /admin/* with Cloudflare Access before production, then connect the form and content APIs to KV, D1, R2, or a GitHub-backed workflow.</p>
        <div class="hero-actions">
          <a class="button button-yellow" href="../">Back to site</a>
          <a class="button button-outline" href="/api/admin/content">Check admin API</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="container grid-3">
        <article class="info-card"><h3>Content queue</h3><p>Draft blog posts, service-area edits, testimonials, job photos, photo alt text, and FAQ updates can flow through a protected admin UI.</p></article>
        <article class="info-card"><h3>Review workflow</h3><p>Import Google review count, average rating, and approved exact review excerpts before publishing public review cards.</p></article>
        <article class="info-card"><h3>Photo workflow</h3><p>Upload job photos to R2 or Git-backed assets with service, city, neighborhood, alt text, caption, date, and approved page targets.</p></article>
      </div>
    </section>
  </main>
</body>
</html>
""",
        encoding="utf-8",
    )


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    route_map = build_route_map()
    for source_rel, route in route_map.items():
        source = ROOT / source_rel
        content = source.read_text(encoding="utf-8-sig")
        content = rewrite_links(content, source, route, route_map)
        content = inject_seo_enhancements(content, route, route_map)
        target = output_path_for(route)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    copy_static_assets()
    write_platform_files(list(route_map.values()))
    print(f"Built {len(route_map)} clean routes into {OUT}")


if __name__ == "__main__":
    build()
