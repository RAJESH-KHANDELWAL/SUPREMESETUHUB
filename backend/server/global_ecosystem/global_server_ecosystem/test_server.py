"""Offline tests for SERVER layer structure and orchestration boundaries."""
import unittest

from backend.server.global_ecosystem.global_server_ecosystem import (
    GlobalServerEcosystemManager,
    GlobalServerEcosystemService,
    get_layer_catalog,
)
from backend.server.global_ecosystem.global_server_ecosystem.models import ServerOrchestrationRequest

class FakeCore:
    def validate_request(self, request):
        return {**request, "validated": True}

class FakeEngine:
    def dispatch(self, operation, payload):
        return {"operation": operation, "payload": payload}

class ServerFoundationTests(unittest.TestCase):
    def test_layer_catalog_defines_all_five_independent_owners(self):
        catalog = get_layer_catalog()
        self.assertEqual([item.name for item in catalog], ["API", "CORE", "ENGINE", "DATABASE", "STORAGE"])
        self.assertTrue(all(item.owner_path.startswith("backend/") for item in catalog))

    def test_server_starts_without_external_connections(self):
        status = GlobalServerEcosystemService().health()
        self.assertEqual(status["domain"], "SERVER")
        self.assertFalse(status["status"]["ready"])
        self.assertEqual(status["provider_connections"], "NOT_ATTEMPTED")
        self.assertEqual([item["name"] for item in status["layers"]], ["API", "CORE", "ENGINE", "DATABASE", "STORAGE"])

    def test_manager_owns_lifecycle_and_uses_injected_adapters(self):
        manager = GlobalServerEcosystemManager()
        manager.register_layer("CORE", FakeCore())
        manager.register_layer("ENGINE", FakeEngine())
        result = manager.dispatch(ServerOrchestrationRequest("inspect", {"id": "node-1"}))
        self.assertTrue(result.success)
        self.assertTrue(result.result["payload"]["validated"])

    def test_missing_core_and_engine_are_explicit(self):
        result = GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest("inspect"))
        self.assertFalse(result.success)
        self.assertEqual(result.status, "NOT_READY")
        self.assertEqual(set(result.layers["missing"]), {"CORE", "ENGINE"})

    def test_registry_rejects_unknown_and_duplicate_layer(self):
        manager = GlobalServerEcosystemManager()
        with self.assertRaises(ValueError):
            manager.register_layer("UNKNOWN", object())
        manager.register_layer("CORE", FakeCore())
        with self.assertRaises(ValueError):
            manager.register_layer("CORE", FakeCore())
        manager.register_layer("CORE", FakeCore(), replace=True)

    def test_empty_operation_is_rejected(self):
        result = GlobalServerEcosystemService().dispatch(ServerOrchestrationRequest("   "))
        self.assertFalse(result.success)
        self.assertEqual(result.status, "REJECTED")

if __name__ == "__main__":
    unittest.main()
