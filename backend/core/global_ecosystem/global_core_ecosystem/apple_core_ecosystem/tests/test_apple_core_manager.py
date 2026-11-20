"""Structural and behavior tests for Apple Core manager contracts."""
from __future__ import annotations

import importlib
from pathlib import Path
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.domain_runtime import AppleCoreDomainManager

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
DOMAIN_PACKAGES = {
    "APP_STORE_AND_DISTRIBUTION": "apple_app_store_and_distribution_core_ecosystem",
    "APP_STORE_COMMERCE": "apple_app_store_commerce_core_ecosystem",
    "DEVICE_MANAGEMENT": "apple_device_management_domain_core_ecosystem",
    "CLOUD_DATA": "apple_cloud_data_core_ecosystem",
    "PAYMENTS_AND_COMMERCE": "apple_payments_and_commerce_core_ecosystem",
    "IDENTITY_AND_NOTIFICATIONS": "apple_identity_and_notifications_core_ecosystem",
}
PRODUCT_PACKAGES = [
    "apple_app_store_connect_core_ecosystem",
    "apple_app_store_server_core_ecosystem",
    "apple_device_management_core_ecosystem",
    "apple_icloud_cloudkit_core_ecosystem",
    "apple_pay_core_ecosystem",
    "apple_push_notification_core_ecosystem",
    "apple_sign_in_with_apple_core_ecosystem",
    "apple_storekit_core_ecosystem",
]
PACKAGE_IMPORT_ROOT = (
    "backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem"
)


class AppleCoreManagerTests(unittest.TestCase):
    def setUp(self):
        self.manager = get_manager()

    def test_status_is_catalog_only_and_not_live(self):
        status = self.manager.status()
        self.assertEqual(status["ecosystem_id"], "APPLE-CORE-ECOSYSTEM")
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)

    def test_product_catalog_has_eight_families(self):
        self.assertEqual(self.manager.list_products()["count"], 8)

    def test_offerings_inventory_has_eight_entries(self):
        offerings = self.manager.list_offerings()
        self.assertEqual(offerings["offering_count"], 8)
        self.assertEqual(offerings["live_connections_verified"], 0)

    def test_domain_inventory_is_consistent(self):
        domains = self.manager.list_domains()
        inventory = self.manager.list_domain_inventory()
        self.assertEqual(domains["domain_count"], len(DOMAIN_PACKAGES))
        self.assertEqual(sum(item["product_count"] for item in inventory), 8)
        self.assertEqual(set(DOMAIN_PACKAGES), {item["domain_id"] for item in inventory})

    def test_domain_managers_export_and_filter_canonical_inventory(self):
        package_root = PACKAGE_IMPORT_ROOT
        total = 0
        for domain_id, package_name in DOMAIN_PACKAGES.items():
            package = importlib.import_module(f"{package_root}.{package_name}")
            manager = package.get_manager()
            self.assertEqual(manager.DOMAIN_ID, domain_id)
            self.assertEqual(manager.status()["domain_id"], domain_id)
            result = manager.list_offerings()
            self.assertTrue(result["success"])
            total += result["count"]
        self.assertEqual(total, 8)

    def test_domain_readmes_are_present(self):
        for package_name in DOMAIN_PACKAGES.values():
            self.assertTrue((PACKAGE_ROOT / package_name / "README.md").is_file(), package_name)

    def test_product_family_packages_export_managers(self):
        for package_name in PRODUCT_PACKAGES:
            package = importlib.import_module(f"{PACKAGE_IMPORT_ROOT}.{package_name}")
            manager = package.get_manager()
            self.assertTrue(manager.status()["success"], package_name)

    def test_domain_manager_filters_and_lookup(self):
        manager = AppleCoreDomainManager("PAYMENTS_AND_COMMERCE")
        self.assertEqual(manager.list_offerings()["count"], 2)
        self.assertIsNotNone(manager.get_offering("storekit"))
        self.assertIsNone(manager.get_offering("not-registered"))
        self.assertIsNone(manager.get_offering(" "))

    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError):
            AppleCoreDomainManager("UNKNOWN")

    def test_dependency_map_covers_registered_product_families(self):
        self.assertEqual(len(self.manager.dependency_map()["edges"]), 8)


if __name__ == "__main__":
    unittest.main()
