"""Tests for the Industry API Ecosystems service."""
import unittest
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.industry_api_ecosystems.service import IndustryEcosystemService
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.industry_api_ecosystems.router_coverage import get_industry_router_coverage

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

    def test_router_coverage_is_explicit_and_reconciles_registry(self):
        report = get_industry_router_coverage()
        self.assertEqual(report["registered_industry_count"], 39)
        self.assertEqual(report["dedicated_router_count"], 27)
        self.assertEqual(report["missing_dedicated_router_count"], 12)
        self.assertEqual(
            set(report["routed_industry_ids"]) | set(report["missing_industry_ids"]),
            {item["id"] for item in self.service.list_industries(include_adult=True)},
        )
        self.assertFalse(
            set(report["routed_industry_ids"]) & set(report["missing_industry_ids"])
        )

    def test_unknown_industry(self):
        self.assertIsNone(self.service.get_industry("unknown_industry"))

if __name__ == "__main__":
    unittest.main()
