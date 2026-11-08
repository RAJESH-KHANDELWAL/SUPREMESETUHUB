"""Unit tests for the independent SERVER domain."""
import unittest
from backend.server import ServerManager, ServerService, ServerValidationError

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
    def test_lifecycle_changes_control_plane_state_only(self):
        service = ServerService()
        created = service.register(name="Test VPS", server_type="VPS")
        self.assertEqual(service.start(created["server_id"])["status"], "START_REQUESTED")
        self.assertEqual(service.stop(created["server_id"])["status"], "STOP_REQUESTED")
    def test_health_does_not_claim_live_provider_connections(self):
        health = ServerService().health()
        self.assertEqual(health["external_connections"], "NOT_ATTEMPTED")
        self.assertFalse(health["inventory"]["durable"])

if __name__ == "__main__":
    unittest.main()
