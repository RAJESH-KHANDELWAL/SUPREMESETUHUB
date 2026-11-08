"""Registry tests for the lowercase independent SERVER ecosystem."""
import unittest
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry

class FakeProvider:
    provider_id = "aws"
    def describe(self):
        return {"provider_id": self.provider_id, "connection_status": "not_configured"}

class RegistryTests(unittest.TestCase):
    def test_layer_registry_accepts_known_layers(self):
        registry = ServerLayerRegistry()
        adapter = object()
        self.assertIs(registry.register("CORE", adapter), adapter)
        self.assertIs(registry.get("core"), adapter)

    def test_layer_registry_rejects_unknown_layer(self):
        with self.assertRaises(ValueError):
            ServerLayerRegistry().register("UNKNOWN", object())

    def test_provider_registry_normalizes_provider_ids(self):
        registry = ServerProviderRegistry()
        provider = FakeProvider()
        registry.register("AWS", provider)
        self.assertIs(registry.get("aws"), provider)
        self.assertEqual(registry.catalog()[1]["status"], "REGISTERED")

    def test_provider_registry_rejects_provider_id_mismatch(self):
        registry = ServerProviderRegistry()
        provider = FakeProvider()
        with self.assertRaises(ValueError):
            registry.register("google", provider)

if __name__ == "__main__":
    unittest.main()
