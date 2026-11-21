"""Tests for GLOBAL WEBSITE CORE metadata and layer boundaries."""
import unittest
from . import get_manager, get_provider, get_domain, list_domain_inventory, list_providers, list_product_families

class GlobalWebsiteCoreTests(unittest.TestCase):
    def test_canonical_manager(self):
        manager = get_manager()
        self.assertEqual(manager.ECOSYSTEM_ID, "GLOBAL-WEBSITE-CORE-ECOSYSTEM")
        self.assertEqual(manager.status()["status"], "CORE_CATALOG_ONLY")

    def test_provider_registry_matches_existing_namespaces(self):
        providers = list_providers()
        ids = [item["provider_id"] for item in providers]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids), {"aws", "google", "microsoft", "vicetemple"})
        self.assertTrue(all(item["live_connection_verified"] is False for item in providers))
        self.assertIsNotNone(get_provider("google"))

    def test_domains_are_unique_and_families_resolve(self):
        domains = list_domain_inventory()
        ids = [item["domain_id"] for item in domains]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(domains), 20)
        for family in list_product_families():
            for domain_id in family["domain_ids"]:
                self.assertIsNotNone(get_domain(domain_id), domain_id)

    def test_master_catalog_is_read_only_and_canonical(self):
        catalog = get_manager().catalog()
        self.assertEqual(catalog["master_catalog"]["canonical_entry_ids"], ["S09_websites"])
        self.assertEqual(catalog["master_catalog"]["taxonomy_entries_added"], 0)

    def test_layer_boundary(self):
        catalog = get_manager().catalog()
        self.assertFalse(catalog["remote_operations_enabled"])
        self.assertEqual(catalog["api_calls_performed"], 0)
        self.assertTrue(all(p["remote_operations_enabled"] is False for p in catalog["providers"]))

    def test_domain_runtime_rejects_unknown_domain(self):
        manager = get_manager().get_domain_manager("DOMAIN_NAME_MANAGEMENT")
        self.assertEqual(manager.describe()["domain"]["domain_id"], "DOMAIN_NAME_MANAGEMENT")
        with self.assertRaises(ValueError):
            get_manager().get_domain_manager("NOT_A_REAL_DOMAIN")

if __name__ == "__main__":
    unittest.main()
