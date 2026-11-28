import unittest
from ..domain_catalog import list_domains,validate_mappings,get_domain
from ..manager import get_manager
from ..policy import is_allowed
class BusinessTests(unittest.TestCase):
 def test_catalog_mapping(self): self.assertGreaterEqual(len(list_domains()),45); self.assertTrue(validate_mappings()["valid"]); self.assertIsNotNone(get_domain("solar_epc_installation"))
 def test_classification(self):
  m=get_manager(); self.assertEqual(m.catalog()["layer"],"GLOBAL_BADA_BUSINESS_CORE"); self.assertTrue(m.classify_service("solar_epc_installation","SERVICE")["valid"]); self.assertFalse(m.classify_service("solar_epc_installation","NOPE")["valid"])
 def test_policy(self): self.assertTrue(is_allowed("CLASSIFY_SERVICE")); self.assertFalse(is_allowed("EXECUTE_GRID_OPERATIONS"))
if __name__=="__main__": unittest.main()
