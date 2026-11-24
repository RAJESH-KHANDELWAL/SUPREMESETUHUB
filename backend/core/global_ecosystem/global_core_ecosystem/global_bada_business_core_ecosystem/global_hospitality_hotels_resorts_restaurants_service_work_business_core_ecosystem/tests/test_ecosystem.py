import unittest
from ..contracts import ECOSYSTEM_ID
from ..domain_catalog import DOMAINS, get_domain, search_domains
from ..manager import get_manager
from ..policy import authorize, validate_fields, validate_provider_claim
class HospitalityBusinessTests(unittest.TestCase):
    def test_identity_and_manager(self):
        self.assertEqual(get_manager().catalog()["ecosystem_id"],ECOSYSTEM_ID)
        self.assertTrue(get_manager().health()["catalog_ready"])
    def test_business_work_coverage(self):
        self.assertGreaterEqual(len(DOMAINS),15)
        self.assertIsNotNone(get_domain("business_strategy"))
        self.assertTrue(search_domains("freelance"))
    def test_live_delivery_not_claimed(self):
        health=get_manager().health()
        self.assertFalse(health["live_service_delivery_enabled"])
        self.assertFalse(health["payments_enabled"])
    def test_sensitive_data_and_provider_evidence(self):
        self.assertFalse(validate_fields(["access_token"])["allowed"])
        self.assertFalse(validate_provider_claim("verified")["allowed"])
        self.assertTrue(validate_provider_claim("verified",True)["allowed"])
    def test_contract_consent(self):
        self.assertFalse(authorize("sign_contract",True,True,False)["allowed"])
        self.assertTrue(authorize("sign_contract",True,True,True)["allowed"])
if __name__=="__main__": unittest.main()
