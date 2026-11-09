"""Offline tests for Bada Business CLOUD ecosystem."""
import unittest
from .catalog import get_bada_business_cloud_catalog
from .models import BadaBusinessCloudRequest, BadaBusinessCloudResult
from .service import BadaBusinessCloudService

class FakeSharedCloudService:
    def __init__(self):
        self.calls = []
    def execute(self, request):
        self.calls.append(request)
        return type("Result", (), {"status": "accepted", "details": {"resource": request.resource}})()

class TestBadaBusinessCloud(unittest.TestCase):
    def test_catalog_has_six_capabilities(self):
        self.assertEqual(get_bada_business_cloud_catalog()["capability_count"], 6)

    def test_mutating_operation_requires_approval(self):
        service = BadaBusinessCloudService(FakeSharedCloudService())
        result = service.execute(BadaBusinessCloudRequest(
            "application_hosting", "deploy_application", "aws_cloud", "bb-app"
        ))
        self.assertEqual(result.status, "pending_approval")

    def test_unconfigured_service_fails_closed_after_approval(self):
        service = BadaBusinessCloudService()
        request = BadaBusinessCloudRequest(
            "application_hosting", "deploy_application", "aws_cloud", "bb-app", approved=True
        )
        with self.assertRaises(RuntimeError):
            service.execute(request)

    def test_approved_operation_delegates_to_shared_cloud(self):
        shared = FakeSharedCloudService()
        service = BadaBusinessCloudService(shared)
        request = BadaBusinessCloudRequest(
            "application_hosting", "deploy_application", "aws_cloud", "bb-app", approved=True
        )
        result = service.execute(request)
        self.assertEqual(result.status, "accepted")
        self.assertEqual(len(shared.calls), 1)

    def test_unknown_operation_is_rejected(self):
        service = BadaBusinessCloudService(FakeSharedCloudService())
        request = BadaBusinessCloudRequest("application_hosting", "delete_everything", "aws_cloud", "bb-app")
        with self.assertRaises(ValueError):
            service.execute(request)

if __name__ == "__main__":
    unittest.main()
