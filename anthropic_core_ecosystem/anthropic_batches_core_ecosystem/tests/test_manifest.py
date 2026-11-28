"""Offline manifest and lifecycle contract tests."""
import json
import unittest
from pathlib import Path
from ..schemas.product_schema import validate
from ..lifecycle.state import transition

class ProductManifestTests(unittest.TestCase):
    def test_manifest_is_valid_and_not_live(self):
        manifest=json.loads((Path(__file__).parents[1]/"ecosystem_manifest.json").read_text(encoding="utf-8"))
        self.assertTrue(validate(manifest))
        self.assertFalse(manifest["live_connection"])
        self.assertEqual(manifest["product_id"],"anthropic_batches")

    def test_connected_requires_external_verification(self):
        with self.assertRaises(ValueError):
            transition("ADAPTER_PENDING","CONNECTED")
        self.assertEqual(transition("ADAPTER_PENDING","CONNECTED",external_verification=True)["to"],"CONNECTED")

if __name__=="__main__":
    unittest.main()
