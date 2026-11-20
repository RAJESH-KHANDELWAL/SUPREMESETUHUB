"""Structural and behavior tests for Apple Core manager contracts."""
import unittest
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.domain_runtime import AppleCoreDomainManager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_app_store_and_distribution_core_ecosystem import get_manager as get_distribution_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_app_store_commerce_core_ecosystem import get_manager as get_commerce_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_device_management_domain_core_ecosystem import get_manager as get_device_domain_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_cloud_data_core_ecosystem import get_manager as get_cloud_data_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_payments_and_commerce_core_ecosystem import get_manager as get_payments_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.apple_identity_and_notifications_core_ecosystem import get_manager as get_identity_notifications_manager

class AppleCoreManagerTests(unittest.TestCase):
    def setUp(self): self.manager = get_manager()
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
        self.assertEqual(self.manager.list_domains()["domain_count"], 6)
        self.assertEqual(sum(x["product_count"] for x in self.manager.list_domain_inventory()), 8)
    def test_domain_manager_filters(self):
        m = AppleCoreDomainManager("PAYMENTS_AND_COMMERCE")
        self.assertEqual(m.list_offerings()["count"], 2)
        self.assertIsNotNone(m.get_offering("storekit"))
        self.assertIsNone(m.get_offering("not-registered"))
    def test_six_domain_packages_are_available(self):
        managers = [get_distribution_manager(), get_commerce_manager(), get_device_domain_manager(),
                    get_cloud_data_manager(), get_payments_manager(), get_identity_notifications_manager()]
        self.assertEqual(len(managers), 6)
        self.assertEqual(sum(m.list_offerings()["count"] for m in managers), 8)
    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError): AppleCoreDomainManager("UNKNOWN")
    def test_dependency_map_has_all_products(self):
        self.assertEqual(len(self.manager.dependency_map()["edges"]), 8)
if __name__ == "__main__": unittest.main()
