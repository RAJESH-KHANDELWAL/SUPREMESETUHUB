import unittest
from ..domain_catalog import DOMAINS, get_domain
from ..manager import get_manager
from ..policy import authorize, validate_fields
class HospitalityCoreTests(unittest.TestCase):
    def test_catalog_has_real_domains(self): self.assertGreaterEqual(len(DOMAINS), 8)
    def test_lookup_and_search(self): self.assertIsNotNone(get_domain("lodging")); self.assertTrue(get_manager().search("hotel"))
    def test_readiness_does_not_claim_live_operations(self): self.assertFalse(get_manager().health()["live_operations_enabled"])
    def test_sensitive_fields_are_blocked(self): self.assertFalse(validate_fields(["guest_name","card_number"])["allowed"])
    def test_booking_requires_consent(self): self.assertFalse(authorize("confirm_booking",True,True,False)["allowed"]); self.assertTrue(authorize("confirm_booking",True,True,True)["allowed"])
if __name__ == "__main__": unittest.main()
