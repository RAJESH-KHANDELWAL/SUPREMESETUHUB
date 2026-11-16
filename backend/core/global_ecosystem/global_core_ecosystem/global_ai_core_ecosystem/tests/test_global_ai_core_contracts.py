import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.catalog import get_ai_provider
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.contracts import Readiness
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.module_service import AIProductCoreService
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.policy import GlobalAICorePolicy
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.request_contracts import validate_ai_request
from backend.core.global_ecosystem.global_core_ecosystem.global_ai_core_ecosystem.service import GlobalAICoreService


class GlobalAICoreContractTests(unittest.TestCase):
    def test_legacy_openai_alias_resolves_to_canonical_provider(self):
        provider = get_ai_provider("openai")
        self.assertIsNotNone(provider)
        self.assertEqual(provider["id"], "openai_chatgpt")

    def test_task_service_uses_canonical_default_provider(self):
        captured = {}
        def executor(**kwargs):
            captured.update(kwargs)
            return {"output": "ok"}
        result = GlobalAICoreService(executor).generate(task="hello")
        self.assertTrue(result["success"])
        self.assertEqual(captured["provider_id"], "openai_chatgpt")

    def test_unknown_provider_is_rejected_before_engine_execution(self):
        called = []
        def executor(**kwargs):
            called.append(kwargs)
            return {"output": "unexpected"}
        with self.assertRaises(LookupError):
            GlobalAICoreService(executor).generate(task="hello", provider_id="not-a-provider")
        self.assertEqual(called, [])

    def test_request_contract_rejects_nested_secret_material(self):
        with self.assertRaisesRegex(ValueError, "SECRET_MATERIAL_FORBIDDEN_IN_CORE"):
            validate_ai_request({"provider_id":"openai_chatgpt","capability":"text","task":"hello","context":{"nested":{"api-key":"must-not-enter-core"}}})

    def test_request_contract_requires_provider_and_task(self):
        with self.assertRaisesRegex(ValueError, "AI_REQUEST_REQUIRED_FIELDS_MISSING"):
            validate_ai_request({"provider_id":"openai_chatgpt"})

    def test_provider_summary_recursively_filters_secrets_without_mutation(self):
        source={"id":"sample","metadata":{"api_key":"secret","region":"global"}}
        safe=GlobalAICorePolicy.safe_provider_summary(source)
        self.assertEqual(safe,{"id":"sample","metadata":{"region":"global"}})
        self.assertEqual(source["metadata"]["api_key"],"secret")

    def test_live_registry_label_is_not_reported_as_verified_ready(self):
        class SampleCore(AIProductCoreService):
            PROVIDER_ID="openai_chatgpt"
        service=SampleCore()
        service._provider["integration_status"]="live"
        status=service.status()
        self.assertEqual(status["readiness"],Readiness.LIVE_VERIFICATION_REQUIRED.value)
        self.assertFalse(status["live_connection_verified"])


if __name__ == "__main__":
    unittest.main()
