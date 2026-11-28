"""Structural and behavior tests for Communication Core contracts."""
import unittest
from .catalog import get_communication_core_catalog
from .contracts import SecretReference, TenantContext
from .domain_runtime import CommunicationCoreDomainManager
from .manager import get_manager
from .module_service import CommunicationProviderCoreService
from .policy import CommunicationCorePolicy, CommunicationPolicyError

class CommunicationCoreDomainTests(unittest.TestCase):
    def test_catalog_has_unique_provider_ids_and_domains(self):
        catalog = get_communication_core_catalog()
        ids = [item["id"] for item in catalog["providers"]]
        domains = [item["domain_id"] for item in catalog["domains"]]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(len(domains), len(set(domains)))
        self.assertEqual(catalog["provider_reference_count"], len(ids))
        self.assertFalse(catalog["live_connection_verified"])

    def test_domain_manager_rejects_unknown_domain(self):
        with self.assertRaises(ValueError):
            CommunicationCoreDomainManager("NOT_A_DOMAIN")

    def test_domain_manager_is_metadata_only(self):
        result = CommunicationCoreDomainManager("PROVIDER_GOVERNANCE").status()
        self.assertEqual(result["status"], "CORE_DOMAIN_AVAILABLE")
        self.assertEqual(result["api_calls_performed"], 0)

    def test_provider_service_is_metadata_only(self):
        result = CommunicationProviderCoreService("google").status()
        self.assertFalse(result["live_connection_verified"])
        self.assertFalse(result["api_transport_in_core"])

    def test_sensitive_actions_require_authorization(self):
        with self.assertRaises(CommunicationPolicyError):
            CommunicationCorePolicy.require_explicit_authorization("SEND_MESSAGE", False)

    def test_tenant_and_secret_contracts(self):
        TenantContext("tenant", "actor").validate()
        with self.assertRaises(ValueError):
            TenantContext("", "actor").validate()
        SecretReference("vault", "secret://communication/provider")

    def test_canonical_manager_and_master_catalog(self):
        manager = get_manager()
        self.assertEqual(manager.ECOSYSTEM_ID, "GLOBAL-COMMUNICATION-CORE-ECOSYSTEM")
        summary = manager.master_catalog_summary()
        self.assertTrue(summary["available"])

if __name__ == "__main__":
    unittest.main()
