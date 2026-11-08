"""Registry tests for the independent SERVER runtime registry."""
import unittest
from .models import ServerNode
from .registry import ServerRegistry
from .provider_registry import ServerProviderRegistry

class FakeProvider:
    provider_id = "aws"
    def describe(self):
        return {"provider_id": self.provider_id, "connection_status": "not_configured"}

class RegistryTests(unittest.TestCase):
    def test_server_registry_registers_and_retrieves_nodes(self):
        registry = ServerRegistry()
        node = ServerNode("node-1", "Node One")
        registry.register(node)
        self.assertIs(registry.get("node-1"), node)
        self.assertEqual(registry.count(), 1)

    def test_server_registry_rejects_duplicate_ids(self):
        registry = ServerRegistry()
        registry.register(ServerNode("node-1", "Node One"))
        with self.assertRaises(ValueError):
            registry.register(ServerNode("node-1", "Node Two"))

    def test_provider_registry_normalizes_provider_ids(self):
        registry = ServerProviderRegistry()
        provider = FakeProvider()
        registry.register("AWS", provider)
        self.assertIs(registry.get("aws"), provider)

    def test_provider_registry_rejects_provider_id_mismatch(self):
        registry = ServerProviderRegistry()
        with self.assertRaises(ValueError):
            registry.register("google", FakeProvider())

if __name__ == "__main__":
    unittest.main()
