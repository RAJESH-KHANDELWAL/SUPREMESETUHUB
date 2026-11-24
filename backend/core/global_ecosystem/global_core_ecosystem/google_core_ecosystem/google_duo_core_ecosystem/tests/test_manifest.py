import unittest
from ..ecosystem_config import PRODUCT_ID,LIVE_CONNECTION_ENABLED
class TestManifest(unittest.TestCase):
 def test_id(self):self.assertEqual(PRODUCT_ID,"google_duo")
 def test_not_live(self):self.assertFalse(LIVE_CONNECTION_ENABLED)
