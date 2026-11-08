"""Offline tests for the canonical SERVER ecosystem."""
import unittest

from .registry import (
    ServerRegistrationRegistry,
    get_provider,
    get_service_type,
    list_providers,
    list_service_types,
)
from .service import EcosystemService


class ServerRegistryTests(unittest.TestCase):
    def test_catalogs_have_unique_ids_and_required_providers(self):
        providers = list_providers()
        services = list_service_types()
        self.assertEqual(len({x["provider_id"] for x in providers}), len(providers))
        self.assertEqual(len({x["service_type_id"] for x in services}), len(services))
        required = {"aws", "azure", "cloudflare", "digitalocean", "google", "hostinger"}
        self.assertTrue(required.issubset({x["provider_id"] for x in providers}))

    def test_lookups_are_normalized_and_return_copies(self):
        item = get_provider("AWS")
        item["capabilities"].append("tamper")
        self.assertNotIn("tamper", get_provider("aws")["capabilities"])
        self.assertEqual(get_service_type("vps_server")["service_type_id"], "VPS-SERVER")
        with self.assertRaises(KeyError):
            get_provider("not-a-provider")

    def test_inventory_lifecycle(self):
        service = EcosystemService()
        data = {
            "server_id": "node-1", "server_name": "Test Node",
            "provider_id": "aws", "server_type": "vps", "server_role": "app",
            "country": "IN", "region": "ap-south-1", "environment": "test",
        }
        created = service.register_server(**data)
        self.assertTrue(created["success"])
        created["server"]["server_name"] = "mutated"
        self.assertEqual(service.get_server("node-1")["server"]["server_name"], "Test Node")
        self.assertTrue(service.authorize_server("node-1")["server"]["authorized"])
        self.assertFalse(service.disable_server("node-1")["server"]["enabled"])
        self.assertEqual(service.list_servers()["count"], 1)

    def test_registry_rejects_invalid_duplicate_and_unsafe_updates(self):
        registry = ServerRegistrationRegistry()
        with self.assertRaises(ValueError):
            registry.register({"server_id": "incomplete"})
        valid = {
            "server_id": "one", "server_name": "One", "provider_id": "aws",
            "server_type": "vps", "server_role": "app", "country": "IN",
            "region": "west", "environment": "test",
        }
        registry.register(valid)
        with self.assertRaises(ValueError):
            registry.register(valid)
        with self.assertRaises(ValueError):
            registry.update("one", password="not-allowed")


if __name__ == "__main__":
    unittest.main()
