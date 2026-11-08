"""Offline tests for SERVER ownership, registries and orchestration."""
import unittest
from backend.server.global_ecosystem.global_server_ecosystem import (
    GlobalServerEcosystemManager, GlobalServerEcosystemService,
    get_layer_catalog, get_provider_catalog,
)
from backend.server.global_ecosystem.global_server_ecosystem.models import ServerOrchestrationRequest
class FakeCore:
    def validate_request(self, request):
        return {**request, "validated": True}
class FakeEngine:
    def dispatch(self, operation, payload):
        return {"operation": operation, "payload": payload}
class ServerFoundationTests(unittest.TestCase):
    def test_catalog_contains_five_independent_layers(self):
        self.assertEqual([x.name for x in get_layer_catalog()],
                         ["API", "CORE", "ENGINE", "DATABASE", "STORAGE"])
        self.assertTrue(all(x.owner_path.startswith("backend/") for x in get_layer_catalog()))
    def test_provider_catalog_keeps_existing_five_provider_folders(self):
        self.assertEqual([x.provider_id for x in get_provider_catalog()],
                         ["aws", "azure", "digitalocean", "google", "hostinger"])
    def test_health_does_not_open_external_connections(self):
        result = GlobalServerEcosystemService().health()
        self.assertFalse(result["status"]["ready"])
        self.assertEqual(result["external_connections"], "NOT_ATTEMPTED")
        self.assertEqual(len(result["providers"]), 5)
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
    def test_layer_registry_rejects_unknown_and_duplicate_entries(self):
        manager = GlobalServerEcosystemManager()
        with self.assertRaises(ValueError):
            manager.register_layer("UNKNOWN", object())
        manager.register_layer("CORE", FakeCore())
        with self.assertRaises(ValueError):
            manager.register_layer("CORE", FakeCore())
        manager.register_layer("CORE", FakeCore(), replace=True)
    def test_provider_registry_rejects_duplicate_entries(self):
        manager = GlobalServerEcosystemManager()
        manager.register_provider("aws", object())
        with self.assertRaises(ValueError):
            manager.register_provider("AWS", object())
    def test_empty_operation_is_rejected(self):
        result = GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest(" "))
        self.assertFalse(result.success)
        self.assertEqual(result.status, "REJECTED")
if __name__ == "__main__":
    unittest.main()