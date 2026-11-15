"""Unit tests for the independent SERVER domain and its adapter boundaries."""
import unittest

from backend.server import (
    ServerController, ServerManager, ServerService, ServerValidationError,
    ServerNotFoundError,
)
from backend.server.global_ecosystem.global_server_ecosystem import (
    ServerProviderAdapter, ServerCapabilityNotConfigured,
)


class FakeProvider(ServerProviderAdapter):
    provider_id = "aws"
    display_name = "AWS test adapter"

    def __init__(self):
        super().__init__(lambda operation, payload: {
            "operation": operation, "payload": payload,
        })


class FakeOperationAdapter:
    def execute(self, operation, payload):
        return {"operation": operation, "payload": payload}


class ServerDomainTests(unittest.TestCase):
    def test_server_package_exposes_independent_services(self):
        self.assertEqual(ServerManager().describe()["domain"], "SERVER")

    def test_register_and_retrieve_server(self):
        service = ServerService()
        created = service.register(name="Test Web", server_type="WEB", provider="local")
        self.assertEqual(service.get(created["server_id"])["name"], "Test Web")
        self.assertEqual(len(service.list()), 1)

    def test_rejects_unknown_server_type(self):
        with self.assertRaises(ServerValidationError):
            ServerService().register(name="Bad", server_type="UNKNOWN")

    def test_rejects_non_dictionary_metadata(self):
        with self.assertRaises(ServerValidationError):
            ServerService().register(name="Bad", server_type="WEB", metadata="unsafe")

    def test_crud_updates_inventory_only(self):
        service = ServerService()
        created = service.register(name="Before", server_type="WEB")
        updated = service.update(created["server_id"], name="After", metadata={"zone": "in"})
        self.assertEqual(updated["name"], "After")
        self.assertEqual(updated["metadata"]["zone"], "in")
        deleted = service.delete(created["server_id"])
        self.assertTrue(deleted["deleted"])
        self.assertEqual(deleted["scope"], "LOCAL_INVENTORY_ONLY")
        with self.assertRaises(ServerNotFoundError):
            service.get(created["server_id"])

    def test_lifecycle_changes_control_plane_state_only(self):
        service = ServerService()
        created = service.register(name="Test VPS", server_type="VPS")
        self.assertEqual(service.start(created["server_id"])["status"], "START_REQUESTED")
        self.assertEqual(service.stop(created["server_id"])["status"], "STOP_REQUESTED")
        self.assertEqual(service.restart(created["server_id"])["status"], "RESTART_REQUESTED")

    def test_health_does_not_claim_live_provider_connections(self):
        health = ServerService().health()
        self.assertEqual(health["external_connections"], "NOT_ATTEMPTED")
        self.assertFalse(health["inventory"]["durable"])

    def test_provider_registry_is_exposed_through_server_service(self):
        service = ServerService()
        service.register_provider("aws", FakeProvider())
        result = service.execute_provider_operation("aws", "inspect", {"server_id": "s1"})
        self.assertEqual(result["operation"], "inspect")
        self.assertEqual(result["payload"]["server_id"], "s1")
        self.assertEqual(service.provider_health("aws")["status"], "NOT_PROBED")
        self.assertEqual(service.provider_health("aws")["external_connection"], "NOT_ATTEMPTED")

    def test_unconfigured_provider_fails_closed(self):
        with self.assertRaises(RuntimeError):
            ServerService().execute_provider_operation("aws", "inspect")

    def test_operation_adapters_are_exposed_through_server_service(self):
        service = ServerService()
        service.register_operation_adapter("DEPLOYMENT", FakeOperationAdapter())
        result = service.execute_operation("deployment", "release", {"version": "1"})
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["result"]["payload"]["version"], "1")

    def test_unconfigured_operation_fails_closed(self):
        with self.assertRaises(ServerCapabilityNotConfigured):
            ServerService().execute_operation("PROVISIONING", "create", {})

    def test_manager_and_controller_expose_crud_and_lifecycle(self):
        controller = ServerController(ServerManager())
        created = controller.register(name="Managed", server_type="CLOUD")
        self.assertEqual(controller.start(created["server_id"])["status"], "START_REQUESTED")
        self.assertEqual(controller.update(created["server_id"], region="ap-south-1")["region"],
                         "ap-south-1")
        self.assertTrue(controller.delete(created["server_id"])["deleted"])


if __name__ == "__main__":
    unittest.main()
