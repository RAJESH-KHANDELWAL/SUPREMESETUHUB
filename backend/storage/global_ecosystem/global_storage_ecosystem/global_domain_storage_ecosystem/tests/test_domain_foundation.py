import unittest
from global_domain_storage_ecosystem.domain_catalog import DOMAIN_CATEGORIES
from global_domain_storage_ecosystem.domain_models import DomainRecord
from global_domain_storage_ecosystem.domain_registry import DomainRegistry
from global_domain_storage_ecosystem.domain_service import DomainStorageService
class DomainFoundationTests(unittest.TestCase):
 def test_catalog(self): self.assertGreaterEqual(len(DOMAIN_CATEGORIES),8)
 def test_normalization(self): self.assertEqual(DomainRecord("d1","Example.COM.").domain_name,"example.com")
 def test_duplicate_id(self):
  r=DomainRegistry(); r.register(DomainRecord("d1","example.com"))
  with self.assertRaises(ValueError): r.register(DomainRecord("d1","example.net"))
 def test_no_false_live_connection(self): self.assertFalse(DomainStorageService().health()["external_connections_verified"])
if __name__=="__main__": unittest.main()
