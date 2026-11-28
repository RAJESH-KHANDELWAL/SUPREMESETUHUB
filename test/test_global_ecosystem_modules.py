
"""Tests for GLOBAL ECOSYSTEM MODULES and its API integration."""

import unittest

from backend.api.global_ecosystem import GlobalEcosystemAPI
from backend.api.global_ecosystem_modules import GlobalEcosystemModules


class TestGlobalEcosystemModules(unittest.TestCase):

    def setUp(self):
        self.modules = GlobalEcosystemModules()

    def test_status(self):
        result = self.modules.status()
        self.assertTrue(result["success"])
        self.assertEqual(result["name"], "GLOBAL ECOSYSTEM MODULES")
        self.assertGreater(result["module_count"], 0)

    def test_list_modules(self):
        result = self.modules.list_modules()
        self.assertTrue(result["success"])
        self.assertGreater(result["count"], 0)
        self.assertIsInstance(result["modules"], list)

    def test_known_module(self):
        result = self.modules.get_module("AUTH")
        self.assertTrue(result["success"])
        self.assertEqual(result["module"]["path"], "backend.api.auth")

    def test_module_lookup_is_case_insensitive(self):
        result = self.modules.get_module("auth")
        self.assertTrue(result["success"])
        self.assertEqual(result["module"]["module_id"], "AUTH")

    def test_unknown_module(self):
        result = self.modules.get_module("NOT_A_REAL_MODULE")
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "API_MODULE_NOT_FOUND")

    def test_module_data_is_isolated(self):
        result = self.modules.get_module("AUTH")
        result["module"]["name"] = "CHANGED"

        fresh_result = self.modules.get_module("AUTH")
        self.assertEqual(fresh_result["module"]["name"], "AUTH API")

    def test_api_facade_integration(self):
        api = GlobalEcosystemAPI()

        self.assertTrue(api.modules_status()["success"])
        self.assertTrue(api.list_modules()["success"])
        self.assertTrue(api.get_module("AUTH")["success"])
        self.assertIn("GLOBAL ECOSYSTEM MODULES", api.modules_status()["name"])


if __name__ == "__main__":
    unittest.main()
