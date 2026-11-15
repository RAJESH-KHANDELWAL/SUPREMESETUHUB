import unittest
from ..ecosystem_service import describe

class CategoryTests(unittest.TestCase):
    def test_safe_default(self):
        state = describe()
        self.assertEqual(state["connection_state"], "NOT_CONFIGURED")
        self.assertFalse(state["storage_operations_enabled"])

if __name__ == "__main__":
    unittest.main()
