import unittest
from ..domain_catalog import list_domains,get_domain,search_domains
from ..region_catalog import list_regional_frameworks,get_regional_framework
from ..manager import get_manager
from ..policy import is_allowed
class CoreTests(unittest.TestCase):
 def test_catalog(self): self.assertGreaterEqual(len(list_domains()),40); self.assertEqual(len({x["domain_id"] for x in list_domains()}),len(list_domains())); self.assertIsNotNone(get_domain("solar_energy")); self.assertTrue(search_domains("climate"))
 def test_regions(self): self.assertEqual(set(list_regional_frameworks()),{"bharat","global"}); self.assertEqual(get_regional_framework("GLOBAL")["region_id"],"GLOBAL")
 def test_manager(self): self.assertEqual(get_manager().catalog()["layer"],"GLOBAL_CORE"); self.assertEqual(get_manager().status()["domain_count"],len(list_domains()))
 def test_policy(self): self.assertTrue(is_allowed("GET_DOMAIN")); self.assertFalse(is_allowed("DISPATCH_GRID"))
if __name__=="__main__": unittest.main()
