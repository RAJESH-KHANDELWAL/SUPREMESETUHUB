"""Tests for Global Developer Core catalog, runtime and policy."""
import unittest
from .catalog import get_global_developer_core_catalog
from .domain_catalog import DOMAIN_DEFINITIONS
from .domain_runtime import DeveloperCoreDomainManager
from .manager import get_manager, GlobalDeveloperCoreManager
from .contracts import TenantContext, SecretReference
from .module_service import DeveloperProviderCoreService

class DeveloperCoreTests(unittest.TestCase):
    def test_catalog_identity_and_parent(self):
        c=get_global_developer_core_catalog()
        self.assertEqual(c["ecosystem_id"],"GLOBAL-DEVELOPER-CORE-ECOSYSTEM")
        self.assertEqual(c["parent_id"],"GLOBAL-CORE-ECOSYSTEM")
    def test_catalog_has_all_domain_folders(self):
        self.assertEqual(len(get_global_developer_core_catalog()["children"]),29)
        self.assertEqual(len({x["ecosystem_id"] for x in get_global_developer_core_catalog()["children"]}),29)
    def test_domains_are_unique(self):
        self.assertEqual(len(DOMAIN_DEFINITIONS),19)
        self.assertEqual(len(DOMAIN_DEFINITIONS),len(set(DOMAIN_DEFINITIONS)))
    def test_manager_singleton(self):
        self.assertIs(get_manager(),get_manager())
        self.assertIsInstance(get_manager(),GlobalDeveloperCoreManager)
    def test_health_reports_catalog_only(self):
        h=get_manager().health()
        self.assertEqual(h["product_family_count"],28)
        self.assertEqual(h["live_connections_verified"],0)
    def test_domain_runtime_rejects_unknown(self):
        with self.assertRaises(ValueError): DeveloperCoreDomainManager("NOT_A_DOMAIN")
    def test_domain_runtime_lists_modules(self):
        self.assertTrue(DeveloperCoreDomainManager("DEVELOPER_PROVIDER_PLATFORMS").status()["success"])
    def test_secret_reference_is_opaque(self):
        self.assertEqual(SecretReference("vault","path/key").reference,"path/key")
    def test_sensitive_capability_requires_authorization(self):
        s=DeveloperProviderCoreService("GLOBAL-DEVELOPER-GITHUB-DEVELOPER-CORE-ECOSYSTEM")
        result=s.authorize_capability("REPOSITORY_WRITE",TenantContext("tenant","actor"))
        self.assertFalse(result["success"])
    def test_metadata_does_not_call_api(self):
        s=DeveloperProviderCoreService("GLOBAL-DEVELOPER-GITHUB-DEVELOPER-CORE-ECOSYSTEM")
        self.assertFalse(s.status()["live_connection_verified"])

if __name__=="__main__": unittest.main()
