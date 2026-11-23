"""Offline tests for global employment Core."""
import unittest
from manager import get_manager
class EmploymentCoreTests(unittest.TestCase):
 def setUp(self): self.m=get_manager()
 def test_catalog_ready_but_not_live(self): self.assertEqual(self.m.status()["status"],"CORE_CATALOG_READY"); self.assertFalse(self.m.status()["live_data_verified"])
 def test_domains_unique_and_broad(self):
  ids=[x["domain_id"] for x in self.m.list_domains()]; self.assertEqual(len(ids),len(set(ids))); self.assertGreaterEqual(len(ids),12)
 def test_government_and_remote_topics(self): self.assertTrue(self.m.search("government")); self.assertTrue(self.m.search("remote"))
 def test_record_validation(self): self.assertTrue(self.m.validate_record({"record_id":"E-1","name":"Example"})["success"])
 def test_sensitive_trait_rejected(self): self.assertFalse(self.m.validate_record({"record_id":"E-2","name":"Example","religion":"x"})["success"])
if __name__=="__main__": unittest.main()
