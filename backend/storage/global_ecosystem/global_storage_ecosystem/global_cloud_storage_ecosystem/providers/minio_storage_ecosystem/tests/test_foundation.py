import unittest
from ..ecosystem_service import ProviderStorageService

class ProviderTests(unittest.TestCase):
    def test_no_false_connection_claim(self):
        state = ProviderStorageService().describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["external_connections_verified"])
        self.assertFalse(state["storage_operations_enabled"])

if __name__ == "__main__":
    unittest.main()
