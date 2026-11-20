"""Google Core-style public manager and domain contract tests."""
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

    def test_2468_master_catalog_is_referenced_not_loaded_or_counted_as_ai_providers(self):
        reference = get_manager().master_catalog_reference()
        self.assertEqual(reference["target_unique_entries"], 2468)
        self.assertEqual(
            reference["source_path"],
            "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json",
        )
        self.assertFalse(reference["loaded_by_global_ai_core"])
        self.assertNotEqual(len(list_ai_providers()), 2468)

    def test_domain_definitions_remain_nineteen(self):
        self.assertEqual(len(AI_DOMAIN_DEFINITIONS), 19)


if __name__ == "__main__":
    unittest.main()
