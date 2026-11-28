import unittest

from .models import ConnectionRequest
from .service import GlobalConnectionService


class FakeAdapter:
    def connect(self, connection):
        return {"success": True}

    def disconnect(self, connection):
        return {"success": True}


class GlobalConnectionTests(unittest.TestCase):
    def setUp(self):
        self.service = GlobalConnectionService(adapters={"fake": FakeAdapter()})
        self.request = ConnectionRequest("c1", "provider", "server", "api", "https")

    def test_register_and_approval_gate(self):
        self.assertTrue(self.service.register(self.request)["success"])
        self.assertEqual(self.service.manager.connections["c1"].namespace, "global")
        self.assertEqual(self.service.authorize("c1")["error"], "APPROVAL_REQUIRED")
        self.assertTrue(self.service.authorize("c1", approved=True)["success"])

    def test_connect_uses_adapter(self):
        self.service.register(self.request)
        self.service.authorize("c1", approved=True)
        self.assertTrue(self.service.connect("c1", "fake")["success"])

    def test_missing_adapter_fails_closed(self):
        service = GlobalConnectionService()
        service.register(self.request)
        service.authorize("c1", approved=True)
        self.assertEqual(service.connect("c1", "missing")["error"], "CONNECTION_ADAPTER_NOT_CONFIGURED")


if __name__ == "__main__":
    unittest.main()
