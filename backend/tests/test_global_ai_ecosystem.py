"""Tests for GLOBAL AI CORE orchestration and provider boundaries."""
import unittest
from unittest.mock import patch

from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.service import GlobalAICoreService
from backend.engine.global_ecosystem.global_engine_ecosystem.global_ai_engine_ecosystem.manager import EcosystemEngineManager
from backend.engine.global_ecosystem.global_engine_ecosystem.global_ai_engine_ecosystem.openai_provider import OpenAITextEngine


class GlobalAIEcosystemTests(unittest.TestCase):
    def test_core_dispatches_through_injected_engine(self):
        calls = []
        def executor(**kwargs):
            calls.append(kwargs)
            return {"provider": "fake", "model": "test", "output": "analysis", "live_verified": True}
        result = GlobalAICoreService(executor).generate(task="analyze", context={"sector": "retail"})
        self.assertEqual(result["system"], "GLOBAL AI ECOSYSTEM")
        self.assertEqual(result["output"], "analysis")
        self.assertEqual(calls[0]["capability"], "text")
        self.assertIsNone(calls[0]["model_id"])

    def test_core_rejects_empty_task(self):
        service = GlobalAICoreService(lambda **kwargs: {})
        with self.assertRaises(ValueError):
            service.generate(task=" ")

    def test_engine_reports_openai_disabled_without_server_key(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            provider = OpenAITextEngine()
            self.assertFalse(provider.status()["enabled"])

    def test_engine_lists_global_ai_provider(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            manager = EcosystemEngineManager()
            self.assertEqual(manager.provider_status()[0]["provider_id"], "openai")
            self.assertFalse(manager.provider_status()[0]["enabled"])

    def test_engine_registers_all_supported_chat_adapters(self):
        with patch.dict("os.environ", {"OPENAI_API_KEY": ""}):
            manager = EcosystemEngineManager()
            statuses = manager.provider_status()
            provider_ids = {item["provider_id"] for item in statuses}
            self.assertEqual(manager.registry.count(), len(statuses))
            self.assertGreaterEqual(len(statuses), 21)
            self.assertIn("google_gemini", provider_ids)
            self.assertIn("anthropic_claude", provider_ids)
            self.assertIn("ollama", provider_ids)
            self.assertTrue(all(item["live_verified"] is False for item in statuses))


if __name__ == "__main__":
    unittest.main()
