"""Structural and behavior tests for Apple Core manager contracts."""
import unittest
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.domain_runtime import AppleCoreDomainManager

class AppleCoreManagerTests(unittest.TestCase):
    def setUp(self): self.manager = get_manager()
    def test_status_is_catalog_only_and_not_live(self):
        status = self.manager.status()
        self.assertEqual(status["ecosystem_id"], "APPLE-CORE-ECOSYSTEM")
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)
    def test_product_catalog_has_eight_families(self):
        products = self.manager.list_products()
        self.assertEqual(products["count"], 8)
    def test_offerings_inventory_has_eight_entries(self):
        offerings = self.manager.list_offerings()
        self.assertEqual(offerings["offering_count"], 8)
        self.assertEqual(offerings["live_connections_verified"], 0)
    def test_domain_inventory_is_consistent(self):
        domains = self.manager.list_domains()
        self.assertEqual(domains["domain_count"], 6)
        inventory = self.manager.list_domain_inventory()
        self.assertEqual(sum(x["product_count"] for x in inventory), 8)
    def test_domain_manager_filters(self):
        m = AppleCoreDomainManager("PAYMENTS_AND_COMMERCE")
        self.assertEqual(m.list_offerings()["count"], 2)
        self.assertIsNotNone(m.get_offering("storekit"))
        self.assertIsNone(m.get_offering("not-registered"))
    def test_unknown_domain_rejected(self):
        with self.assertRaises(ValueError): AppleCoreDomainManager("UNKNOWN")
    def test_dependency_map_has_all_products(self):
        self.assertEqual(len(self.manager.dependency_map()["edges"]), 8)

if __name__ == "__main__": unittest.main()
