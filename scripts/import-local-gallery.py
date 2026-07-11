#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
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
DEFAULT_MANIFEST = INPUT_DIR / "photo-intake.json"
MAX_EDGE = int(os.environ.get("LOCAL_GALLERY_MAX_EDGE", "1800"))
JPEG_QUALITY = int(os.environ.get("LOCAL_GALLERY_JPEG_QUALITY", "88"))
SUPPORTED_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff"}
if pillow_heif is not None:
    SUPPORTED_EXTENSIONS.update({".heic", ".heif"})

ALLOWED_COUNTIES = {"Summit County", "Wasatch County"}
ALLOWED_SERVICES = {
    "Airbnb and VRBO turnover cleaning",
    "Move-in and move-out cleaning",
    "Deep cleaning",
    "Recurring residential cleaning",
    "Residential house cleaning",
}
SENSITIVE_FIELDS = {
    "exactAddress",
    "streetAddress",
    "clientName",
    "doorCode",
    "accessCode",
    "licensePlate",
}


class IntakeError(ValueError):
    pass


def clean_text(value: str) -> str:
    return re.sub(r"\s+", " ", str(value)).strip()


def slugify(value: str, limit: int = 90) -> str:
    slug = clean_text(value).lower().replace("&", " and ")
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    return re.sub(r"^-+|-+$", "", slug)[:limit] or "photo"


def sha1(path: Path) -> str:
    digest = hashlib.sha1()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def read_gallery() -> list[dict[str, Any]]:
    if not DATA_PATH.exists():
        return []
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


def load_manifest(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise IntakeError(
            f"Photo intake manifest missing: {path}. Copy photo-intake.example.json "
            "to photo-intake.json and record verified job facts before importing."
        )
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except json.JSONDecodeError as error:
        raise IntakeError(f"Photo intake manifest is invalid JSON: {error}") from error
    if not isinstance(payload, dict):
        raise IntakeError("Photo intake manifest must be a JSON object.")
    return payload


def require_true(record: dict[str, Any], field: str, label: str) -> None:
    if record.get(field) is not True:
        raise IntakeError(f"{label} requires {field}=true.")


def safe_route(route: str) -> str:
    value = clean_text(route)
    if not value.startswith("/") or ".." in value or "?" in value or "#" in value:
        raise IntakeError(f"Unsafe or invalid route in photo intake manifest: {route!r}")
    return value if value.endswith("/") else f"{value}/"


def routes_for(service: str, city: str, county: str, extra_routes: list[str]) -> list[str]:
    routes = {"/", "/gallery/", "/services/", "/service-areas/", "/about/", "/contact/"}
    if "Airbnb" in service or "VRBO" in service:
        routes.add("/services/short-term-rental-cleaning/")
    if "Move-in" in service:
        routes.add("/services/move-in-move-out-cleaning/")
    if "Deep" in service:
        routes.add("/services/deep-cleaning/")
    if "Recurring" in service or "Residential" in service:
        routes.add("/services/recurring-cleaning/")

    city_routes = {
        "Park City": "/service-location/park-city/",
        "Heber City": "/service-location/heber-city/",
        "Midway": "/service-location/midway/",
        "Kamas": "/service-location/kamas/",
        "Oakley": "/service-location/oakley/",
        "Coalville": "/service-location/coalville/",
    }
    if city in city_routes:
        routes.add(city_routes[city])
    if county == "Summit County":
        routes.add("/service-location/summit-county/")
    if county == "Wasatch County":
        routes.add("/service-location/wasatch-county/")
    routes.update(safe_route(route) for route in extra_routes)
    return sorted(routes)


def validate_manifest(payload: dict[str, Any], files: list[Path]) -> dict[str, dict[str, Any]]:
    batch = payload.get("batch")
    photos = payload.get("photos")
    if not isinstance(batch, dict) or not isinstance(photos, list):
        raise IntakeError("Manifest requires a batch object and a photos array.")
    if not clean_text(batch.get("id", "")):
        raise IntakeError("Manifest batch.id is required.")
    if not clean_text(batch.get("approvedBy", "")):
        raise IntakeError("Manifest batch.approvedBy is required.")
    require_true(batch, "consentConfirmed", "Manifest batch")
    require_true(batch, "privacyChecked", "Manifest batch")

    records: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(photos):
        if not isinstance(raw, dict):
            raise IntakeError(f"photos[{index}] must be an object.")
        filename = clean_text(raw.get("file", "")).replace("\\", "/")
        label = f"photos[{index}] ({filename or 'missing file'})"
        if not filename or filename in records:
            raise IntakeError(f"{label} must have a unique file value.")
        if Path(filename).is_absolute() or ".." in Path(filename).parts:
            raise IntakeError(f"{label} must stay inside the incoming photo folder.")
        require_true(raw, "approved", label)
        require_true(raw, "consentConfirmed", label)
        require_true(raw, "privacyChecked", label)
        require_true(raw, "locationVerified", label)
        if raw.get("containsSensitiveDetails") is not False:
            raise IntakeError(f"{label} requires containsSensitiveDetails=false.")
        for field in SENSITIVE_FIELDS:
            if clean_text(raw.get(field, "")):
                raise IntakeError(f"{label} contains prohibited field {field}.")

        for field in ("city", "county", "region", "service", "room", "caption"):
            if not clean_text(raw.get(field, "")):
                raise IntakeError(f"{label} requires {field}.")
        if clean_text(raw["county"]) not in ALLOWED_COUNTIES:
            raise IntakeError(f"{label} county must be Summit County or Wasatch County.")
        if clean_text(raw["service"]) not in ALLOWED_SERVICES:
            raise IntakeError(f"{label} uses unsupported service {raw['service']!r}.")
        if len(clean_text(raw["caption"])) < 30:
            raise IntakeError(f"{label} caption must be at least 30 characters.")
        raw["routes"] = [safe_route(route) for route in raw.get("routes", [])]
        records[filename] = raw

    actual = {str(path.relative_to(INPUT_DIR)).replace("\\", "/") for path in files}
    missing_records = sorted(actual - set(records))
    missing_files = sorted(set(records) - actual)
    if missing_records:
        raise IntakeError("Unlisted image files: " + ", ".join(missing_records))
    if missing_files:
        raise IntakeError("Manifest files not found: " + ", ".join(missing_files))
    return records


def save_jpeg(source: Path, target: Path) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(source) as image:
        image = ImageOps.exif_transpose(image)
        if image.mode not in {"RGB", "L"}:
            image = image.convert("RGB")
        image.thumbnail((MAX_EDGE, MAX_EDGE), Image.Resampling.LANCZOS)
        # Saving a fresh JPEG intentionally strips source EXIF metadata.
        image.save(target, "JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)


def build_item(
    source: Path,
    record: dict[str, Any],
    batch: dict[str, Any],
    asset_rel: str,
    file_hash: str,
    rank: int,
) -> dict[str, Any]:
    city = clean_text(record["city"])
    county = clean_text(record["county"])
    region = clean_text(record.get("region", "Utah"))
    room = clean_text(record["room"])
    service = clean_text(record["service"])
    location = f"{city}, {region}" if city else f"{county}, {region}"
    caption = clean_text(record["caption"])
    alt = clean_text(record.get("alt", "")) or (
        f"{room} after {service.lower()} by Sun Ray Cleaning Services in {location}"
    )
    hashtags = ["#SunRayCleaning", "#UtahCleaning", "#HouseCleaning"]
    if city:
        hashtags.insert(1, f"#{re.sub(r'[^A-Za-z0-9]', '', city)}Cleaning")
    return {
        "asset": asset_rel,
        "sourceAsset": str(source.relative_to(ROOT)).replace("\\", "/"),
        "sourceHash": file_hash,
        "sourceRank": rank,
        "name": clean_text(record.get("name", "")) or f"{city or county} {room} {service} photo",
        "room": room,
        "service": service,
        "location": location,
        "city": city,
        "county": county,
        "region": region,
        "alt": alt,
        "caption": caption,
        "keywords": [
            f"{city or county} {service}",
            f"{room} cleaning",
            f"{county} house cleaning",
            "Sun Ray Cleaning Services photos",
        ],
        "routes": routes_for(service, city, county, list(record.get("routes", []))),
        "importedAt": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "approved": True,
        "localUpload": True,
        "proof": {
            "batchId": clean_text(batch["id"]),
            "jobId": clean_text(record.get("jobId", "")),
            "approvedBy": clean_text(batch["approvedBy"]),
            "consentConfirmed": True,
            "privacyChecked": True,
            "locationVerified": True,
            "locationPrecision": "city-or-county-only",
        },
        "socialReady": {
            "caption": caption,
            "hashtags": hashtags,
            "channels": ["facebook", "instagram", "googleBusinessProfile"],
            "status": "draft",
        },
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Import approved, provenance-checked Sun Ray job photos.")
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--validate-only", action="store_true", help="Validate the batch without writing files.")
    parser.add_argument("--dry-run", action="store_true", help="Validate and preview generated gallery records.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = image_files()
    if not files:
        print(f"No incoming photos found in {INPUT_DIR.relative_to(ROOT)}. Nothing to import.")
        return 0

    try:
        payload = load_manifest(args.manifest)
        records = validate_manifest(payload, files)
    except IntakeError as error:
        print(f"Photo intake blocked: {error}", file=sys.stderr)
        return 2

    gallery = read_gallery()
    known_hashes = {str(item.get("sourceHash", "")) for item in gallery if item.get("sourceHash")}
    known_sources = {str(item.get("sourceAsset", "")) for item in gallery if item.get("sourceAsset")}
    max_rank = max([int(item.get("sourceRank", 0) or 0) for item in gallery] or [0])
    new_items: list[dict[str, Any]] = []
    skipped = 0

    for source in files:
        source_rel = str(source.relative_to(ROOT)).replace("\\", "/")
        manifest_rel = str(source.relative_to(INPUT_DIR)).replace("\\", "/")
        file_hash = sha1(source)
        if file_hash in known_hashes or source_rel in known_sources:
            skipped += 1
            continue
        record = records[manifest_rel]
        basename = "-".join(
            [
                "sun-ray",
                slugify(record.get("city") or record["county"]),
                slugify(record["service"]),
                slugify(record["room"]),
                file_hash[:10],
            ]
        )
        target = ASSET_DIR / f"{basename}.jpg"
        asset_rel = str(target.relative_to(ROOT)).replace("\\", "/")
        max_rank += 1
        item = build_item(source, record, payload["batch"], asset_rel, file_hash, max_rank)
        new_items.append(item)
        if not (args.validate_only or args.dry_run):
            save_jpeg(source, target)

    if args.dry_run:
        print(json.dumps(new_items, indent=2))
    elif args.validate_only:
        print(f"Photo intake valid. New photos ready: {len(new_items)}. Existing duplicates: {skipped}.")
    elif new_items:
        DATA_PATH.write_text(json.dumps(new_items + gallery, indent=2) + "\n", encoding="utf-8")

    print(
        f"Local gallery import complete. New photos: {len(new_items)}. "
        f"Skipped existing photos: {skipped}. Input: {INPUT_DIR.relative_to(ROOT)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
