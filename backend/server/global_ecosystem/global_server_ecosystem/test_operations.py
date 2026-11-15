"""Offline tests for GLOBAL SERVER ECOSYSTEM operational boundaries."""
import unittest
from .operation_catalog import list_capabilities
from .operations import (
    ServerOperationService,
    ServerCapabilityNotConfigured,
    UnknownServerCapability,
)

class FakeOperationAdapter:
    def execute(self, operation, payload):
        return {"operation": operation, "payload": payload, "adapter": "test"}

class GlobalServerOperationTests(unittest.TestCase):
    def test_catalog_is_complete_and_unconfigured_by_default(self):
        service = ServerOperationService()
        self.assertGreaterEqual(len(list_capabilities()), 7)
        self.assertTrue(all(
            row["status"] == "NOT_CONFIGURED"
            for row in service.status()["capabilities"]
        ))

    def test_missing_adapter_fails_closed(self):
        with self.assertRaises(ServerCapabilityNotConfigured):
            ServerOperationService().execute("PROVISIONING", "create", {"size": "small"})

    def test_unknown_capability_is_rejected(self):
        with self.assertRaises(UnknownServerCapability):
            ServerOperationService().register_adapter("UNKNOWN", FakeOperationAdapter())

    def test_registered_adapter_receives_operation_and_payload(self):
        service = ServerOperationService()
        service.register_adapter("DEPLOYMENT", FakeOperationAdapter())
        result = service.execute("deployment", "release", {"version": "1.0"})
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["result"]["payload"]["version"], "1.0")

    def test_duplicate_registration_requires_replace(self):
        service = ServerOperationService()
        service.register_adapter("BACKUP", FakeOperationAdapter())
        with self.assertRaises(ValueError):
            service.register_adapter("BACKUP", FakeOperationAdapter())
        service.register_adapter("BACKUP", FakeOperationAdapter(), replace=True)

    def test_bad_adapter_result_is_not_reported_as_success(self):
        class BadAdapter:
            def execute(self, operation, payload):
                return "pretend-success"
        service = ServerOperationService()
        service.register_adapter("MONITORING", BadAdapter())
        with self.assertRaises(TypeError):
            service.execute("MONITORING", "collect")

if __name__ == "__main__":
    unittest.main()
