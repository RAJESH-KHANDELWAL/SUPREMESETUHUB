"""Offline tests for employment services business Core."""
import unittest
from manager import get_manager
class EmploymentServicesTests(unittest.TestCase):
 def setUp(self): self.m=get_manager()
 def test_catalog_only_status(self): self.assertEqual(self.m.status()["status"],"CORE_CATALOG_READY"); self.assertFalse(self.m.status()["live_services_verified"])
 def test_domains_unique_and_broad(self):
  ids=[x["domain_id"] for x in self.m.list_domains()]; self.assertEqual(len(ids),len(set(ids))); self.assertGreaterEqual(len(ids),15)
 def test_recruitment_and_payroll_search(self): self.assertTrue(self.m.search("recruitment")); self.assertTrue(self.m.search("payroll"))
 def test_provider_validation(self): self.assertTrue(self.m.validate_provider({"record_id":"P-1","name":"Example Provider"})["success"])
 def test_licence_and_guarantee_controls(self):
  self.assertFalse(self.m.validate_provider({"record_id":"P-2","name":"X","licensed_activity":True})["success"]); self.assertFalse(self.m.validate_provider({"record_id":"P-3","name":"X","guaranteed_job":True})["success"])
if __name__=="__main__": unittest.main()
