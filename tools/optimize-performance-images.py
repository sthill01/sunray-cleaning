from __future__ import annotations

import json
import re
from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "assets" / "perf"

IMAGES = [
    (
        "assets/team-action-2026-06/sun-ray-team-kitchen-cleaning-service.jpg",
        "sun-ray-team-kitchen-cleaning-service-768.webp",
        768,
        72,
    ),
    (
        "assets/team-action-2026-06/sun-ray-employee-kitchen-cabinet-cleaning.jpg",
        "sun-ray-employee-kitchen-cabinet-cleaning-768.webp",
        768,
        72,
    ),
    (
        "assets/team-action-2026-06/sun-ray-employee-sofa-detail-cleaning.jpg",
        "sun-ray-employee-sofa-detail-cleaning-768.webp",
        768,
        72,
    ),
    (
        "assets/team-action-2026-06/sun-ray-employee-stovetop-detail-cleaning.jpg",
        "sun-ray-employee-stovetop-detail-cleaning-768.webp",
        768,
        72,
    ),
    (
        "assets/team-action-2026-06/sun-ray-employee-shower-glass-cleaning.jpg",
        "sun-ray-employee-shower-glass-cleaning-768.webp",
        768,
        72,
    ),
    ("assets/logo-nav.png", "logo-nav-384.webp", 384, 82),
]


def webp_for(source: str, target_name: str, width: int, quality: int) -> Path:
    source_path = ROOT / source
    target_path = OUT / target_name
    with Image.open(source_path) as image:
        ratio = width / image.width
        height = round(image.height * ratio)
        resized = image.resize((width, height), Image.Resampling.LANCZOS)
        save_image = resized.convert("RGBA" if image.mode == "RGBA" else "RGB")
        save_image.save(target_path, "WEBP", quality=quality, method=6)
    return target_path


def svg_dimensions(path: Path) -> tuple[int, int] | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    width_match = re.search(r'\bwidth="([0-9.]+)', text)
    height_match = re.search(r'\bheight="([0-9.]+)', text)
    if width_match and height_match:
        return round(float(width_match.group(1))), round(float(height_match.group(1)))
    viewbox_match = re.search(r'\bviewBox="[-0-9.]+\s+[-0-9.]+\s+([0-9.]+)\s+([0-9.]+)"', text)
    if viewbox_match:
        return round(float(viewbox_match.group(1))), round(float(viewbox_match.group(2)))
    return None


def write_image_dimensions() -> Path:
    dimensions: dict[str, dict[str, int]] = {}
    for path in sorted((ROOT / "assets").rglob("*")):
        if not path.is_file():
            continue
        rel = path.relative_to(ROOT).as_posix()
        suffix = path.suffix.lower()
        size: tuple[int, int] | None = None
        if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
            with Image.open(path) as image:
                size = image.size
        elif suffix == ".svg":
            size = svg_dimensions(path)
        if size:
            dimensions[rel] = {"width": int(size[0]), "height": int(size[1])}
    target = DATA / "image-dimensions.json"
    target.write_text(json.dumps(dimensions, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return target


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for source, target_name, width, quality in IMAGES:
        target = webp_for(source, target_name, width, quality)
        print(f"{target.relative_to(ROOT)} {target.stat().st_size / 1024:.1f} KiB")
    dimensions = write_image_dimensions()
    print(f"{dimensions.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
