import unittest
from automotive_mobility.catalog import CATEGORIES
from automotive_mobility.service import AutomotiveMobilityService

class AutomotiveMobilityServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = AutomotiveMobilityService()

    def test_category_count(self):
        self.assertEqual(len(self.service.list_categories()), 18)

    def test_category_ids_are_unique(self):
        ids = [item["id"] for item in CATEGORIES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_each_category_has_subcategories(self):
        for item in CATEGORIES:
            with self.subTest(category=item["id"]):
                self.assertTrue(item["subcategories"])

    def test_known_category(self):
        self.assertIsNotNone(self.service.get_category("passenger_vehicles"))

    def test_new_category(self):
        self.assertIsNotNone(self.service.get_category("roadside_assistance"))

    def test_unknown_category(self):
        self.assertIsNone(self.service.get_category("unknown"))

    def test_query_filter(self):
        self.assertTrue(self.service.list_categories("battery"))

if __name__ == "__main__":
    unittest.main()
