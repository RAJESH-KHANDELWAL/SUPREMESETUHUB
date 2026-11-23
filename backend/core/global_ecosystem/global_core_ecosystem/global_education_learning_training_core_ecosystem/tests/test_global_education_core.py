import unittest
from ..domain_catalog import list_domains,get_domain
from ..manager import get_manager
from ..policy import is_allowed
class GlobalEducationCoreTests(unittest.TestCase):
 def test_unique_domain_ids(self):
  ids=[x["domain_id"] for x in list_domains()]; self.assertEqual(len(ids),len(set(ids)))
 def test_case_insensitive_lookup(self): self.assertEqual(get_domain("SCHOOL_EDUCATION")["name"],"School Education")
 def test_manager_catalog(self):
  m=get_manager(); self.assertEqual(m.catalog()["layer"],"GLOBAL_CORE"); self.assertEqual(m.status()["domain_count"],15)
 def test_search(self): self.assertTrue(get_manager().search("online"))
 def test_scope_policy(self): self.assertTrue(is_allowed("GET_DOMAIN")); self.assertFalse(is_allowed("ENROLL_LEARNERS"))
if __name__=="__main__": unittest.main()
