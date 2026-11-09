import unittest

from .models import BadaBusinessConnectionRequest
from .service import BadaBusinessConnectionService
from ..service import GlobalConnectionService


class FakeAdapter:
    def connect(self, connection):
        return {"success": True}

    def disconnect(self, connection):
        return {"success": True}


class BadaBusinessConnectionTests(unittest.TestCase):
    def setUp(self):
        self.global_service = GlobalConnectionService(adapters={"fake": FakeAdapter()})
        self.service = BadaBusinessConnectionService(self.global_service)
        self.request = BadaBusinessConnectionRequest("bb1", "bada_business", "server1", "api", "https")

    def test_register_and_approve(self):
        self.assertTrue(self.service.register(self.request)["success"])
        self.assertEqual(self.global_service.manager.connections["bb1"].namespace, "bada_business")
        self.assertEqual(self.service.authorize("bb1")["error"], "APPROVAL_REQUIRED")
        self.assertTrue(self.service.authorize("bb1", approved=True)["success"])

    def test_connection_uses_shared_adapter(self):
        self.service.register(self.request)
        self.service.authorize("bb1", approved=True)
        self.assertTrue(self.service.connect("bb1", "fake")["success"])

    def test_reject_unsupported_type(self):
        bad = BadaBusinessConnectionRequest("bb2", "bada_business", "server1", "unknown", "https")
        self.assertFalse(self.service.register(bad)["success"])


if __name__ == "__main__":
    unittest.main()
