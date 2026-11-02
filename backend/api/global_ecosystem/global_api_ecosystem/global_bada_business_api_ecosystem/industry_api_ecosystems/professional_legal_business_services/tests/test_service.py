"""Unit tests for Professional, Legal & Business Services taxonomy service."""
import unittest
from professional_legal_business_services.service import ProfessionalServicesService

class ProfessionalServicesServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = ProfessionalServicesService()

    def test_lists_categories(self):
        self.assertEqual(len(self.service.list_categories()), 12)

    def test_gets_known_category(self):
        item = self.service.get_category("legal_services")
        self.assertIsNotNone(item)
        self.assertEqual(item["id"], "legal_services")

    def test_unknown_category_returns_none(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_search_filters_categories(self):
        self.assertTrue(self.service.list_categories("legal"))

if __name__ == "__main__":
    unittest.main()
