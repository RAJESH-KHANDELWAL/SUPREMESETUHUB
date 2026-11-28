"""Google Core-style public manager, domain and master-catalog contract tests."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem import (
    GlobalAICoreDomainManager,
    get_manager,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.catalog import (
    list_ai_providers,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.domain_catalog import (
    AI_DOMAIN_DEFINITIONS,
)


class GlobalAICoreManagerTests(unittest.TestCase):
    def test_global_ai_manager_public_contract(self):
        manager = get_manager()
        self.assertEqual(manager.status()["ecosystem_id"], "GLOBAL-AI-CORE-ECOSYSTEM")
        self.assertEqual(manager.health()["provider_count"], len(list_ai_providers()))
        self.assertEqual(manager.list_products()["count"], len(list_ai_providers()))
        self.assertEqual(manager.list_domains()["domain_count"], 19)
        self.assertEqual(len(manager.list_domain_inventory()), 19)
        self.assertEqual(manager.get_product("openai")["id"], "openai_chatgpt")
        self.assertEqual(manager.get_offering("openai_chatgpt")["id"], "openai_chatgpt")
        self.assertTrue(manager.dependency_map()["success"])

    def test_global_ai_domain_manager_is_scoped_to_registered_domain(self):
        manager = GlobalAICoreDomainManager("GLOBAL_FOUNDATION_MODELS")
        self.assertEqual(manager.status()["domain_id"], "GLOBAL_FOUNDATION_MODELS")
        self.assertTrue(manager.list_products()["success"])
        self.assertIsNotNone(manager.get_product("openai_chatgpt"))

    def test_unknown_global_ai_domain_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "UNKNOWN_GLOBAL_AI_CORE_DOMAIN"):
            GlobalAICoreDomainManager("NOT_A_REAL_DOMAIN")

    def test_master_catalog_reference_preserves_engine_ownership(self):
        reference = get_manager().master_catalog_reference()
        self.assertEqual(reference["target_unique_entries"], 2468)
        self.assertEqual(
            reference["source_path"],
            "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
        )
        self.assertEqual(reference["owner_layer"], "GLOBAL_ENGINE_ECOSYSTEM")
        self.assertEqual(reference["access_mode"], "READ_ONLY_ON_DEMAND")
        self.assertTrue(reference["source_of_truth"])
        self.assertFalse(reference["loaded_by_reference_call"])

    def test_master_catalog_inventory_covers_every_current_source_row(self):
        inventory = get_manager().master_catalog_inventory()
        source_path = Path("backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
        source = json.loads(source_path.read_text(encoding="utf-8"))
        expected_counts = source["counts"]
        expansion = source["expansion"]

        self.assertTrue(inventory["success"])
        self.assertEqual(inventory["target_unique_entries"], 2468)
        self.assertEqual(inventory["target_unique_entries"], expansion["target_unique_entries"])
        self.assertEqual(inventory["current_unique_entries"], expected_counts["unique_catalogue_entries"])
        self.assertEqual(inventory["current_unique_entries"], expansion["current_unique_entries"])
        self.assertEqual(inventory["remaining_unique_entries"], expansion["remaining_unique_entries"])
        self.assertEqual(inventory["remaining_unique_entries"], 2468 - inventory["current_unique_entries"])
        self.assertEqual(inventory["source_numbered_entries"], expected_counts["source_numbered_entries"])
        self.assertEqual(inventory["cross_reference_entries"], expected_counts["cross_reference_entries"])
        self.assertEqual(inventory["section_count"], expected_counts["section_count"])
        self.assertEqual(len(inventory["entries"]), expected_counts["source_numbered_entries"])
        self.assertEqual(len(inventory["sections"]), expected_counts["section_count"])
        self.assertEqual(
            sum(entry["entry_kind"] != "cross_reference" for entry in inventory["entries"]),
            expected_counts["unique_catalogue_entries"],
        )

    def test_master_catalog_cross_references_are_preserved_and_resolvable(self):
        manager = get_manager()
        inventory = manager.master_catalog_inventory()
        references = [
            entry for entry in inventory["entries"]
            if entry["entry_kind"] == "cross_reference"
        ]
        for entry in references:
            canonical = manager.get_master_catalog_entry(entry["canonical_entry_id"])
            self.assertIsNotNone(canonical)
            self.assertNotEqual(canonical["entry_kind"], "cross_reference")
        self.assertIsNone(manager.get_master_catalog_entry("NOT_A_REAL_ENTRY"))

    def test_master_catalog_can_exclude_cross_reference_rows_without_losing_source(self):
        manager = get_manager()
        all_rows = manager.master_catalog_inventory(include_cross_references=True)
        unique_rows = manager.master_catalog_inventory(include_cross_references=False)
        self.assertEqual(
            len(unique_rows["entries"]),
            all_rows["source_numbered_entries"] - all_rows["cross_reference_entries"],
        )
        self.assertEqual(
            unique_rows["source_numbered_entries"],
            all_rows["source_numbered_entries"],
        )

    def test_domain_definitions_remain_nineteen(self):
        self.assertEqual(len(AI_DOMAIN_DEFINITIONS), 19)


if __name__ == "__main__":
    unittest.main()
