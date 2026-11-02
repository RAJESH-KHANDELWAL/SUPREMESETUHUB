"""Tests for AgricultureFoodService."""
import unittest

from agriculture_food_natural_resources.service import AgricultureFoodService

class AgricultureFoodServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = AgricultureFoodService()

    def test_catalog_has_expected_categories(self):
        items = self.service.list_categories()
        self.assertGreaterEqual(len(items), 12)
        self.assertTrue(all(item["id"] and item["subcategories"] for item in items))

    def test_search_is_case_insensitive(self):
        items = self.service.list_categories(query="DAIRY")
        self.assertTrue(any(item["id"] == "livestock_and_dairy" for item in items))

    def test_search_matches_subcategory(self):
        items = self.service.list_categories(query="cold storage")
        self.assertTrue(any(item["id"] == "storage_cold_chain_and_logistics" for item in items))

    def test_get_category(self):
        item = self.service.get_category("crop_farming")
        self.assertEqual(item["name"], "Crop Farming & Field Agriculture")

    def test_unknown_category(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_status(self):
        status = self.service.get_status()
        self.assertEqual(status["domain_id"], "agriculture_food_natural_resources")
        self.assertEqual(status["category_count"], len(self.service.list_categories()))

if __name__ == "__main__":
    unittest.main()
