import unittest
from ..catalog import list_github_families
class CatalogTests(unittest.TestCase):
 def test_refs_and_live_state(self):
  for x in list_github_families(): self.assertTrue(x["api_catalog_ref"].endswith("_api_ecosystem")); self.assertFalse(x["live_connection_verified"])
if __name__=="__main__": unittest.main()
