"""Tests for the mirrored GLOBAL CORE ECOSYSTEM hierarchy."""

import unittest

from backend.core.global_ecosystem.global_core_ecosystem import (
    ECOSYSTEM_ID,
    ECOSYSTEM_NAME,
    GlobalEcosystemManager,
    get_module,
    list_modules,
    status as core_ecosystem_status,
    tree as core_ecosystem_tree,
)


class TestGlobalCoreEcosystemHierarchy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manager = GlobalEcosystemManager()

    def test_health_uses_global_core_ecosystem(self):
        result = self.manager.health()
        self.assertTrue(result["success"])
        self.assertTrue(result["root_exists"])
        self.assertTrue(result["core_exists"])

    def test_public_package_entry_point_uses_canonical_registry_identity(self):
        self.assertEqual(ECOSYSTEM_ID, "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(ECOSYSTEM_NAME, "GLOBAL CORE ECOSYSTEM")
        result = core_ecosystem_status()
        self.assertEqual(result["ecosystem_id"], "GLOBAL-CORE-ECOSYSTEM")
        self.assertEqual(result["ecosystem"], "GLOBAL CORE ECOSYSTEM")
        self.assertTrue(result["success"])

    def test_public_package_lists_and_retrieves_core_modules(self):
        listing = list_modules()
        self.assertTrue(listing["success"])
        self.assertGreater(listing["count"], 0)
        self.assertTrue(listing["items"])

        result = get_module("GLOBAL-CORE-ECOSYSTEM")
        self.assertTrue(result["success"])
        self.assertEqual(
            result["item"]["ecosystem_id"],
            "GLOBAL-CORE-ECOSYSTEM",
        )

    def test_public_package_tree_exposes_core_hierarchy(self):
        result = core_ecosystem_tree()
        self.assertTrue(result["success"])
        self.assertEqual(result["id"], "GLOBAL-CORE-ECOSYSTEM")
        root = result["children"][0]
        core = next(
            child
            for child in root["children"]
            if child["ecosystem_id"] == "GLOBAL-CORE-ECOSYSTEM"
        )
        child_ids = {child["ecosystem_id"] for child in core["children"]}
        self.assertIn("GLOBAL-BUSINESS-CORE-ECOSYSTEM", child_ids)
        self.assertIn("GLOBAL-SERVER-CORE-ECOSYSTEM", child_ids)

    def test_core_ecosystem_is_registered_under_global_root(self):
        result = self.manager.get("GLOBAL-CORE-ECOSYSTEM")
        self.assertIsNotNone(result)
        self.assertEqual(result["name"], "GLOBAL CORE ECOSYSTEM")
        self.assertEqual(result["parent_id"], "GLOBAL-ECOSYSTEM")

    def test_core_service_ecosystems_are_children_of_core(self):
        expected = {
            "GLOBAL-BUSINESS-CORE-ECOSYSTEM",
            "GLOBAL-SERVER-CORE-ECOSYSTEM",
            "GLOBAL-DATABASE-CORE-ECOSYSTEM",
            "GLOBAL-STORAGE-CORE-ECOSYSTEM",
            "GLOBAL-SECURITY-CORE-ECOSYSTEM",
            "GLOBAL-API-CORE-ECOSYSTEM",
            "GLOBAL-AI-CORE-ECOSYSTEM",
            "GLOBAL-SEARCH-CORE-ECOSYSTEM",
            "GLOBAL-BACKUP-CORE-ECOSYSTEM",
            "GLOBAL-LOGGING-CORE-ECOSYSTEM",
            "GLOBAL-NOTIFICATIONS-CORE-ECOSYSTEM",
            "GLOBAL-SETTINGS-CORE-ECOSYSTEM",
        }
        records = {
            item["ecosystem_id"]: item
            for item in self.manager.list()["ecosystems"]
        }
        self.assertTrue(expected.issubset(records))
        for ecosystem_id in expected:
            self.assertEqual(
                records[ecosystem_id]["parent_id"],
                "GLOBAL-CORE-ECOSYSTEM",
                ecosystem_id,
            )

    def test_tree_places_core_under_global_ecosystem(self):
        tree = self.manager.tree()["tree"]
        children = {child["ecosystem_id"]: child for child in tree["children"]}
        core = children["GLOBAL-CORE-ECOSYSTEM"]
        core_children = {child["ecosystem_id"] for child in core["children"]}
        self.assertIn("GLOBAL-BUSINESS-CORE-ECOSYSTEM", core_children)
        self.assertIn("GLOBAL-SERVER-CORE-ECOSYSTEM", core_children)


if __name__ == "__main__":
    unittest.main()
