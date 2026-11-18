"""AWS API Gateway family manifest/config consistency tests."""
import json
import unittest
from pathlib import Path

class TestAwsFamilyManifest(unittest.TestCase):
    def test_manifest_matches_family_config(self):
        root = Path(__file__).resolve().parents[1]
        manifest = json.loads((root / "ecosystem_manifest.json").read_text(encoding="utf-8"))
        namespace = {}
        exec((root / "ecosystem_config.py").read_text(encoding="utf-8"), namespace)
        self.assertEqual(manifest["ecosystem_id"], namespace["ECOSYSTEM_ID"])
        self.assertEqual(manifest["capabilities"], namespace["CAPABILITIES"])
        self.assertFalse(manifest["live_connection_verified"])
