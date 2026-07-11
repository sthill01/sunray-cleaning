import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "import-local-gallery.py"
INCOMING = ROOT / "incoming-sunray-photos"


class PhotoIntakeTests(unittest.TestCase):
    def run_importer(self, batch_dir: Path, manifest: Path | None = None):
        env = os.environ.copy()
        env["LOCAL_GALLERY_INPUT_DIR"] = str(batch_dir.relative_to(ROOT))
        command = [sys.executable, str(SCRIPT), "--validate-only"]
        if manifest:
            command.extend(["--manifest", str(manifest)])
        return subprocess.run(command, cwd=ROOT, env=env, text=True, capture_output=True)

    def valid_payload(self, filename: str):
        return {
            "batch": {
                "id": "test-kamas-kitchen",
                "approvedBy": "Sun Ray owner",
                "consentConfirmed": True,
                "privacyChecked": True,
            },
            "photos": [
                {
                    "file": filename,
                    "approved": True,
                    "consentConfirmed": True,
                    "privacyChecked": True,
                    "locationVerified": True,
                    "containsSensitiveDetails": False,
                    "city": "Kamas",
                    "county": "Summit County",
                    "region": "Utah",
                    "service": "Recurring residential cleaning",
                    "room": "Kitchen",
                    "caption": "Verified recurring kitchen cleaning for a Kamas service-area home.",
                    "routes": ["/blog/kamas-oakley-recurring-kitchen-cleaning/"],
                }
            ],
        }

    def test_valid_manifest_passes(self):
        with tempfile.TemporaryDirectory(dir=INCOMING) as temp:
            batch = Path(temp)
            photo = batch / "kamas-kitchen.jpg"
            photo.write_bytes(b"test image bytes")
            manifest = batch / "photo-intake.json"
            manifest.write_text(json.dumps(self.valid_payload(photo.name)), encoding="utf-8")
            result = self.run_importer(batch, manifest)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Photo intake valid", result.stdout)

    def test_unlisted_photo_is_blocked(self):
        with tempfile.TemporaryDirectory(dir=INCOMING) as temp:
            batch = Path(temp)
            (batch / "unlisted.jpg").write_bytes(b"test image bytes")
            manifest = batch / "photo-intake.json"
            manifest.write_text(
                json.dumps({
                    "batch": {
                        "id": "test",
                        "approvedBy": "Sun Ray owner",
                        "consentConfirmed": True,
                        "privacyChecked": True,
                    },
                    "photos": [],
                }),
                encoding="utf-8",
            )
            result = self.run_importer(batch, manifest)
            self.assertEqual(result.returncode, 2)
            self.assertIn("Unlisted image files", result.stderr)

    def test_sensitive_details_are_blocked(self):
        with tempfile.TemporaryDirectory(dir=INCOMING) as temp:
            batch = Path(temp)
            photo = batch / "kamas-kitchen.jpg"
            photo.write_bytes(b"test image bytes")
            payload = self.valid_payload(photo.name)
            payload["photos"][0]["clientName"] = "Private Client"
            manifest = batch / "photo-intake.json"
            manifest.write_text(json.dumps(payload), encoding="utf-8")
            result = self.run_importer(batch, manifest)
            self.assertEqual(result.returncode, 2)
            self.assertIn("prohibited field clientName", result.stderr)


if __name__ == "__main__":
    unittest.main()
