#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    from PIL import Image, ImageOps
except ImportError as error:
    raise SystemExit(
        "Missing Pillow. Install it with: python -m pip install pillow pillow-heif"
    ) from error

try:
    import pillow_heif

    pillow_heif.register_heif_opener()
except ImportError:
    pillow_heif = None


ROOT = Path(__file__).resolve().parents[1]
INPUT_DIR = ROOT / os.environ.get("LOCAL_GALLERY_INPUT_DIR", "incoming-sunray-photos")
DATA_PATH = ROOT / "data" / "job-gallery.json"
ASSET_DIR = ROOT / os.environ.get(
    "LOCAL_GALLERY_ASSET_DIR",
    f"assets/job-gallery-{datetime.now().strftime('%Y-%m')}",
)
MAX_EDGE = int(os.environ.get("LOCAL_GALLERY_MAX_EDGE", "1800"))
JPEG_QUALITY = int(os.environ.get("LOCAL_GALLERY_JPEG_QUALITY", "88"))
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
if pillow_heif is not None:
    SUPPORTED_EXTENSIONS.update({".heic", ".heif"})


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def slugify(value: str, limit: int = 90) -> str:
    slug = clean_text(value).lower()
    slug = slug.replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = re.sub(r"^-+|-+$", "", slug)
    return slug[:limit] or "photo"


def humanize(value: str) -> str:
    value = re.sub(r"[_\-]+", " ", Path(value).stem)
    value = re.sub(r"\b(img|dsc|photo|cleaning|sun|ray)\b", " ", value, flags=re.I)
    return clean_text(value)


def infer_room(text: str) -> str:
    value = text.lower()
    if re.search(r"\b(kitchen|island|counter|stove|oven|sink|backsplash|pantry)\b", value):
        return "Kitchen"
    if re.search(r"\b(bathroom|bath|shower|tub|toilet|vanity|mirror)\b", value):
        return "Bathroom"
    if re.search(r"\b(bedroom|bed|bunk|linen|sheets)\b", value):
        return "Bedroom"
    if re.search(r"\b(living|family room|sofa|couch|fireplace|great room)\b", value):
        return "Living room"
    if re.search(r"\b(entry|mudroom|foyer|hallway)\b", value):
        return "Entry"
    if re.search(r"\b(laundry|washer|dryer)\b", value):
        return "Laundry room"
    return "Home"


def infer_service(text: str) -> str:
    value = text.lower()
    if re.search(r"\b(airbnb|vrbo|short[- ]term|vacation rental|turnover|guest|checkout|check-in|rental)\b", value):
        return "Airbnb and VRBO turnover cleaning"
    if re.search(r"\b(move[- ]?in|move[- ]?out|moving)\b", value):
        return "Move-in and move-out cleaning"
    if re.search(r"\b(deep|detail|spring clean|seasonal|post[- ]ski|reset)\b", value):
        return "Deep cleaning"
    if re.search(r"\b(recurring|weekly|biweekly|monthly|maintenance)\b", value):
        return "Recurring residential cleaning"
    return "Residential house cleaning"


def infer_location(text: str) -> dict[str, str]:
    value = text.lower()
    region = os.environ.get("LOCAL_GALLERY_DEFAULT_REGION", "Utah")
    if re.search(r"\b(midway|homestead|interlaken|deer creek)\b", value):
        return {"location": f"Midway, {region}", "city": "Midway", "county": "Wasatch County", "region": region}
    if re.search(r"\b(heber|red ledges|timber lakes|charleston|daniels|jordanelle)\b", value):
        return {"location": f"Heber City, {region}", "city": "Heber City", "county": "Wasatch County", "region": region}
    if re.search(r"\b(deer valley|canyons|old town|park meadows|prospector|silver springs|jeremy ranch|promontory|park city)\b", value):
        return {"location": f"Park City, {region}", "city": "Park City", "county": "Summit County", "region": region}
    if "wasatch county" in value:
        return {"location": f"Wasatch County, {region}", "city": "Heber City", "county": "Wasatch County", "region": region}
    if "summit county" in value:
        return {"location": f"Summit County, {region}", "city": "Park City", "county": "Summit County", "region": region}
    city = os.environ.get("LOCAL_GALLERY_DEFAULT_CITY", "Park City")
    county = os.environ.get("LOCAL_GALLERY_DEFAULT_COUNTY", "Summit County")
    return {"location": f"{city}, {region}", "city": city, "county": county, "region": region}


def routes_for(service: str, city: str, county: str) -> list[str]:
    routes = {
        "/",
        "/gallery/",
        "/services/",
        "/service-areas/",
        "/about/",
        "/contact/",
    }
    if "Airbnb" in service or "VRBO" in service:
        routes.add("/services/short-term-rental-cleaning/")
    if "Move-in" in service:
        routes.add("/services/move-in-move-out-cleaning/")
    if "Deep" in service:
        routes.add("/services/deep-cleaning/")
    if "Recurring" in service or "Residential" in service:
        routes.add("/services/recurring-cleaning/")
    if city == "Park City":
        routes.add("/service-location/park-city/")
    if city == "Heber City":
        routes.add("/service-location/heber-city/")
    if city == "Midway":
        routes.add("/service-location/midway/")
    if county == "Summit County":
        routes.add("/service-location/summit-county/")
    if county == "Wasatch County":
        routes.add("/service-location/wasatch-county/")
    return sorted(routes)


def sha1(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def read_gallery() -> list[dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def image_files() -> list[Path]:
    if not INPUT_DIR.exists():
        return []
    return sorted(
        path
        for path in INPUT_DIR.rglob("*")
        if path.is_file()
        and path.suffix.lower() in SUPPORTED_EXTENSIONS
        and not any(part.startswith(".") for part in path.relative_to(INPUT_DIR).parts)
    )


def save_jpeg(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode not in {"RGB", "L"}:
            image = image.convert("RGB")
        if max(image.size) > MAX_EDGE:
            image.thumbnail((MAX_EDGE, MAX_EDGE), Image.Resampling.LANCZOS)
        image.save(target, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)


def build_item(source: Path, asset_rel: str, file_hash: str, rank: int) -> dict[str, Any]:
    context = clean_text(" ".join(source.relative_to(INPUT_DIR).parts))
    room = infer_room(context)
    service = infer_service(context)
    location = infer_location(context)
    descriptive = humanize(source.name)
    name = clean_text(f"{location['city']} {room} {service} photo")
    caption = (
        f"{room} cleaning photo from Sun Ray Cleaning Services"
        f" for {location['location']} homes."
    )
    if descriptive:
        caption = f"{descriptive.title()} - {caption}"
    return {
        "asset": asset_rel,
        "sourceAsset": str(source.relative_to(ROOT)).replace("\\", "/"),
        "sourceHash": file_hash,
        "sourceRank": rank,
        "name": name,
        "room": room,
        "service": service,
        "location": location["location"],
        "city": location["city"],
        "county": location["county"],
        "region": location["region"],
        "alt": f"{room} after {service.lower()} by Sun Ray Cleaning Services in {location['location']}",
        "caption": caption,
        "keywords": [
            f"{location['city']} {service}".strip(),
            f"{room} cleaning",
            f"{location['county']} house cleaning",
            "Sun Ray Cleaning Services photos",
        ],
        "routes": routes_for(service, location["city"], location["county"]),
        "importedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "approved": True,
        "localUpload": True,
    }


def main() -> None:
    gallery = read_gallery()
    known_hashes = {str(item.get("sourceHash", "")) for item in gallery if item.get("sourceHash")}
    known_sources = {str(item.get("sourceAsset", "")) for item in gallery if item.get("sourceAsset")}
    max_rank = max([int(item.get("sourceRank", 0) or 0) for item in gallery] or [0])
    new_items: list[dict[str, Any]] = []
    skipped = 0

    for source in image_files():
        source_rel = str(source.relative_to(ROOT)).replace("\\", "/")
        file_hash = sha1(source)
        if file_hash in known_hashes or source_rel in known_sources:
            skipped += 1
            continue
        context = clean_text(" ".join(source.relative_to(INPUT_DIR).parts))
        location = infer_location(context)
        service = infer_service(context)
        room = infer_room(context)
        basename = "-".join(
            [
                "sun-ray",
                slugify(location["city"] or location["county"]),
                slugify(service),
                slugify(room),
                file_hash[:10],
            ]
        )
        target = ASSET_DIR / f"{basename}.jpg"
        save_jpeg(source, target)
        asset_rel = str(target.relative_to(ROOT)).replace("\\", "/")
        max_rank += 1
        new_items.append(build_item(source, asset_rel, file_hash, max_rank))

    if new_items:
        DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
        DATA_PATH.write_text(json.dumps(new_items + gallery, indent=2) + "\n", encoding="utf-8")

    print(
        f"Local gallery import complete. New photos: {len(new_items)}. "
        f"Skipped existing photos: {skipped}. Input: {INPUT_DIR.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
