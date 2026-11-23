import unittest
from ..contracts import ECOSYSTEM_ID
from ..domain_catalog import DOMAINS, get_domain, search_domains
from ..manager import get_manager
from ..policy import authorize, validate_fields
class HospitalityCoreTests(unittest.TestCase):
    def test_identity_and_manager(self):
        self.assertEqual(get_manager().catalog()["ecosystem_id"],ECOSYSTEM_ID)
        self.assertTrue(get_manager().health()["catalog_ready"])
    def test_catalog_coverage(self):
        self.assertGreaterEqual(len(DOMAINS),12)
        self.assertIsNotNone(get_domain("accommodation"))
        self.assertTrue(search_domains("hotel"))
    def test_catalog_is_defensive_copy(self):
        first=get_manager().catalog(); first["domains"]["accommodation"].append("INVALID")
        self.assertNotIn("INVALID",get_manager().catalog()["domains"]["accommodation"])
    def test_sensitive_data_and_consent(self):
        self.assertFalse(validate_fields(["card_number"])["allowed"])
        self.assertFalse(authorize("confirm_booking",True,True,False)["allowed"])
        self.assertTrue(authorize("confirm_booking",True,True,True)["allowed"])
if __name__=="__main__": unittest.main()
