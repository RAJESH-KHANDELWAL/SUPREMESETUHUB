"""Focused tests for the GLOBAL CORE ECOSYSTEM foundation and hierarchy."""

import unittest

from backend.core.global_ecosystem.global_core_ecosystem import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    GlobalEcosystemManager,
    get_module,
    list_modules,
    status as package_status,
    tree as package_tree,
)
from backend.core.global_ecosystem.global_core_ecosystem.manager import get_catalog
from backend.core.global_ecosystem.global_core_ecosystem.models import (
    GlobalEcosystemIdentity,
)
from backend.core.global_ecosystem.global_core_ecosystem.registry import (
    GlobalEcosystemRegistry,
)


class GlobalCoreEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.manager = GlobalEcosystemManager()

    def test_catalog_has_unique_ids_and_parent_first_order(self):
        records = get_catalog()
        seen = set()

        self.assertTrue(records)
        for record in records:
            ecosystem_id = record["ecosystem_id"]
            self.assertNotIn(ecosystem_id, seen)
            parent_id = record.get("parent_id")
            if parent_id:
                self.assertIn(parent_id, seen, ecosystem_id)
            seen.add(ecosystem_id)

    def test_global_root_and_core_are_healthy(self):
        health = self.manager.health()
        self.assertTrue(health["success"])
        self.assertTrue(health["root_exists"])
        self.assertTrue(health["core_exists"])
        self.assertEqual(
            self.manager.get("GLOBAL-CORE-ECOSYSTEM")["parent_id"],
            "GLOBAL-ECOSYSTEM",
        )

    def test_package_entry_points_expose_core_identity(self):
        self.assertEqual(ECOSYSTEM_ID, "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(ECOSYSTEM_NAME, "GLOBAL CORE ECOSYSTEM")
        result = package_status()
        self.assertTrue(result["success"])
        self.assertEqual(result["ecosystem_id"], ECOSYSTEM_ID)
        self.assertEqual(result["ecosystem"], ECOSYSTEM_NAME)

    def test_package_lists_and_retrieves_core_modules(self):
        listing = list_modules()
        self.assertTrue(listing["success"])
        self.assertGreater(listing["count"], 0)
        self.assertTrue(listing["items"])

        result = get_module(ECOSYSTEM_ID)
        self.assertTrue(result["success"])
        self.assertEqual(result["item"]["ecosystem_id"], ECOSYSTEM_ID)

    def test_core_service_children_are_registered_under_core(self):
        expected = {
            "GLOBAL-BUSINESS-CORE-ECOSYSTEM",
            "GLOBAL-DATABASE-CORE-ECOSYSTEM",
            "GLOBAL-STORAGE-CORE-ECOSYSTEM",
            "GLOBAL-API-CORE-ECOSYSTEM",
            "GLOBAL-AI-CORE-ECOSYSTEM",
            "GLOBAL-SECURITY-CORE-ECOSYSTEM",
            "GLOBAL-SERVER-CORE-ECOSYSTEM",
        }
        records = {
            item["ecosystem_id"]: item
            for item in self.manager.list()["ecosystems"]
        }
        self.assertTrue(expected.issubset(records))
        for ecosystem_id in expected:
            self.assertEqual(
                records[ecosystem_id]["parent_id"],
                ECOSYSTEM_ID,
                ecosystem_id,
            )

    def test_tree_places_core_under_global_root(self):
        result = package_tree()
        self.assertTrue(result["success"])
        self.assertEqual(result["id"], ECOSYSTEM_ID)
        self.assertTrue(result["children"])
        root = result["children"][0]
        core = next(
            child for child in root["children"]
            if child["ecosystem_id"] == ECOSYSTEM_ID
        )
        child_ids = {child["ecosystem_id"] for child in core["children"]}
        self.assertIn("GLOBAL-BUSINESS-CORE-ECOSYSTEM", child_ids)
        self.assertIn("GLOBAL-SERVER-CORE-ECOSYSTEM", child_ids)

    def test_registry_rejects_missing_parent(self):
        registry = GlobalEcosystemRegistry()
        identity = GlobalEcosystemIdentity(
            ecosystem_id="TEST-CHILD",
            name="TEST CHILD",
            ecosystem_type="TEST",
            parent_id="MISSING-PARENT",
        )
        with self.assertRaisesRegex(ValueError, "Parent ecosystem not found"):
            registry.register(identity)

    def test_manager_rejects_duplicate_and_missing_parent(self):
        duplicate = GlobalEcosystemIdentity(
            ecosystem_id=ECOSYSTEM_ID,
            name="DUPLICATE CORE",
            ecosystem_type="TEST",
        )
        self.assertEqual(
            self.manager.register(duplicate)["error"],
            "ECOSYSTEM_ALREADY_EXISTS",
        )

        orphan = GlobalEcosystemIdentity(
            ecosystem_id="TEST-ORPHAN-CORE",
            name="TEST ORPHAN CORE",
            ecosystem_type="TEST",
            parent_id="MISSING-PARENT",
        )
        self.assertEqual(
            self.manager.register(orphan)["error"],
            "PARENT_NOT_FOUND",
        )


if __name__ == "__main__":
    unittest.main()
