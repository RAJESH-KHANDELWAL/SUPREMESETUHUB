"""Google Core-style manager and master-catalog contract tests."""
from __future__ import annotations
import json
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.global_app_core_ecosystem import get_manager
from backend.global_ecosystem.global_app_ecosystem.providers import list_app_providers, validate_app_provider_registry
from backend.global_ecosystem.global_app_ecosystem.scope import APP_SCOPE_DOMAINS, list_domain_ids

class GlobalAppCoreManagerTests(unittest.TestCase):
    def test_public_manager_contract(self):
        manager = get_manager()
        status = manager.status()
        self.assertEqual(status["ecosystem_id"], "GLOBAL-APP-CORE-ECOSYSTEM")
        self.assertEqual(status["provider_count"], len(list_app_providers()))
        self.assertEqual(status["domain_count"], len(APP_SCOPE_DOMAINS))
        self.assertTrue(status["provider_registry_valid"])
        self.assertEqual(manager.list_products()["count"], len(list_app_providers()))
        self.assertEqual(len(manager.list_domain_inventory()), len(list_domain_ids()))
        self.assertEqual(manager.get_product("google")["id"], "google")
        self.assertIsNone(manager.get_product("not_a_provider"))
        self.assertTrue(manager.dependency_map()["success"])

    def test_provider_registry_filters_and_taxonomies(self):
        self.assertEqual(validate_app_provider_registry(), ())
        india = get_manager().list_products(origin="india")
        self.assertTrue(all(item["origin"] == "india" for item in india["products"]))
        self.assertGreater(len(get_manager().list_app_types()), 0)
        self.assertGreater(len(get_manager().list_capability_groups()), 0)
        self.assertEqual(get_manager().validate_app_type("web_app")["id"], "web_app")

    def test_master_catalog_reference_preserves_engine_ownership(self):
        reference = get_manager().master_catalog_reference()
        self.assertEqual(reference["target_unique_entries"], 2468)
        self.assertEqual(reference["source_path"], "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
        self.assertEqual(reference["owner_layer"], "GLOBAL_ENGINE_ECOSYSTEM")
        self.assertEqual(reference["access_mode"], "READ_ONLY_ON_DEMAND")
        self.assertTrue(reference["source_of_truth"])
        self.assertFalse(reference["loaded_by_reference_call"])

    def test_master_catalog_inventory_reconciles_source_rows(self):
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

    def test_cross_references_resolve_and_can_be_filtered(self):
        manager = get_manager()
        full = manager.master_catalog_inventory()
        unique = manager.master_catalog_inventory(include_cross_references=False)
        refs = [x for x in full["entries"] if x["entry_kind"] == "cross_reference"]
        for ref in refs:
            canonical = manager.get_master_catalog_entry(ref["canonical_entry_id"])
            self.assertIsNotNone(canonical)
            self.assertNotEqual(canonical["entry_kind"], "cross_reference")
        self.assertEqual(len(unique["entries"]), full["source_numbered_entries"] - full["cross_reference_entries"])
        self.assertEqual(unique["source_numbered_entries"], full["source_numbered_entries"])
        self.assertIsNone(manager.get_master_catalog_entry("NOT_A_REAL_ENTRY"))

if __name__ == "__main__":
    unittest.main()
