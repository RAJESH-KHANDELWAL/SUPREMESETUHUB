
"""Backend tests for the GLOBAL ECOSYSTEM API."""

import unittest

from backend.api.global_ecosystem import GlobalEcosystemAPI


class TestBackendGlobalEcosystemAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.api = GlobalEcosystemAPI()

    def test_api_health(self):
        result = self.api.health()

        self.assertIsInstance(result, dict)
        self.assertTrue(result["success"])

    def test_root_ecosystem(self):
        result = self.api.get("GLOBAL-ECOSYSTEM")

        self.assertTrue(result["success"])
        self.assertEqual(
            result["ecosystem"]["ecosystem_id"],
            "GLOBAL-ECOSYSTEM",
        )

    def test_people_ecosystem_exists(self):
        self.assertTrue(
            self.api.exists("GLOBAL-PEOPLE-ECOSYSTEM")
        )

    def test_business_ecosystem_exists(self):
        self.assertTrue(
            self.api.exists("GLOBAL-BUSINESS-ECOSYSTEM")
        )

    def test_list_ecosystems(self):
        result = self.api.list()

        self.assertTrue(result["success"])
        self.assertGreater(result["count"], 0)
        self.assertIsInstance(result["ecosystems"], list)

    def test_names_include_root(self):
        result = self.api.names()

        self.assertTrue(result["success"])
        self.assertIn("GLOBAL ECOSYSTEM", result["names"])

    def test_missing_ecosystem(self):
        result = self.api.get("NONEXISTENT-ECOSYSTEM")

        self.assertFalse(result["success"])
        self.assertEqual(
            result["error"],
            "ECOSYSTEM_NOT_FOUND",
        )

    def test_tree(self):
        result = self.api.tree()

        self.assertTrue(result["success"])
        self.assertEqual(
            result["tree"]["ecosystem_id"],
            "GLOBAL-ECOSYSTEM",
        )

    def test_connection_map(self):
        result = self.api.connection_map()

        self.assertTrue(result["success"])
        self.assertGreater(result["node_count"], 0)


if __name__ == "__main__":
    unittest.main()
