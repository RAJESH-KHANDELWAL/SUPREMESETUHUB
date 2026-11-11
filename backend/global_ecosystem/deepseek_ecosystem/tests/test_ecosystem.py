"""Unit tests for DeepSeek provider metadata and request planning."""
import unittest
from backend.global_ecosystem.deepseek_ecosystem import (
    DeepSeekEcosystemService, get_catalog, get_health, validate_request,
)

class DeepSeekEcosystemTests(unittest.TestCase):
    def test_catalog_is_provider_scoped(self):
        catalog = get_catalog()
        self.assertEqual(catalog["provider_id"], "deepseek")
        self.assertIn("deepseek-reasoner", catalog["models"])
        self.assertFalse(catalog["live_connection_verified"])

    def test_catalog_returns_detached_products(self):
        first = get_catalog()
        first["products"].clear()
        self.assertTrue(get_catalog()["products"])

    def test_valid_chat_request(self):
        result = validate_request("chat_completions", {"messages": [{"role": "user", "content": "hello"}]})
        self.assertTrue(result["valid"])

    def test_rejects_missing_chat_input(self):
        with self.assertRaises(ValueError):
            validate_request("chat_completions", {})

    def test_rejects_credentials_in_payload(self):
        with self.assertRaises(ValueError):
            validate_request("chat_completions", {"prompt": "hello", "api_key": "do-not-accept"})

    def test_rejects_unknown_operation(self):
        with self.assertRaises(ValueError):
            validate_request("delete_everything", {})

    def test_request_plan_does_not_execute_live_call(self):
        plan = DeepSeekEcosystemService().plan_request("chat_completions", {"prompt": "hello"})
        self.assertFalse(plan["live_execution"])
        self.assertEqual(plan["status"], "PLAN_ONLY")

    def test_requires_catalog_model(self):
        with self.assertRaises(ValueError):
            DeepSeekEcosystemService().plan_request("chat_completions", {"prompt": "hello"}, "unknown-model")

    def test_health_does_not_claim_connectivity(self):
        health = get_health()
        self.assertFalse(health["connection_verified"])

if __name__ == "__main__":
    unittest.main()
