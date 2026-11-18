"""Provider-facade tests covering all capability dispatch boundaries."""
import unittest

from ...contracts import CapabilityRequest, TenantContext
from ...service import CohereCoreService


class CohereProviderRoutingTests(unittest.TestCase):
    def setUp(self):
        self.service = CohereCoreService()

    def test_all_capabilities_dispatch_to_validators(self):
        cases = {
            "classify": {"inputs": ["hello"]},
            "command": {"message": "hello"},
            "embed": {"texts": ["hello"]},
            "rerank": {"query": "hello", "documents": ["hello world"]},
            "tokenize": {"text": "hello"},
        }
        for capability, inputs in cases.items():
            with self.subTest(capability=capability):
                result = self.service.validate(CapabilityRequest(capability, inputs))
                self.assertTrue(result.ok, result.errors)
                self.assertEqual(result.status, "validated")

    def test_capability_specific_invalid_input_is_rejected(self):
        cases = {
            "classify": {"inputs": [""]},
            "command": {"message": ""},
            "embed": {"texts": []},
            "rerank": {"query": "hello", "documents": [], "top_n": 0},
            "tokenize": {"text": ""},
        }
        for capability, inputs in cases.items():
            with self.subTest(capability=capability):
                result = self.service.validate(CapabilityRequest(capability, inputs))
                self.assertFalse(result.ok)
                self.assertEqual(result.status, "rejected")
                self.assertTrue(result.errors)

    def test_unknown_capability_is_rejected(self):
        result = self.service.validate(CapabilityRequest("unknown", {}))
        self.assertFalse(result.ok)
        self.assertEqual(result.status, "rejected")

    def test_non_mapping_inputs_are_rejected(self):
        result = self.service.validate(CapabilityRequest("command", []))
        self.assertFalse(result.ok)
        self.assertIn("inputs must be a mapping", result.errors)

    def test_wrong_field_types_are_rejected_without_crashing(self):
        cases = {
            "command": {"message": 42},
            "rerank": {"query": 42, "documents": ["doc"]},
            "tokenize": {"text": None},
            "embed": {"texts": "not-a-list"},
        }
        for capability, inputs in cases.items():
            with self.subTest(capability=capability):
                result = self.service.validate(CapabilityRequest(capability, inputs))
                self.assertFalse(result.ok)
                self.assertEqual(result.status, "rejected")

    def test_nested_secret_fields_are_rejected(self):
        result = self.service.validate(
            CapabilityRequest("command", {"message": "hello", "chat_history": [{"authorization": "secret"}]})
        )
        self.assertFalse(result.ok)
        self.assertIn("Secret material", result.errors[0])

    def test_unknown_fields_and_unsupported_options_are_rejected(self):
        unknown = self.service.validate(CapabilityRequest("tokenize", {"text": "hello", "execute": True}))
        options = self.service.validate(CapabilityRequest("tokenize", {"text": "hello"}, options={"temperature": 0.2}))
        self.assertFalse(unknown.ok)
        self.assertFalse(options.ok)

    def test_authorization_requires_tenant_context_and_never_calls_api(self):
        denied = self.service.authorize_capability("embed", None)
        allowed = self.service.authorize_capability(
            "embed", TenantContext(tenant_id="tenant-1", actor_id="actor-1")
        )
        self.assertFalse(denied["success"])
        self.assertTrue(allowed["success"])
        self.assertFalse(allowed["api_call_performed"])

    def test_status_never_claims_live_connectivity(self):
        status = self.service.status()
        self.assertFalse(status["live_provider_calls_enabled"])
        self.assertFalse(status["live_connection_verified"])
        self.assertEqual(status["api_calls_performed"], 0)


if __name__ == "__main__":
    unittest.main()
