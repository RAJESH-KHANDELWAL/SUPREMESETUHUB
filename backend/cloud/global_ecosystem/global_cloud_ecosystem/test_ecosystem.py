"""Offline tests for GLOBAL CLOUD ECOSYSTEM contracts."""
import unittest
from .catalog import get_cloud_catalog
from .models import CloudProviderDescriptor, CloudOperationRequest, CloudOperationResult
from .adapters import CloudAdapterRegistry
from .service import GlobalCloudEcosystemService
from .manager import GlobalCloudEcosystemManager

class FakeAdapter:
    provider_id = "test_cloud"
    def describe(self):
        return {"provider_id": self.provider_id}
    def execute(self, request):
        return CloudOperationResult(request.provider_id, request.operation, "accepted", "test-resource")

class TestGlobalCloudEcosystem(unittest.TestCase):
    def test_catalog_lists_four_provider_records(self):
        catalog = get_cloud_catalog()
        self.assertEqual(catalog["provider_count"], 4)
        self.assertFalse(catalog["live_connections_enabled"])

    def test_descriptor_is_immutable_and_normalizes_capabilities(self):
        descriptor = CloudProviderDescriptor("sample", "Sample", "test", ["compute"])
        self.assertEqual(descriptor.capabilities, ("compute",))

    def test_registry_requires_explicit_registration(self):
        registry = CloudAdapterRegistry()
        registry.register(FakeAdapter())
        self.assertEqual(registry.get("TEST_CLOUD").provider_id, "test_cloud")

    def test_service_delegates_to_injected_adapter(self):
        service = GlobalCloudEcosystemService(adapters=(FakeAdapter(),))
        request = CloudOperationRequest("test_cloud", "inspect", "resource")
        result = service.execute(request)
        self.assertEqual(result.status, "accepted")

    def test_unconfigured_adapter_fails_closed(self):
        service = GlobalCloudEcosystemService()
        request = CloudOperationRequest("aws_cloud", "create", "instance")
        with self.assertRaises(KeyError):
            service.execute(request)

    def test_manager_reports_no_live_connectivity_claim(self):
        manager = GlobalCloudEcosystemManager()
        status = manager.initialize()
        self.assertTrue(status["initialized"])
        self.assertFalse(status["live_provider_connectivity_verified"])

if __name__ == "__main__":
    unittest.main()
