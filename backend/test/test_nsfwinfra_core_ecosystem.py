"""NSFWinfra Core control-plane tests; no provider network calls."""
from __future__ import annotations

import unittest
from pathlib import Path

from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.manager import (
    get_nsfwinfra_core_catalog,
)
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.contracts import (
    TenantContext,
)
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.manager import (
    CANONICAL_ENTRY_IDS,
    MASTER_CATALOG_PATH,
    get_manager,
)
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.module_service import (
    NSFWinfraProductCoreService,
)


class NSFWinfraCoreEcosystemTests(unittest.TestCase):
    def test_ten_existing_products_and_api_refs_exist(self):
        repo = Path(__file__).resolve().parents[2]
        items = get_nsfwinfra_core_catalog()["children"]
        self.assertEqual(len(items), 10)
        for item in items:
            self.assertTrue((repo / item["core_module"]).is_dir(), item["core_module"])
            self.assertTrue((repo / item["api_catalog_ref"]).is_dir(), item["api_catalog_ref"])

    def test_ai_layer_refs_resolve(self):
        repo = Path(__file__).resolve().parents[2]
        catalog = get_nsfwinfra_core_catalog()
        for key in ("ai_api_ref", "ai_core_ref"):
            self.assertTrue((repo / catalog[key]).is_dir(), catalog[key])
        self.assertIsNone(catalog["ai_provider_ref"])

    def test_unique_product_ids_and_coverage(self):
        items = get_nsfwinfra_core_catalog()["children"]
        ids = [item["ecosystem_id"] for item in items]
        self.assertEqual(len(ids), len(set(ids)))
        inventory = get_manager().list_domain_inventory()
        self.assertEqual(len(inventory), 21)
        self.assertTrue(
            all(item["product_count"] > 0 for item in inventory),
            [item["domain_id"] for item in inventory if not item["product_count"]],
        )

    def test_master_catalog_is_read_only_and_topics_exist(self):
        reference = get_manager().master_catalog()
        self.assertTrue(reference["available"])
        self.assertEqual(reference["target_unique_entries"], 2468)
        self.assertEqual(reference["current_unique_entries"], 246)
        self.assertEqual(reference["remaining_unique_entries"], 2222)
        self.assertEqual(reference["canonical_entry_ids"], list(CANONICAL_ENTRY_IDS))
        self.assertFalse(reference["catalogue_mutated"])
        self.assertTrue(MASTER_CATALOG_PATH.exists())
        self.assertTrue(all(reference["mapped_entry_presence"].values()))

    def test_catalog_status_is_not_live(self):
        status = get_manager().status()
        self.assertEqual(status["product_count"], 10)
        self.assertTrue(status["master_catalog"]["available"])
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)

    def test_tenant_context_and_capability_policy(self):
        service = NSFWinfraProductCoreService("NSFW-IMAGE-GENERATION-CORE-ECOSYSTEM")
        self.assertFalse(
            service.authorize_capability("IMAGE_GENERATION_CAPABILITY_DISCOVERY", None)["success"]
        )
        self.assertTrue(
            service.authorize_capability(
                "IMAGE_GENERATION_CAPABILITY_DISCOVERY", TenantContext("t1", "a1")
            )["success"]
        )
        self.assertFalse(
            service.authorize_capability("UNKNOWN_CAPABILITY", TenantContext("t1", "a1"))["success"]
        )

    def test_unknown_product_and_domain_rejected(self):
        with self.assertRaises(LookupError):
            NSFWinfraProductCoreService("not-a-product")
        with self.assertRaises(LookupError):
            get_manager().get_domain_manager("NO_DOMAIN")

    def test_catalog_defensive_copy(self):
        catalog = get_nsfwinfra_core_catalog()
        catalog["children"][0]["name"] = "corrupt"
        self.assertNotEqual(
            get_nsfwinfra_core_catalog()["children"][0]["name"], "corrupt"
        )

    def test_age_policy_is_default_deny(self):
        from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.policy import (
            NSFWinfraCorePolicy,
        )

        policy = NSFWinfraCorePolicy.age_and_content_policy()
        self.assertEqual(policy["default_adult_access"], "DENY")
        self.assertFalse(policy["execution_performed"])


if __name__ == "__main__":
    unittest.main()
