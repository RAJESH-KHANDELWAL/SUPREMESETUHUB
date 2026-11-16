import unittest
from ..contracts import CATEGORY_ID, EXECUTION_ENABLED, STATUS


class CategoryContractTests(unittest.TestCase):
    def test_category_is_metadata_only(self):
        self.assertEqual(CATEGORY_ID, "dns_services")
        self.assertEqual(STATUS, "CORE_CATEGORY_CATALOG_ONLY")
        self.assertFalse(EXECUTION_ENABLED)


if __name__ == "__main__":
    unittest.main()
