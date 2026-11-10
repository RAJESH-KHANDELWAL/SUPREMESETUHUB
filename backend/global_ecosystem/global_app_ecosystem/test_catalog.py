"""Offline integrity tests for the Bharat-to-global APP catalog."""
import unittest
from backend.global_ecosystem.global_app_ecosystem import (
 list_app_providers,get_app_provider,validate_app_provider_registry,
 list_app_types,list_app_capability_groups,get_scope_catalog,list_domain_ids,
)
class GlobalAppCatalogTests(unittest.TestCase):
 def test_provider_catalog_is_populated_and_unique(self):
  rows=list_app_providers();self.assertGreaterEqual(len(rows),70)
  self.assertEqual(len({x["id"] for x in rows}),len(rows));self.assertEqual(validate_app_provider_registry(),())
 def test_bharat_and_global_providers_are_present(self):
  self.assertIsNotNone(get_app_provider("zoho"));self.assertIsNotNone(get_app_provider("google"))
  self.assertTrue(list_app_providers(origin="india"));self.assertTrue(list_app_providers(origin="global"))
 def test_catalog_does_not_claim_live_integrations(self):
  self.assertTrue(all(x["integration_status"]=="catalog_only" for x in list_app_providers()))
  self.assertTrue(all(x["live_connection_verified"] is False for x in list_app_providers()))
 def test_provider_results_are_defensive_copies(self):
  item=get_app_provider("google");item["name"]="corrupted";self.assertEqual(get_app_provider("google")["name"],"Google")
 def test_app_types_and_capabilities(self):
  ids={x["id"] for x in list_app_types()}
  self.assertTrue({"native_mobile","web_app","desktop_app","progressive_web_app","saas_app"}.issubset(ids))
  self.assertGreaterEqual(len(list_app_capability_groups()),10)
 def test_scope_is_broad_and_bharat_to_global(self):
  ids=set(list_domain_ids());self.assertIn("bharat_india_apps",ids);self.assertIn("global_world_regional_apps",ids)
  self.assertGreaterEqual(len(ids),25);self.assertEqual(len(get_scope_catalog()["domains"]),len(ids))
if __name__=="__main__":unittest.main()
