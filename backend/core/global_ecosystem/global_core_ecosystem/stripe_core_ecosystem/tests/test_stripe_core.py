"""Behavioral and structural tests for Stripe Core."""
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.catalog import get_stripe_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.contracts import TenantContext,SecretReference
from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.policy import StripeCorePolicy,StripeCorePolicyError
ROOT=Path(__file__).resolve().parents[1]
class StripeCoreTests(unittest.TestCase):
 def test_all_22_product_managers_exist(self):
  children=get_stripe_core_catalog()["children"];self.assertEqual(len(children),22);self.assertEqual(len({p["api_family"] for p in children}),22)
  for child in children:self.assertTrue((ROOT/child["module"]/"manager.py").is_file(),child["module"])
 def test_manager_inventory_and_domains(self):
  manager=get_manager();self.assertEqual(manager.list_products()["count"],22);self.assertEqual(manager.list_domains()["product_count"],22);self.assertEqual(len(manager.dependency_map()["edges"]),22);self.assertEqual(manager.health()["live_connections_verified"],0)
 def test_no_live_connection_claim(self):
  catalog=get_stripe_core_catalog();self.assertFalse(catalog["live_connection_verified"]);self.assertTrue(all(p["connected"] is False for p in catalog["children"]))
 def test_tenant_and_secret_reference_contracts(self):
  TenantContext("tenant-1","actor-1").validate();self.assertEqual(SecretReference("vault","stripe/tenant-1").provider,"vault")
  with self.assertRaises(ValueError):TenantContext("","actor").validate()
 def test_policy_and_sanitization(self):
  product={"enabled":True,"capabilities":["PAYMENT_INTENT_STATE"]};StripeCorePolicy.validate_capability(product,"PAYMENT_INTENT_STATE");self.assertIn("SENSITIVE",StripeCorePolicy.classify_capability("PAYMENT_INTENT_STATE"))
  with self.assertRaises(StripeCorePolicyError):StripeCorePolicy.validate_capability(product,"NOT_REGISTERED")
  self.assertNotIn("secret_key",StripeCorePolicy.sanitize({"secret_key":"x","safe":"ok"}))
 def test_legacy_service_compatibility(self):
  from backend.core.global_ecosystem.global_core_ecosystem.stripe_core_ecosystem.service import StripeCoreEcosystemService
  self.assertEqual(StripeCoreEcosystemService().status()["module_count"],22)
if __name__=="__main__":unittest.main()
