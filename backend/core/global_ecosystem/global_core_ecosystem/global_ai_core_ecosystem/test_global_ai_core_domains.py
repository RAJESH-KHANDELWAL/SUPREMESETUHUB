"""Google Core-style public manager, domain and master-catalog contract tests."""
from __future__ import annotations

import unittest

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

    def test_master_catalog_inventory_exposes_all_existing_rows_without_padding(self):
        inventory = get_manager().master_catalog_inventory()
        self.assertTrue(inventory["success"])
        self.assertEqual(inventory["target_unique_entries"], 2468)
        self.assertEqual(inventory["current_unique_entries"], 246)
        self.assertEqual(inventory["remaining_unique_entries"], 2222)
        self.assertEqual(inventory["source_numbered_entries"], 248)
        self.assertEqual(inventory["cross_reference_entries"], 2)
        self.assertEqual(inventory["section_count"], 13)
        self.assertEqual(len(inventory["entries"]), 248)
        self.assertEqual(len(inventory["sections"]), 13)
        self.assertEqual(
            sum(entry["entry_kind"] != "cross_reference" for entry in inventory["entries"]),
            246,
        )

    def test_master_catalog_cross_references_are_preserved_and_resolvable(self):
        manager = get_manager()
        sexual_health = manager.get_master_catalog_entry("S05_sexual_health")
        human_rights = manager.get_master_catalog_entry("S11_human_rights")
        self.assertEqual(sexual_health["canonical_entry_id"], "S04_sexual_health")
        self.assertEqual(human_rights["canonical_entry_id"], "S02_human_rights")
        self.assertIsNone(manager.get_master_catalog_entry("NOT_A_REAL_ENTRY"))

    def test_master_catalog_can_exclude_cross_reference_rows_without_losing_source(self):
        inventory = get_manager().master_catalog_inventory(include_cross_references=False)
        self.assertEqual(len(inventory["entries"]), 246)
        self.assertEqual(inventory["source_numbered_entries"], 248)
        self.assertEqual(inventory["cross_reference_entries"], 2)

    def test_domain_definitions_remain_nineteen(self):
        self.assertEqual(len(AI_DOMAIN_DEFINITIONS), 19)


if __name__ == "__main__":
    unittest.main()
