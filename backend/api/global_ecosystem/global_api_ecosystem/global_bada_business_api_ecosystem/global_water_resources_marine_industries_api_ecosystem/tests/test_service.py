"""Regression tests for the Water Resources & Marine Industries service."""

import unittest

from ..service import WaterMarineService


class WaterMarineServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = WaterMarineService()

    def test_lists_all_categories(self):
        self.assertEqual(len(self.service.list_categories()), 12)

    def test_returns_known_category(self):
        self.assertIsNotNone(self.service.get_category("water_resources"))

    def test_returns_none_for_unknown_category(self):
        self.assertIsNone(self.service.get_category("unknown"))


if __name__ == "__main__":
    unittest.main()
