import json
import unittest
from pathlib import Path
from ..ecosystem_config import PRODUCT_ID, PRODUCT_NAME, LIVE_CONNECTION_ENABLED
class ContractTests(unittest.TestCase):
    def test_identity(self):
        self.assertEqual(PRODUCT_ID, "creative_cloud")
        self.assertTrue(PRODUCT_NAME)
    def test_manifest_contract(self):
        data=json.loads((Path(__file__).parents[1]/"ecosystem_manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(data["product_id"],PRODUCT_ID)
        self.assertEqual(data["product_name"],PRODUCT_NAME)
        self.assertFalse(data["live_connection"])
    def test_not_live_by_default(self): self.assertFalse(LIVE_CONNECTION_ENABLED)
if __name__ == "__main__": unittest.main()
