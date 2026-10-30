"""Unit tests for the industry taxonomy service."""
import unittest

from industry_ecosystems.service import IndustryEcosystemService


class IndustryEcosystemServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = IndustryEcosystemService()

    def test_lists_industries_for_india(self):
        items = self.service.list_industries(coverage="india")
        self.assertGreaterEqual(len(items), 17)
        self.assertTrue(all("india" in item["coverage"] for item in items))

    def test_filters_by_channel(self):
        items = self.service.list_industries(channel="online")
        self.assertTrue(all("online" in item["channels"] for item in items))

    def test_search_is_case_insensitive(self):
        items = self.service.list_industries(query="EDUCATION")
        self.assertEqual([item["id"] for item in items], ["education_learning_training"])

    def test_adult_domain_is_opt_in(self):
        hidden = self.service.get_industry("adult_sexual_wellness")
        visible = self.service.get_industry("adult_sexual_wellness", include_adult=True)
        self.assertIsNone(hidden)
        self.assertIsNotNone(visible)

    def test_unknown_industry_returns_none(self):
        self.assertIsNone(self.service.get_industry("not_a_real_industry"))


if __name__ == "__main__":
    unittest.main()
