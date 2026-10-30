"""Tests for the Industry API Ecosystems service."""
import unittest
from industry_api_ecosystems.service import IndustryEcosystemService

class IndustryEcosystemServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = IndustryEcosystemService()

    def test_india_filter(self):
        items = self.service.list_industries(coverage="india")
        self.assertGreaterEqual(len(items), 17)
        self.assertTrue(all("india" in x["coverage"] for x in items))

    def test_channel_filter(self):
        items = self.service.list_industries(channel="online")
        self.assertTrue(all("online" in x["channels"] for x in items))

    def test_case_insensitive_search(self):
        items = self.service.list_industries(query="EDUCATION")
        self.assertEqual([x["id"] for x in items], ["education_learning_training"])

    def test_adult_taxonomy_opt_in(self):
        self.assertIsNone(self.service.get_industry("adult_sexual_wellness"))
        self.assertIsNotNone(self.service.get_industry("adult_sexual_wellness", include_adult=True))

    def test_unknown_industry(self):
        self.assertIsNone(self.service.get_industry("unknown_industry"))

if __name__ == "__main__":
    unittest.main()
