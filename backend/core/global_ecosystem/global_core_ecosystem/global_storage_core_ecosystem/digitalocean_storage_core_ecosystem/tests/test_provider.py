import unittest
from ..ecosystem_config import PROVIDER_ID,STATUS,LIVE_CONNECTION_VERIFIED
from ..capabilities.catalog import list_capabilities
class ProviderTests(unittest.TestCase):
 def test_catalog_only(self):
  self.assertEqual(PROVIDER_ID,"digitalocean")
  self.assertEqual(STATUS,"CATALOG_ONLY")
  self.assertFalse(LIVE_CONNECTION_VERIFIED)
  self.assertTrue(list_capabilities())
if __name__=="__main__": unittest.main()
