"""Offline tests for SERVER orchestration boundaries."""
import unittest

from backend.server.global_ecosystem.global_server_ecosystem import GlobalServerEcosystemService
from backend.server.global_ecosystem.global_server_ecosystem.models import ServerOrchestrationRequest


class FakeCore:
    def validate_request(self, request):
        return {**request, "validated": True}


class FakeEngine:
    def dispatch(self, operation, payload):
        return {"operation": operation, "payload": payload}


class ServerFoundationTests(unittest.TestCase):
    def test_server_starts_without_external_connections(self):
        status = GlobalServerEcosystemService().health()
        self.assertEqual(status["domain"], "SERVER")
        self.assertFalse(status["status"]["ready"])
        self.assertEqual(status["provider_connections"], "NOT_ATTEMPTED")
        self.assertEqual(
            [item["name"] for item in status["layers"]],
            ["API", "CORE", "ENGINE", "DATABASE", "STORAGE"],
        )

    def test_server_dispatches_through_injected_core_and_engine(self):
        service = GlobalServerEcosystemService()
        service.register_layer("CORE", FakeCore())
        service.register_layer("ENGINE", FakeEngine())
        result = service.dispatch(ServerOrchestrationRequest("inspect", {"id": "node-1"}))
        self.assertTrue(result.success)
        self.assertEqual(result.status, "COMPLETED")
        self.assertTrue(result.result["payload"]["validated"])

    def test_server_requires_core_and_engine_before_dispatch(self):
        result = GlobalServerEcosystemService().dispatch(
            ServerOrchestrationRequest("inspect")
        )
        self.assertFalse(result.success)
        self.assertEqual(result.status, "NOT_READY")
        self.assertEqual(set(result.layers["missing"]), {"CORE", "ENGINE"})

    def test_registry_rejects_unknown_layer_and_duplicate_registration(self):
        service = GlobalServerEcosystemService()
        with self.assertRaises(ValueError):
            service.register_layer("UNKNOWN", object())
        service.register_layer("CORE", FakeCore())
        with self.assertRaises(ValueError):
            service.register_layer("CORE", FakeCore())
        service.register_layer("CORE", FakeCore(), replace=True)

    def test_empty_operation_is_rejected(self):
        result = GlobalServerEcosystemService().dispatch(
            ServerOrchestrationRequest("   ")
        )
        self.assertFalse(result.success)
        self.assertEqual(result.status, "REJECTED")


if __name__ == "__main__":
    unittest.main()
