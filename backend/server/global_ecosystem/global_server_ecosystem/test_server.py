"""Offline tests for the independent SERVER runtime and provider setup."""
import unittest
from backend.server.global_ecosystem.global_server_ecosystem import (
    GlobalServerEcosystemManager, GlobalServerEcosystemService, ServerNode,
    ServerProviderAdapter, get_provider_catalog,
)

class FakeProvider(ServerProviderAdapter):
    provider_id = "aws"
    display_name = "AWS test adapter"

class ServerFoundationTests(unittest.TestCase):
    def test_server_setup_does_not_register_or_require_peer_layers(self):
        service = GlobalServerEcosystemService()
        health = service.health()
        self.assertEqual(health["domain"], "SERVER")
        self.assertNotIn("layers", health)
        self.assertNotIn("API", health)

    def test_server_node_registry_lifecycle(self):
        manager = GlobalServerEcosystemManager()
        node = ServerNode("srv-1", "Primary Server", host="127.0.0.1", port=8080)
        manager.register_server(node)
        self.assertIs(manager.get_server("srv-1"), node)
        self.assertEqual(len(manager.list_servers()), 1)
        self.assertTrue(manager.unregister_server("srv-1"))
        self.assertIsNone(manager.get_server("srv-1"))

    def test_duplicate_server_requires_explicit_replace(self):
        manager = GlobalServerEcosystemManager()
        manager.register_server(ServerNode("srv-1", "Primary"))
        with self.assertRaises(ValueError):
            manager.register_server(ServerNode("srv-1", "Replacement"))
        manager.register_server(ServerNode("srv-1", "Replacement"), replace=True)
        self.assertEqual(manager.get_server("srv-1").name, "Replacement")

    def test_provider_catalog_contains_server_integrations(self):
        ids = {item.provider_id for item in get_provider_catalog()}
        self.assertTrue({"abelohost", "aws", "cloudflare", "digitalocean",
                         "google", "microsoft", "vicetemple"}.issubset(ids))
        self.assertTrue({"azure", "hostinger"}.issubset(ids))

    def test_health_is_local_and_does_not_claim_live_connections(self):
        result = GlobalServerEcosystemService().health()
        self.assertEqual(result["external_connections"], "NOT_ATTEMPTED")
        self.assertEqual(result["configured_provider_count"], 0)

    def test_provider_registration_is_owned_by_server(self):
        manager = GlobalServerEcosystemManager()
        manager.register_provider("aws", FakeProvider())
        self.assertEqual(manager.status()["configured_providers"], 1)

if __name__ == "__main__":
    unittest.main()
