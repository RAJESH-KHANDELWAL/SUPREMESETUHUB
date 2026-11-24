import unittest
from ..ecosystem_config import PRODUCT_ID,PRODUCT_NAME,LIVE_CONNECTION_ENABLED
class ContractTests(unittest.TestCase):
 def test_identity(self):self.assertEqual(PRODUCT_ID,"google_authenticator");self.assertTrue(PRODUCT_NAME)
 def test_not_live(self):self.assertFalse(LIVE_CONNECTION_ENABLED)
if __name__=="__main__":unittest.main()
