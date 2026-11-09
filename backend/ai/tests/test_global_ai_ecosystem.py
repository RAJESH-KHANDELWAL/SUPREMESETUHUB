"""Focused tests for the AI ecosystem's catalog and execution boundaries."""
import unittest

from backend.ai.global_ecosystem.global_ai_ecosystem import (
    GlobalAIEcosystemService,
    get_catalog,
)
from backend.ai.global_ecosystem.global_ai_ecosystem.registry import AIAdapterRegistry
from backend.ai.global_ecosystem.global_ai_ecosystem.schemas import AIExecutionRequest


class GlobalAIEcosystemTests(unittest.TestCase):
    def test_catalog_has_expected_domains(self):
        catalog = get_catalog()
        for domain in (
            "providers", "models", "capabilities", "services",
            "agent_components", "workflows", "knowledge",
            "infrastructure", "governance", "integrations",
        ):
            self.assertIn(domain, catalog)
            self.assertTrue(catalog[domain])

    def test_runtime_is_disabled_without_executor(self):
        service = GlobalAIEcosystemService()
        self.assertFalse(service.status()["runtime_enabled"])
        with self.assertRaisesRegex(RuntimeError, "AI_RUNTIME_NOT_CONFIGURED"):
            service.execute(AIExecutionRequest(task="hello", provider_id="openai"))

    def test_explicit_adapter_registration_and_dispatch(self):
        registry = AIAdapterRegistry()
        registry.register(
            "test-provider",
            capabilities=["text"],
            handler=lambda capability, **payload: {"capability": capability, **payload},
        )
        result = registry.execute("test-provider", "text", prompt="hello")
        self.assertEqual(result["capability"], "text")
        self.assertEqual(result["prompt"], "hello")

    def test_request_validation(self):
        with self.assertRaisesRegex(ValueError, "AI_TASK_REQUIRED"):
            AIExecutionRequest(task=" ", provider_id="openai").validate()


if __name__ == "__main__":
    unittest.main()
