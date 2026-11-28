"""Global Cloud Core manager, domain, provider and master-catalog contract tests."""
from __future__ import annotations
import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_cloud_core_ecosystem import (
    CLOUD_DOMAIN_DEFINITIONS, GlobalCloudCoreDomainManager, get_manager,
)
from backend.global_ecosystem.global_cloud_ecosystem import (
    list_cloud_providers, list_cloud_workloads, validate_cloud_catalog, validate_cloud_workloads,
)

class GlobalCloudCoreManagerTests(unittest.TestCase):
    def test_public_manager_and_registry_contract(self):
        manager = get_manager()
        status = manager.status()
        self.assertEqual(status["ecosystem_id"], "GLOBAL-CLOUD-CORE-ECOSYSTEM")
        self.assertEqual(status["provider_count"], len(list_cloud_providers()))
        self.assertEqual(status["workload_count"], len(list_cloud_workloads()))
        self.assertTrue(status["success"], status["validation_errors"])
        self.assertEqual(validate_cloud_catalog(), ())
        self.assertEqual(validate_cloud_workloads(), ())
        self.assertEqual(manager.list_products()["count"], len(list_cloud_providers()))
        self.assertEqual(manager.get_product("aws")["id"], "aws")
        self.assertIsNone(manager.get_product("not_a_cloud_provider"))
        self.assertTrue(manager.dependency_map()["success"])

    def test_provider_origin_filter_and_taxonomies(self):
        manager = get_manager()
        india = manager.list_products(origin="india")
        self.assertTrue(india["products"])
        self.assertTrue(all(item["origin"] == "india" for item in india["products"]))
        self.assertEqual(manager.list_scopes()["count"], 10)
        self.assertEqual(manager.list_capabilities()["count"], 7)
        self.assertEqual(manager.list_offerings()["count"], len(list_cloud_workloads()))
        self.assertEqual(manager.get_offering("multi_cloud_sovereign")["id"], "multi_cloud_sovereign")

    def test_domain_inventory_is_complete_and_reconciles(self):
        manager = get_manager()
        inventory = manager.list_domain_inventory()
        summary = manager.list_domains()
        self.assertEqual(len(CLOUD_DOMAIN_DEFINITIONS), 10)
        self.assertEqual(summary["provider_count"], len(list_cloud_providers()))
        self.assertEqual(len(inventory), len(list_cloud_providers()))
        self.assertEqual(sum(item["provider_count"] for item in summary["domains"]), len(inventory))
        for item in inventory:
            self.assertIn(item["core_domain_id"], CLOUD_DOMAIN_DEFINITIONS)

    def test_domain_manager_is_scoped_and_unknown_domain_rejected(self):
        domain = GlobalCloudCoreDomainManager("STORAGE_AND_BACKUP")
        self.assertEqual(domain.status()["domain_id"], "STORAGE_AND_BACKUP")
        self.assertTrue(domain.list_products()["success"])
        self.assertIsNotNone(domain.get_product("dropbox"))
        with self.assertRaisesRegex(ValueError, "UNKNOWN_GLOBAL_CLOUD_CORE_DOMAIN"):
            GlobalCloudCoreDomainManager("NOT_A_REAL_DOMAIN")

    def test_workload_safety_and_filters(self):
        manager = get_manager()
        adult = manager.list_offerings(adult_industry=True)
        self.assertTrue(adult["offerings"])
        for item in adult["offerings"]:
            self.assertTrue(item["guardrails"])
            self.assertFalse(item["live_provider_connection_verified"])
        india = manager.list_offerings(region="bharat_india")
        self.assertTrue(all("bharat_india" in item["regions"] for item in india["offerings"]))

    def test_master_catalog_reference_preserves_engine_ownership(self):
        reference = get_manager().master_catalog_reference()
        self.assertEqual(reference["target_unique_entries"], 2468)
        self.assertEqual(reference["source_path"], "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
        self.assertEqual(reference["owner_layer"], "GLOBAL_ENGINE_ECOSYSTEM")
        self.assertEqual(reference["access_mode"], "READ_ONLY_ON_DEMAND")
        self.assertTrue(reference["source_of_truth"])
        self.assertFalse(reference["loaded_by_reference_call"])

    def test_master_catalog_inventory_reconciles_all_source_rows(self):
        inventory = get_manager().master_catalog_inventory()
        source = json.loads(Path("backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json").read_text(encoding="utf-8"))
        counts, expansion = source["counts"], source["expansion"]
        self.assertTrue(inventory["success"])
        self.assertEqual(inventory["target_unique_entries"], 2468)
        self.assertEqual(inventory["current_unique_entries"], counts["unique_catalogue_entries"])
        self.assertEqual(inventory["remaining_unique_entries"], expansion["remaining_unique_entries"])
        self.assertEqual(inventory["source_numbered_entries"], counts["source_numbered_entries"])
        self.assertEqual(inventory["cross_reference_entries"], counts["cross_reference_entries"])
        self.assertEqual(len(inventory["entries"]), counts["source_numbered_entries"])
        self.assertEqual(len(inventory["sections"]), counts["section_count"])

    def test_cross_references_are_resolvable_and_filterable(self):
        manager = get_manager()
        full = manager.master_catalog_inventory()
        unique = manager.master_catalog_inventory(include_cross_references=False)
        refs = [item for item in full["entries"] if item["entry_kind"] == "cross_reference"]
        for item in refs:
            canonical = manager.get_master_catalog_entry(item["canonical_entry_id"])
            self.assertIsNotNone(canonical)
            self.assertNotEqual(canonical["entry_kind"], "cross_reference")
        self.assertEqual(len(unique["entries"]), full["source_numbered_entries"] - full["cross_reference_entries"])
        self.assertEqual(unique["source_numbered_entries"], full["source_numbered_entries"])
        self.assertIsNone(manager.get_master_catalog_entry("NOT_A_REAL_ENTRY"))

if __name__ == "__main__":
    unittest.main()
