import unittest
from backend.core.global_ecosystem.global_core_ecosystem.slack_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.slack_core_ecosystem.contracts import TenantContext
from backend.core.global_ecosystem.global_core_ecosystem.slack_core_ecosystem.module_service import SlackProductCoreService
from backend.core.global_ecosystem.global_core_ecosystem.slack_core_ecosystem.product_catalog import PRODUCTS
class SlackCoreTests(unittest.TestCase):
 def test_manager_catalog_only(self):
  m=get_manager();self.assertEqual(m.status()['ecosystem_id'],'SLACK-CORE-ECOSYSTEM');self.assertFalse(m.status()['live_connection_verified'])
 def test_fourteen_unique_products(self):self.assertEqual(len(PRODUCTS),14);self.assertEqual(len({p['product_id'] for p in PRODUCTS}),14)
 def test_domains_capabilities(self):
  m=get_manager();self.assertEqual(m.list_products()['count'],14);self.assertEqual(m.list_domains()['domain_count'],8);self.assertGreater(m.health()['capability_count'],20)
 def test_tenant_context(self):
  with self.assertRaises(ValueError):TenantContext('','actor').validate()
 def test_unknown_capability_denied(self):
  class Messages(SlackProductCoreService):PRODUCT_ID='SLACK_MESSAGES'
  result=Messages().authorize_capability('ADMIN_DELETE',TenantContext('tenant','actor'));self.assertFalse(result['success']);self.assertEqual(result['status'],'POLICY_DENIED')
if __name__=='__main__':unittest.main()
