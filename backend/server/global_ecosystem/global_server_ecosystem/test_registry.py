"""Registry tests for the lowercase independent SERVER ecosystem."""
import unittest
from .registry import ServerLayerRegistry
from .provider_registry import ServerProviderRegistry
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
        provider = object()
        registry.register("AWS", provider)
        self.assertIs(registry.get("aws"), provider)
if __name__ == "__main__":
    unittest.main()