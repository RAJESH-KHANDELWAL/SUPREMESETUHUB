"""Provider-facade routing tests for the five Cohere capability contracts."""
import unittest

from ..contracts import CapabilityRequest
from ..service import CohereCoreService


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


if __name__ == "__main__":
    unittest.main()
