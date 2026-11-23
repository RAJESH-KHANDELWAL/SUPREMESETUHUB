import unittest
from ..domain_catalog import DOMAINS, get_domain
from ..manager import get_manager
from ..policy import authorize, validate_fields, validate_provider_claim
class HospitalityBusinessTests(unittest.TestCase):
    def test_service_domains_are_populated(self): self.assertGreaterEqual(len(DOMAINS), 9)
    def test_domain_search(self): self.assertIsNotNone(get_domain("business_strategy")); self.assertTrue(get_manager().search("revenue"))
    def test_manager_does_not_claim_live_delivery(self): self.assertFalse(get_manager().health()["service_delivery_enabled"])
    def test_sensitive_fields_blocked(self): self.assertFalse(validate_fields(["supplier_name","access_token"])["allowed"])
    def test_provider_claim_requires_evidence(self): self.assertFalse(validate_provider_claim("verified")["allowed"]); self.assertTrue(validate_provider_claim("verified",True)["allowed"])
    def test_contract_action_requires_consent(self): self.assertFalse(authorize("sign_contract",True,True,False)["allowed"])
if __name__ == "__main__": unittest.main()
