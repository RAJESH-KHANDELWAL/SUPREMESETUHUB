import unittest
from salesforce_core_ecosystem.manager import get_manager
class SalesforceCoreTests(unittest.TestCase):
 def setUp(self): self.m=get_manager()
 def test_metadata_status(self):
  s=self.m.status(); self.assertEqual(s["provider_id"],"salesforce"); self.assertEqual(s["product_count"],14); self.assertFalse(s["live_connections_verified"]); self.assertFalse(s["api_transport_in_core"])
 def test_unique_products(self):
  p=self.m.list_products(); self.assertEqual(len(p),14); self.assertEqual(len({x["product_id"] for x in p}),14); self.assertTrue(all(x["enabled"] for x in p))
 def test_domains_cover_products(self):
  ds=self.m.list_domains(); ids={d["id"] for d in ds}; ps=self.m.list_products(); self.assertTrue(all(p["domain_id"] in ids for p in ps)); self.assertEqual(sum(len(self.m.products_by_domain(d["id"])) for d in ds),len(ps))
 def test_lookup_routes_manager(self):
  p=self.m.get_product("rest"); self.assertEqual(p["product_id"],"SALESFORCE_REST"); self.assertEqual(self.m.product_manager("rest").describe()["slug"],"rest")
 def test_unknown_product_rejected(self):
  with self.assertRaises(KeyError): self.m.product_manager("unknown").describe()
 def test_policy_externalizes_secrets(self):
  p=self.m.policy(); self.assertEqual(p["credential_storage"],"EXTERNAL_SECRET_STORE_ONLY"); self.assertFalse(p["api_transport_in_core"])
if __name__=="__main__": unittest.main()
