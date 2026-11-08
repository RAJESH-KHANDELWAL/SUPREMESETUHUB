"""Offline tests for SERVER ownership, provider alignment and orchestration."""
import unittest
from backend.server.global_ecosystem.global_server_ecosystem import (
    GlobalServerEcosystemManager, GlobalServerEcosystemService,
    ServerProviderAdapter, get_layer_catalog, get_provider_catalog,
)
from backend.server.global_ecosystem.global_server_ecosystem.models import ServerOrchestrationRequest

class FakeCore:
    def validate_request(self, request):
        return {**request, "validated": True}

class FakeEngine:
    def dispatch(self, operation, payload):
        return {"operation": operation, "payload": payload}

class FakeDatabase:
    def read_server_record(self, server_id):
        return {"server_id": server_id}

class FakeStorage:
    def resolve_artifact(self, artifact_id):
        return {"artifact_id": artifact_id}

class FakeProvider(ServerProviderAdapter):
    provider_id = "aws"
    display_name = "AWS test adapter"

class ServerFoundationTests(unittest.TestCase):
    def test_catalog_contains_five_independent_layers(self):
        self.assertEqual([x.name for x in get_layer_catalog()],
                         ["API", "CORE", "ENGINE", "DATABASE", "STORAGE"])
        self.assertTrue(all(x.owner_path.startswith("backend/") for x in get_layer_catalog()))

    def test_provider_catalog_aligns_with_peer_layers_and_keeps_additional_providers(self):
        providers = {x.provider_id: x for x in get_provider_catalog()}
        self.assertTrue({"abelohost", "aws", "cloudflare", "digitalocean",
                         "google", "microsoft", "vicetemple"}.issubset(providers))
        self.assertTrue({"azure", "hostinger"}.issubset(providers))
        self.assertEqual(providers["azure"].alignment, "ADDITIONAL")

    def test_health_does_not_open_external_connections(self):
        result = GlobalServerEcosystemService().health()
        self.assertFalse(result["status"]["ready"])
        self.assertEqual(result["external_connections"], "NOT_ATTEMPTED")
        self.assertEqual(len(result["providers"]), 9)

    def test_manager_dispatches_using_injected_core_and_engine(self):
        manager = GlobalServerEcosystemManager()
        manager.register_layer("CORE", FakeCore())
        manager.register_layer("ENGINE", FakeEngine())
        result = manager.dispatch(ServerOrchestrationRequest("inspect", {"id": "srv-1"}))
        self.assertTrue(result.success)
        self.assertEqual(result.status, "COMPLETED")
        self.assertTrue(result.result["payload"]["validated"])

    def test_dispatch_requires_core_and_engine(self):
        result = GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest("inspect"))
        self.assertFalse(result.success)
        self.assertEqual(result.status, "NOT_READY")
        self.assertEqual(set(result.layers["missing"]), {"CORE", "ENGINE"})

    def test_database_and_storage_are_called_only_through_registered_adapters(self):
        manager = GlobalServerEcosystemManager()
        with self.assertRaises(RuntimeError):
            manager.read_server_record("srv-1")
        with self.assertRaises(RuntimeError):
            manager.resolve_artifact("artifact-1")
        manager.register_layer("DATABASE", FakeDatabase())
        manager.register_layer("STORAGE", FakeStorage())
        self.assertEqual(manager.read_server_record("srv-1")["server_id"], "srv-1")
        self.assertEqual(manager.resolve_artifact("artifact-1")["artifact_id"], "artifact-1")

    def test_layer_registry_rejects_unknown_and_duplicate_entries(self):
        manager = GlobalServerEcosystemManager()
        with self.assertRaises(ValueError):
            manager.register_layer("UNKNOWN", object())
        manager.register_layer("CORE", FakeCore())
        with self.assertRaises(ValueError):
            manager.register_layer("CORE", FakeCore())
        manager.register_layer("CORE", FakeCore(), replace=True)

    def test_provider_registry_rejects_unknown_duplicate_and_mismatched_adapters(self):
        manager = GlobalServerEcosystemManager()
        manager.register_provider("aws", FakeProvider())
        with self.assertRaises(ValueError):
            manager.register_provider("AWS", FakeProvider())
        with self.assertRaises(KeyError):
            manager.register_provider("not-a-provider", FakeProvider())
        class WrongProvider(FakeProvider):
            provider_id = "google"
        with self.assertRaises(ValueError):
            manager.register_provider("aws", WrongProvider())

    def test_empty_operation_is_rejected(self):
        result = GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest(" "))
        self.assertFalse(result.success)
        self.assertEqual(result.status, "REJECTED")

if __name__ == "__main__":
    unittest.main()
