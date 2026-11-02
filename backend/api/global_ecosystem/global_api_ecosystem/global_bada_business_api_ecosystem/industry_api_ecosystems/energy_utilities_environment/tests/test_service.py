"""Unit tests for Energy, Utilities & Environment taxonomy service."""
import unittest
from energy_utilities_environment.service import EnergyEnvironmentService

class EnergyEnvironmentServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = EnergyEnvironmentService()

    def test_lists_categories(self):
        self.assertEqual(len(self.service.list_categories()), 12)

    def test_gets_known_category(self):
        item = self.service.get_category("renewable_energy")
        self.assertIsNotNone(item)
        self.assertEqual(item["id"], "renewable_energy")

    def test_unknown_category_returns_none(self):
        self.assertIsNone(self.service.get_category("not_a_real_category"))

    def test_search_filters_categories(self):
        self.assertTrue(self.service.list_categories("renewable"))

if __name__ == "__main__":
    unittest.main()
