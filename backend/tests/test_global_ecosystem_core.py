"""Tests for the CORE GLOBAL ECOSYSTEM."""

import unittest

from backend.core.global_ecosystem.manager import GlobalEcosystemManager


class TestGlobalEcosystemCore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.manager = GlobalEcosystemManager()

    def test_root_exists(self):
        result = self.manager.get("GLOBAL-ECOSYSTEM")

        self.assertIsNotNone(result)
        self.assertEqual(
            result["ecosystem_id"],
            "GLOBAL-ECOSYSTEM",
        )

    def test_registry_contains_catalog(self):
        result = self.manager.list()

        self.assertTrue(result["success"])
        self.assertEqual(
            result["count"],
            len(result["ecosystems"]),
        )
        self.assertGreaterEqual(result["count"], 1)

    def test_health_reports_foundation(self):
        result = self.manager.health()

        self.assertTrue(result["success"])
        self.assertTrue(result["root_exists"])
        self.assertTrue(result["core_exists"])

    def test_google_core_ecosystem_is_registered(self):
        self.assertTrue(self.manager.exists("GLOBAL-GOOGLE-CORE-ECOSYSTEM"))
        self.assertTrue(self.manager.exists("GLOBAL-GOOGLE-API-CORE-ECOSYSTEM"))
        self.assertTrue(self.manager.exists("GLOBAL-GOOGLE-PRODUCT-CORE-ECOSYSTEM"))
        self.assertTrue(self.manager.exists("GLOBAL-GOOGLE-GEMINI-CORE-ECOSYSTEM"))

    def test_google_core_catalog_exposes_safe_readiness(self):
        result = self.manager.google_catalog_status()
        self.assertTrue(result["success"])
        self.assertGreaterEqual(result["api_family_count"], 20)
        self.assertGreaterEqual(result["product_count"], 50)
        self.assertFalse(result["live_connection_verified"])
        self.assertEqual(result["token_storage_status"], "NOT_IMPLEMENTED")

    def test_people_category_exists(self):
        self.assertTrue(
            self.manager.exists("GLOBAL-PEOPLE-ECOSYSTEM")
        )

    def test_business_category_exists(self):
        self.assertTrue(
            self.manager.exists("GLOBAL-BUSINESS-ECOSYSTEM")
        )

    def test_personal_registration_exists(self):
        self.assertTrue(
            self.manager.exists(
                "PERSONAL-RAJESHKHANDELWALOFFICIAL"
            )
        )

    def test_company_registration_exists(self):
        self.assertTrue(
            self.manager.exists(
                "COMPANY-KHANDELWALGROUPANDCOMPANY"
            )
        )

    def test_tree_has_root(self):
        result = self.manager.tree()

        self.assertTrue(result["success"])
        self.assertIsNotNone(result["tree"])
        self.assertEqual(
            result["tree"]["ecosystem_id"],
            "GLOBAL-ECOSYSTEM",
        )

    def test_connection_map(self):
        result = self.manager.connection_map()

        self.assertTrue(result["success"])
        self.assertEqual(
            result["node_count"],
            self.manager.registry.count(),
        )
        self.assertEqual(
            result["edge_count"],
            result["node_count"] - 1,
        )

    def test_names(self):
        result = self.manager.names()

        self.assertTrue(result["success"])
        self.assertEqual(
            result["count"],
            len(result["names"]),
        )
        self.assertIn("GLOBAL ECOSYSTEM", result["names"])


if __name__ == "__main__":
    unittest.main()
