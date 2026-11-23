import unittest
from ..domain_catalog import list_business_domains,get_business_domain,validate_business_domains
from ..manager import get_manager
from ..policy import is_allowed
class EducationBusinessCoreTests(unittest.TestCase):
 def test_unique_domain_ids(self):
  ids=[x["domain_id"] for x in list_business_domains()]; self.assertEqual(len(ids),len(set(ids)))
 def test_all_capabilities_classified(self): self.assertTrue(all(x["capabilities"]==["SERVICE","WORK","BUSINESS"] for x in list_business_domains()))
 def test_core_mapping(self): self.assertEqual(get_business_domain("online_courses_learning_platforms")["core_domain_id"],"digital_online_distance_learning")
 def test_manager_filter(self): self.assertEqual(len(get_manager().filter_by_capability("SERVICE")),15)
 def test_policy_validation(self):
  self.assertTrue(validate_business_domains()["valid"]); self.assertTrue(is_allowed("GET_CATALOG")); self.assertFalse(is_allowed("PROCESS_PAYMENTS"))
if __name__=="__main__": unittest.main()
