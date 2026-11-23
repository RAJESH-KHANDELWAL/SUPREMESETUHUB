"""Tests for GLOBAL WEB CORE metadata and layer boundaries."""
import unittest
from . import get_manager, get_provider, get_domain, list_domain_inventory, list_providers

class GlobalWebCoreTests(unittest.TestCase):
    def test_canonical_manager(self):
        manager = get_manager()
        self.assertEqual(manager.ECOSYSTEM_ID, "GLOBAL-WEB-CORE-ECOSYSTEM")
        self.assertEqual(manager.status()["status"], "CORE_CATALOG_ONLY")

    def test_provider_ids_are_unique_and_catalog_only(self):
        providers = list_providers()
        ids = [item["provider_id"] for item in providers]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {"aws", "cloudflare", "google", "microsoft"})
        self.assertTrue(all(item["live_connection_verified"] is False for item in providers))
        self.assertIsNotNone(get_provider("cloudflare"))

    def test_domain_ids_are_unique(self):
        domains = list_domain_inventory()
        ids = [item["domain_id"] for item in domains]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(domains), 20)
        self.assertIsNotNone(get_domain("DOMAINS_AND_DNS"))

    def test_layer_boundary(self):
        catalog = get_manager().catalog()
        self.assertFalse(catalog["remote_operations_enabled"])
        self.assertEqual(catalog["api_calls_performed"], 0)
        self.assertEqual(catalog["master_catalog"]["taxonomy_entries_added"], 0)

    def test_dependency_map_is_metadata_only(self):
        result = get_manager().dependency_map()
        self.assertTrue(result["success"])
        self.assertFalse(result["remote_operations_enabled"])

if __name__ == "__main__":
    unittest.main()
