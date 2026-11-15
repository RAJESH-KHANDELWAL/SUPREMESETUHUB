"""Unit tests for DATABASE hierarchy and provider registries."""
import unittest

from .ecosystem_registry import DatabaseEcosystemRegistry
from .manager import GlobalDatabaseEcosystemManager
from .registry import GlobalDatabaseEcosystemRegistry as ProviderRegistry


class TestDatabaseRegistries(unittest.TestCase):
    def test_hierarchy_registry_enforces_parent(self):
        registry = DatabaseEcosystemRegistry()
        with self.assertRaises(ValueError):
            registry.register({"ecosystem_id": "CHILD", "name": "Child", "parent_id": "MISSING"})

    def test_provider_registry_lists_expected_adapters(self):
        providers = ProviderRegistry.list_providers()
        ids = {item["provider_id"] for item in providers}
        self.assertEqual(ids, {"google", "aws", "microsoft", "proton", "mega"})
        self.assertTrue(all(item["connection_status"] == "not_configured" for item in providers))

    def test_provider_lookup(self):
        provider = ProviderRegistry.get_provider("google")
        self.assertEqual(provider.describe()["provider_id"], "google")

    def test_provider_lookup_rejects_unknown(self):
        with self.assertRaises(KeyError):
            ProviderRegistry.get_provider("unknown")

    def test_manager_exposes_provider_discovery(self):
        manager = GlobalDatabaseEcosystemManager()
        self.assertEqual(len(manager.list_providers()), 5)


if __name__ == "__main__":
    unittest.main()
