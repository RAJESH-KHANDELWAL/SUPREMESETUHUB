"""Validate Cloudflare's canonical product package scaffolds."""
from __future__ import annotations
import json
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.global_cloudflare_core_ecosystem.manager import get_manager

ROOT = Path(__file__).resolve().parents[1] / "core" / "global_ecosystem" / "global_core_ecosystem" / "global_cloudflare_core_ecosystem"
REQUIRED_FOLDERS = {"authentication", "capabilities", "docs", "events", "lifecycle", "models", "schemas", "security", "services", "tests"}

class CloudflareProductCorePackageTests(unittest.TestCase):
    def test_runtime_catalog_and_product_packages_match(self):
        catalog = get_manager().canonical_product_catalog()
        self.assertEqual(catalog["catalog_validation"], [])
        self.assertEqual(len(catalog["products"]), 10)
        self.assertFalse(catalog["live_connection_verified"])
        seen = set()
        for product in catalog["products"]:
            product_id = product["id"]
            with self.subTest(product=product_id):
                self.assertNotIn(product_id, seen)
                seen.add(product_id)
                package = ROOT / f"{product_id}_cloudflare_core_ecosystem"
                self.assertTrue(package.is_dir())
                manifest = json.loads((package / "ecosystem_manifest.json").read_text(encoding="utf-8"))
                self.assertEqual(manifest["provider"], "cloudflare")
                self.assertEqual(manifest["product_id"], product_id)
                self.assertEqual(manifest["product_name"], product["name"])
                self.assertEqual(manifest["category"], product["category"])
                self.assertEqual(manifest["capabilities"], list(product["capabilities"]))
                self.assertEqual(manifest["core_status"], "CORE_CATALOG_ONLY")
                self.assertFalse(manifest["live_connection"])
                self.assertIsNone(manifest["api_catalog_ref"])
                for required in ("README.md", "__init__.py", "contracts.py", "ecosystem_config.py", "authentication/contract.php"):
                    self.assertTrue((package / required).is_file(), f"{product_id}/{required}")
                for folder in REQUIRED_FOLDERS:
                    self.assertTrue((package / folder).is_dir(), f"{product_id}/{folder}")
    def test_manager_catalog_is_read_only_runtime_projection(self):
        catalog = get_manager().canonical_product_catalog()
        self.assertEqual(catalog["runtime_source_of_record"], "backend/global_ecosystem/global_cloudflare_ecosystem/catalog.py")
        self.assertTrue(all(p["status"] == "CORE_CATALOG_ONLY" for p in catalog["products"]))
        self.assertTrue(all(p["live_connection"] is False for p in catalog["products"]))

if __name__ == "__main__":
    unittest.main()
