"""Offline structural tests for this ENGINE package boundary."""
import unittest
from . import ECOSYSTEM_ID, ECOSYSTEM_NAME, LAYER

class EngineBoundaryTests(unittest.TestCase):
    def test_package_is_owned_by_engine_layer(self):
        self.assertEqual(LAYER, "ENGINE")

    def test_package_exposes_stable_identity_metadata(self):
        self.assertTrue(ECOSYSTEM_ID)
        self.assertTrue(ECOSYSTEM_NAME)
        self.assertEqual(ECOSYSTEM_ID, ECOSYSTEM_ID.upper())

if __name__ == "__main__":
    unittest.main()
