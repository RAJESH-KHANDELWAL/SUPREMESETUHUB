"""Offline tests for canonical GLOBAL SERVER ECOSYSTEM."""
import unittest
from .registry import ServerRegistrationRegistry, get_provider, get_service_type, list_providers, list_service_types
from .service import EcosystemService


class ServerRegistryTests(unittest.TestCase):
    def test_catalog_ids_are_unique_and_expected_providers_exist(self):
        providers, services = list_providers(), list_service_types()
        self.assertEqual(len({x["provider_id"] for x in providers}), len(providers))
        self.assertEqual(len({x["service_type_id"] for x in services}), len(services))
        expected = {"aws", "azure", "cloudflare", "digitalocean", "google", "hostinger"}
        self.assertTrue(expected.issubset({x["provider_id"] for x in providers}))

    def test_lookup_normalization_and_copy_isolation(self):
        item = get_provider("AWS")
        item["capabilities"].append("tamper")
        self.assertNotIn("tamper", get_provider("aws")["capabilities"])
        self.assertEqual(get_service_type("vps_server")["service_type_id"], "VPS-SERVER")
        with self.assertRaises(KeyError):
            get_provider("not-a-provider")

    def test_inventory_lifecycle(self):
        service = EcosystemService()
        payload = {
            "server_id": "node-1", "server_name": "Test Node", "provider_id": "aws",
            "server_type": "vps", "server_role": "app", "country": "IN",
            "region": "ap-south-1", "environment": "test",
        }
        created = service.register_server(**payload)
        self.assertTrue(created["success"])
        created["server"]["server_name"] = "tampered"
        self.assertEqual(service.get_server("node-1")["server"]["server_name"], "Test Node")
        self.assertTrue(service.authorize_server("node-1")["server"]["authorized"])
        self.assertFalse(service.disable_server("node-1")["server"]["enabled"])
        self.assertEqual(service.list_servers()["count"], 1)

    def test_validation_duplicate_and_update_allowlist(self):
        registry = ServerRegistrationRegistry()
        with self.assertRaises(ValueError):
            registry.register({"server_id": "incomplete"})
        payload = {
            "server_id": "one", "server_name": "One", "provider_id": "aws",
            "server_type": "vps", "server_role": "app", "country": "IN",
            "region": "west", "environment": "test",
        }
        registry.register(payload)
        with self.assertRaises(ValueError):
            registry.register(payload)
        with self.assertRaises(ValueError):
            registry.update("one", password="not-allowed")


if __name__ == "__main__":
    unittest.main()
