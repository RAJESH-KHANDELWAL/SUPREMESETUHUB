import unittest
from ..catalog import get_github_core_catalog
from ..contracts import TenantContext
from ..service import GitHubCoreEcosystemService
from ..orchestrator import GitHubCoreOrchestrator
class ProviderTests(unittest.TestCase):
 def test_twelve_families(self): self.assertEqual(len(get_github_core_catalog()["children"]),12)
 def test_no_live_claim(self): self.assertFalse(GitHubCoreEcosystemService().status()["live_connection_verified"])
 def test_partial_api_coverage(self): self.assertEqual(GitHubCoreOrchestrator().health()["families_with_existing_api_routes"],2)
 def test_tenant_context(self):
  TenantContext("t","a").validate()
  with self.assertRaises(ValueError): TenantContext("","a").validate()
if __name__=="__main__": unittest.main()
