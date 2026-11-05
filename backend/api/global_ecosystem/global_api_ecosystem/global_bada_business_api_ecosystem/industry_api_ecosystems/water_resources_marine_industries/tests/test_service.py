"""Regression tests for the Water Resources & Marine Industries service."""

import unittest

from ..catalog import CATEGORIES
from ..service import WaterMarineService


class WaterMarineServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = WaterMarineService()

    def test_lists_all_categories(self):
        self.assertEqual(len(self.service.list_categories()), 12)

    def test_category_ids_are_unique(self):
        ids = [item["id"] for item in CATEGORIES]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_category_has_name_and_subcategories(self):
        for item in CATEGORIES:
            with self.subTest(category=item["id"]):
                self.assertTrue(item["name"])
                self.assertTrue(item["subcategories"])

    def test_returns_known_category(self):
        self.assertIsNotNone(self.service.get_category("water_resources"))

    def test_returns_none_for_unknown_category(self):
        self.assertIsNone(self.service.get_category("unknown"))

    def test_filters_categories_by_name_or_subcategory(self):
        self.assertEqual(
            [item["id"] for item in self.service.list_categories("desalination")],
            ["water_treatment"],
        )

    def test_status_discloses_scaffold_and_data_limits(self):
        status = self.service.get_status()
        self.assertEqual(status["domain_id"], "water_resources_marine_industries")
        self.assertEqual(status["status"], "taxonomy_scaffold")
        self.assertEqual(status["category_count"], 12)
        self.assertIn("india", status["coverage"])
        self.assertIn("global", status["coverage"])
        self.assertIn("not verified", status["note"])


if __name__ == "__main__":
    unittest.main()
