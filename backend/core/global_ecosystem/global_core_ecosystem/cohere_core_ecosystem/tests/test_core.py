import unittest
from cohere_core_ecosystem.contracts import CapabilityRequest
from cohere_core_ecosystem.manager import CohereCoreManager

class CohereCoreTests(unittest.TestCase):
    def setUp(self):
        self.manager = CohereCoreManager()

    def test_all_capabilities_registered(self):
        self.assertEqual(set(self.manager.list_capabilities()), {"classify", "command", "embed", "rerank", "tokenize"})

    def test_known_capability_validates(self):
        result = self.manager.validate(CapabilityRequest("embed", {"texts": ["hello"]}))
        self.assertTrue(result.ok)

    def test_unknown_capability_rejected(self):
        result = self.manager.validate(CapabilityRequest("unknown", {}))
        self.assertFalse(result.ok)

if __name__ == "__main__":
    unittest.main()
