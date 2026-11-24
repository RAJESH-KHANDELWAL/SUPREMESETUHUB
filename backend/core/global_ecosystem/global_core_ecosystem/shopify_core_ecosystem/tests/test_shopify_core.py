import unittest
from backend.core.global_ecosystem.global_core_ecosystem.shopify_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.shopify_core_ecosystem.product_catalog import PRODUCTS
from backend.core.global_ecosystem.global_core_ecosystem.shopify_core_ecosystem.contracts import TenantContext
class ShopifyCoreTests(unittest.TestCase):
 def test_manager_catalog_only(self):
  m=get_manager(); self.assertEqual(m.status()["ecosystem_id"],"SHOPIFY-CORE-ECOSYSTEM"); self.assertFalse(m.status()["live_connection_verified"])
 def test_all_fifteen_products_are_unique(self):
  self.assertEqual(len(PRODUCTS),15); self.assertEqual(len({p["product_id"] for p in PRODUCTS}),15)
 def test_discovery(self):
  m=get_manager(); self.assertIsNotNone(m.get_product("SHOPIFY_ORDERS")); self.assertGreaterEqual(m.list_domains()["domain_count"],10)
 def test_tenant_context(self):
  with self.assertRaises(ValueError): TenantContext("","actor").validate()
if __name__=="__main__": unittest.main()
