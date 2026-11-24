"""Unit tests for DeepSeek catalog, validation, and request planning."""
from __future__ import annotations
import os
import unittest
from unittest.mock import patch
from backend.global_ecosystem.deepseek_ecosystem import DeepSeekEcosystemService, get_health, validate_request
from backend.global_ecosystem.deepseek_ecosystem.registry import get_product, list_capabilities, list_products

class DeepSeekEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = DeepSeekEcosystemService()

    def test_catalog_models_and_layer_boundaries(self):
        catalog = self.service.catalog()
        self.assertEqual(catalog["models"], ["deepseek-chat", "deepseek-reasoner"])
        self.assertIn("api", catalog["architecture_refs"])
        self.assertIn("engine", catalog["architecture_refs"])
        self.assertFalse(catalog["live_connection_verified"])

    def test_chat_plan_is_metadata_only_and_hides_content(self):
        plan = self.service.plan_request("chat_completions", {"messages": [{"role": "user", "content": "hello"}]})
        self.assertEqual(plan["status"], "PLAN_ONLY")
        self.assertFalse(plan["live_execution"])
        self.assertNotIn("hello", str(plan))

    def test_reasoner_model_selection(self):
        plan = self.service.plan_request("responses", {"input": "solve"}, model="deepseek-reasoner")
        self.assertEqual(plan["model"], "deepseek-reasoner")

    def test_unknown_model_rejected(self):
        with self.assertRaises(ValueError):
            self.service.plan_request("chat_completions", {"prompt": "hi"}, "unknown")

    def test_unknown_operation_rejected(self):
        with self.assertRaises(ValueError):
            validate_request("admin", {})

    def test_nested_secret_field_rejected(self):
        with self.assertRaises(ValueError):
            validate_request("chat_completions", {"messages": [{"role": "user", "content": "hi", "token": "bad"}]})

    def test_search_requires_non_empty_query(self):
        with self.assertRaises(ValueError):
            validate_request("search", {"query": " "})

    def test_fetch_requires_http_url(self):
        with self.assertRaises(ValueError):
            validate_request("fetch", {"url": "file:///etc/passwd"})

    def test_health_reports_key_presence_only(self):
        with patch.dict(os.environ, {"DEEPSEEK_API_KEY": "example"}, clear=False):
            health = get_health()
        self.assertTrue(health["configured"])
        self.assertFalse(health["connection_verified"])
        self.assertNotIn("example", str(health))

    def test_registry(self):
        self.assertEqual(len(list_products()), 2)
        self.assertIn("reasoning", list_capabilities())
        self.assertEqual(get_product("deepseek-chat")["id"], "deepseek-chat")

if __name__ == "__main__":
    unittest.main()
