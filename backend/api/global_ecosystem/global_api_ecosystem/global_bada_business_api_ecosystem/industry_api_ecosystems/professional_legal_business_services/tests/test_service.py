"""Unit tests for the Professional Services taxonomy service."""
import unittest
from professional_legal_business_services.service import ProfessionalServicesService

class ProfessionalServicesServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = ProfessionalServicesService()

    def test_lists_professional_categories(self):
        items = self.service.list_categories()
        self.assertEqual(len(items), 12)
        self.assertNotIn("legal_services", {item["id"] for item in items})

    def test_gets_known_category(self):
        item = self.service.get_category("accounting_bookkeeping")
        self.assertIsNotNone(item)
        self.assertEqual(item["id"], "accounting_bookkeeping")

    def test_legal_category_is_not_in_professional_catalog(self):
        self.assertIsNone(self.service.get_category("legal_services"))

    def test_unknown_category_returns_none(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_search_filters_categories(self):
        self.assertTrue(self.service.list_categories("accounting"))
        self.assertFalse(self.service.list_categories("litigation"))

if __name__ == "__main__":
    unittest.main()
