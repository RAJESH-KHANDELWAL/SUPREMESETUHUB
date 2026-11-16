"""Offline tests for Global Cloudflare Core contracts and product package parity."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_cloudflare_core_ecosystem.catalog import (
    get_cloudflare_core_catalog,
    validate_cloudflare_core_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_cloudflare_core_ecosystem.contracts import (
    CloudflareTenantContext,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_cloudflare_core_ecosystem.policy import (
    CloudflareCorePolicy,
    CloudflareCorePolicyError,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_cloudflare_core_ecosystem.service import (
    CloudflareCoreEcosystemService,
)

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FOLDERS = {
    "authentication", "capabilities", "docs", "events", "lifecycle",
    "models", "schemas", "security", "services", "tests",
}


class CloudflareCoreTests(unittest.TestCase):
    def test_runtime_catalog_is_valid_and_has_ten_products(self):
        self.assertEqual(validate_cloudflare_core_catalog(), ())
        self.assertEqual(len(get_cloudflare_core_catalog()["products"]), 10)

    def test_each_canonical_product_has_google_standard_package(self):
        for product in get_cloudflare_core_catalog()["products"]:
            package = ROOT / f"{product['id']}_cloudflare_core_ecosystem"
            self.assertTrue((package / "README.md").is_file())
            self.assertTrue((package / "ecosystem_config.py").is_file())
            self.assertTrue((package / "contracts.py").is_file())
            manifest = json.loads((package / "ecosystem_manifest.json").read_text())
            self.assertEqual(manifest["provider"], "cloudflare")
            self.assertEqual(manifest["product_id"], product["id"])
            self.assertFalse(manifest["live_connection"])
            self.assertTrue(all((package / folder).is_dir() for folder in REQUIRED_FOLDERS))
            self.assertTrue((package / "authentication" / "contract.php").is_file())

    def test_service_is_read_only_and_reports_no_live_connection(self):
        service = CloudflareCoreEcosystemService()
        status = service.status()
        self.assertEqual(status["product_count"], 10)
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)
        self.assertFalse(status["health"]["execution_performed"])
        self.assertFalse(status["health"]["persistence_performed"])


    def test_provider_is_registered_in_parent_global_core_catalog(self):
        from backend.core.global_ecosystem.global_core_ecosystem.catalog import get_catalog

        matches = [
            item for item in get_catalog()
            if item["ecosystem_id"] == "GLOBAL-CLOUDFLARE-CORE-ECOSYSTEM"
        ]
        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0]["parent_id"], "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(matches[0]["metadata"]["status"], "CORE_CATALOG_ONLY")
        self.assertFalse(matches[0]["metadata"]["live_connection_verified"])

    def test_tenant_context_validation(self):
        CloudflareCorePolicy.require_tenant_context(
            CloudflareTenantContext(tenant_id="tenant-1", actor_id="actor-1")
        )
        with self.assertRaises(CloudflareCorePolicyError):
            CloudflareCorePolicy.require_tenant_context(None)

    def test_capability_requires_catalog_membership(self):
        product = get_cloudflare_core_catalog()["products"][0]
        CloudflareCorePolicy.validate_capability(product, product["capabilities"][0])
        with self.assertRaises(CloudflareCorePolicyError):
            CloudflareCorePolicy.validate_capability(product, "UNREGISTERED_CAPABILITY")


if __name__ == "__main__":
    unittest.main()
