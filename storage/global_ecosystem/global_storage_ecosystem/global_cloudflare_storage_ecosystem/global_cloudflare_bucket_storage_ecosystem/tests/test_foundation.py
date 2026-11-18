import unittest
from ..ecosystem_models import StorageCategoryRecord
from ..ecosystem_service import StorageCategoryService

class FoundationTests(unittest.TestCase):
    def test_safe_readiness(self):
        state = StorageCategoryService().describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["external_connections_verified"])
        self.assertFalse(state["storage_operations_enabled"])

    def test_record_cannot_assert_connected(self):
        with self.assertRaises(ValueError):
            StorageCategoryRecord("r1", "sample", connection_state="CONNECTED")

if __name__ == "__main__":
    unittest.main()
