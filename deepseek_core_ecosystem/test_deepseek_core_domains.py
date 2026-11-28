"""Structural and behavior tests for the DeepSeek Core control plane."""
import unittest

from .catalog import get_catalog, list_capabilities
from .contracts import DeepSeekCoreResult
from .manager import get_manager
from .service import DeepSeekCoreService


class DeepSeekCoreTests(unittest.TestCase):
    def test_catalog_registers_four_capabilities(self):
        catalog = get_catalog()
        self.assertEqual(catalog["provider"], "deepseek")
        self.assertEqual(set(list_capabilities()), {
            "chat_completions", "responses", "search", "fetch"
        })

    def test_manager_reports_metadata_only(self):
        status = get_manager().status()
        self.assertEqual(status["ecosystem_id"], "DEEPSEEK-CORE-ECOSYSTEM")
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)

    def test_capability_contracts_validate_without_live_calls(self):
        service = DeepSeekCoreService()
        cases = [
            ("chat_completions", {"messages": [{"role": "user", "content": "hi"}]}),
            ("responses", {"input": "hi"}),
            ("search", {"query": "hi"}),
            ("fetch", {"urls": ["https://example.com"]}),
        ]
        for capability, payload in cases:
            with self.subTest(capability=capability):
                result = service.validate(capability, payload)
                self.assertEqual(result["capability"], capability)
                self.assertFalse(result["live_call"])

    def test_unknown_capability_is_rejected(self):
        with self.assertRaises(ValueError):
            get_manager().validate("unknown", {})

    def test_secret_fields_are_rejected(self):
        with self.assertRaises(ValueError):
            get_manager().validate(
                "responses", {"input": "hi", "nested": {"api_key": "do-not-accept"}}
            )

    def test_execute_is_disabled(self):
        with self.assertRaisesRegex(RuntimeError, "LIVE_PROVIDER_CALLS_DISABLED"):
            DeepSeekCoreService().execute()

    def test_result_contract_serializes(self):
        result = DeepSeekCoreResult(success=True, data={"capability_count": 4})
        self.assertEqual(result.to_dict()["ecosystem_id"], "DEEPSEEK-CORE-ECOSYSTEM")


if __name__ == "__main__":
    unittest.main()
