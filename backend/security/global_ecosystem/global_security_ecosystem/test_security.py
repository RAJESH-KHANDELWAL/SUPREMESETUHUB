"""Offline tests for GLOBAL SECURITY safe defaults and isolation."""
import unittest
from .catalog import get_capability
from .models import SecurityAsset
from .provider_base import SecurityProviderAdapter
from .service import GlobalSecurityEcosystemService
from .operations import SecurityAuthorizationRequired, SecurityCapabilityNotConfigured

class FakeProvider(SecurityProviderAdapter):
    provider_id = "aws"
    display_name = "AWS Security test adapter"
    def __init__(self):
        super().__init__(handler=lambda operation, payload: {"operation": operation, "received": payload}, health_probe=lambda: {"healthy": True})

class SecurityEcosystemTests(unittest.TestCase):
    def test_asset_rejects_secret_metadata(self):
        with self.assertRaises(ValueError):
            SecurityAsset("a1", "test", "APPLICATION", metadata={"api_key": "never"})

    def test_duplicate_asset_rejected(self):
        service = GlobalSecurityEcosystemService()
        service.register_asset(SecurityAsset("a1", "app", "APPLICATION"))
        with self.assertRaises(ValueError):
            service.register_asset(SecurityAsset("a1", "app2", "APPLICATION"))

    def test_provider_catalog_is_not_live_connection(self):
        service = GlobalSecurityEcosystemService()
        self.assertEqual(service.provider_health("aws")["status"], "NOT_CONFIGURED")
        service.register_provider("aws", FakeProvider())
        self.assertEqual(service.provider_health("aws")["status"], "HEALTHY")

    def test_authorization_required_by_default(self):
        service = GlobalSecurityEcosystemService()
        service.register_provider("aws", FakeProvider())
        with self.assertRaises(SecurityAuthorizationRequired):
            service.execute("aws", "POSTURE.READ", "list_findings", {})

    def test_authorization_must_be_literal_true(self):
        service = GlobalSecurityEcosystemService(authorizer=lambda *_: 1)
        service.register_provider("aws", FakeProvider())
        with self.assertRaises(SecurityAuthorizationRequired):
            service.execute("aws", "POSTURE.READ", "list_findings", {})

    def test_authorized_read_only_operation(self):
        service = GlobalSecurityEcosystemService(authorizer=lambda *_: True)
        service.register_provider("aws", FakeProvider())
        result = service.execute("aws", "POSTURE.READ", "list_findings", {"limit": 5}, principal={"role": "AUDITOR"})
        self.assertEqual(result["status"], "COMPLETED")
        self.assertEqual(result["access"], "READ_ONLY")

    def test_provider_rejects_secret_payload(self):
        provider = FakeProvider()
        with self.assertRaises(ValueError):
            provider.execute("list_findings", {"nested": {"api_key": "do-not-pass"}})

    def test_provider_rejects_secret_result(self):
        provider = SecurityProviderAdapter(handler=lambda *_: {"access_token": "do-not-return"})
        with self.assertRaises(ValueError):
            provider.execute("read", {})

    def test_unknown_capability_rejected(self):
        self.assertIsNone(get_capability("DELETE.PROTECTION"))

    def test_missing_provider_fails_closed(self):
        service = GlobalSecurityEcosystemService(authorizer=lambda *_: True)
        with self.assertRaises(SecurityCapabilityNotConfigured):
            service.execute("aws", "POSTURE.READ", "list_findings", {})

if __name__ == "__main__":
    unittest.main()
