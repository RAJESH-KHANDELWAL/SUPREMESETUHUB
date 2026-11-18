import unittest
from backend.core.global_ecosystem.global_core_ecosystem.global_individual_core_ecosystem.catalog import ECOSYSTEM,get_capability,list_capabilities
from backend.core.global_ecosystem.global_core_ecosystem.global_individual_core_ecosystem.orchestrator import GlobalIndividualCoreOrchestrator
from backend.core.global_ecosystem.global_core_ecosystem.global_individual_core_ecosystem.policy import GlobalIndividualCorePolicy
class GlobalIndividualCoreTests(unittest.TestCase):
 def test_registry_count_and_unique_ids(self):
  items=list_capabilities();self.assertEqual(len(items),29);self.assertEqual(len({x["id"] for x in items}),29)
 def test_sensitive_classification(self):self.assertIn("CONSENT",GlobalIndividualCorePolicy.classify_capability("ADULT_CONSENT"))
 def test_lookup_returns_copy(self):
  x=get_capability("individual-wallet-finance");x["name"]="MUTATED";self.assertNotEqual(get_capability("individual-wallet-finance")["name"],"MUTATED")
 def test_catalog_does_not_claim_live_connection(self):
  self.assertIsNone(ECOSYSTEM["api_available"]);self.assertFalse(ECOSYSTEM["live_connection_verified"]);self.assertEqual(ECOSYSTEM["api_calls_performed"],0)
 def test_orchestrator_health(self):
  o=GlobalIndividualCoreOrchestrator();self.assertEqual(o.health()["capability_count"],29);self.assertGreater(o.taxonomy()["domain_count"],0)
 def test_secret_and_pii_metadata_filter(self):self.assertEqual(GlobalIndividualCorePolicy.safe_metadata({"nested":{"api_key":"x","email":"private@example.com","phone":"123","label":"ok"}}),{"nested":{"label":"ok"}})
if __name__=="__main__":unittest.main()


 def test_secret_filter_handles_compound_and_camel_case_keys(self):
  safe=GlobalIndividualCorePolicy.safe_metadata({
   "contact_email":"private@example.com",
   "accessToken":"secret",
   "bank-account":"1234",
   "display_name":"safe",
   "nested":[{"privateKey":"secret","label":"ok"}],
  })
  self.assertEqual(safe,{"display_name":"safe","nested":[{"label":"ok"}]})

 def test_invalid_tenant_context_is_wrapped_as_policy_error(self):
  from backend.core.global_ecosystem.global_core_ecosystem.global_individual_core_ecosystem.contracts import TenantContext
  from backend.core.global_ecosystem.global_core_ecosystem.global_individual_core_ecosystem.policy import GlobalIndividualCorePolicyError
  with self.assertRaises(GlobalIndividualCorePolicyError):
   GlobalIndividualCorePolicy.require_tenant_context(TenantContext(tenant_id=None,actor_id="actor"))
