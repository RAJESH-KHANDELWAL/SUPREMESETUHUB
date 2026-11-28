import json
import unittest
from pathlib import Path
from ..ecosystem_service import EcosystemService

ROOT = Path(__file__).resolve().parents[1]

class CloudflareStorageFoundationTests(unittest.TestCase):
    def test_safe_readiness(self):
        state = EcosystemService().describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["external_connections_verified"])
        self.assertFalse(state["storage_operations_enabled"])

    def test_google_style_direct_categories(self):
        manifest = json.loads((ROOT / "ecosystem_manifest.json").read_text(encoding="utf-8"))
        packages = sorted(p for p in ROOT.glob("global_cloudflare_*_storage_ecosystem") if p.is_dir())
        self.assertEqual(len(packages), manifest["category_folder_count"])
        self.assertFalse((ROOT / "categories").exists())
        self.assertFalse((ROOT / "providers").exists())
        for package in packages:
            for rel in ("README.md", "ecosystem_manifest.json", "api/routes.py", "models/record.py", "schemas/manifest.schema.json", "tests/test_foundation.py"):
                self.assertTrue((package / rel).is_file(), f"Missing {package.name}/{rel}")

if __name__ == "__main__":
    unittest.main()
