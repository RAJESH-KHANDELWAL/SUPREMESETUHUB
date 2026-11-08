"""Tests for SERVER operational capability boundaries."""
import unittest
from backend.server.operations import (
    ServerOperationService, ServerCapabilityNotConfigured, UnknownServerCapability,
)

class FakeAdapter:
    def execute(self, operation, payload):
        return {"operation": operation, "payload": payload, "provider_action": "TEST_ONLY"}

class ServerOperationTests(unittest.TestCase):
    def test_catalog_is_visible_but_not_claimed_as_configured(self):
        service = ServerOperationService()
        status = service.status()
        self.assertEqual(status["domain"], "SERVER")
        self.assertGreaterEqual(len(status["capabilities"]), 6)
        self.assertTrue(all(x["status"] == "NOT_CONFIGURED" for x in status["capabilities"]))

    def test_unconfigured_capability_fails_closed(self):
        with self.assertRaises(ServerCapabilityNotConfigured):
            ServerOperationService().execute("PROVISIONING", "create", {"size": "small"})

    def test_unknown_capability_is_rejected(self):
        with self.assertRaises(UnknownServerCapability):
            ServerOperationService().register_adapter("UNKNOWN", FakeAdapter())

    def test_registered_adapter_receives_operation_and_payload(self):
        service = ServerOperationService()
        service.register_adapter("DEPLOYMENT", FakeAdapter())
        result = service.execute("DEPLOYMENT", "release", {"version": "1.2"})
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["result"]["payload"]["version"], "1.2")

    def test_duplicate_adapter_requires_explicit_replace(self):
        service = ServerOperationService()
        service.register_adapter("MONITORING", FakeAdapter())
        with self.assertRaises(ValueError):
            service.register_adapter("MONITORING", FakeAdapter())
        service.register_adapter("MONITORING", FakeAdapter(), replace=True)

if __name__ == "__main__":
    unittest.main()
