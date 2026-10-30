import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_dimensions import (
    BUSINESS_DIMENSIONS,
    get_business_dimension,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.service import (
    BusinessEcosystemService,
)


class TestGlobalBadaBusinessEcosystem(unittest.TestCase):
    def setUp(self):
        self.service = BusinessEcosystemService()

    def test_business_modules_cover_core_commercial_functions(self):
        module_ids = {item["id"] for item in self.service.list_modules()["modules"]}
        self.assertTrue({
            "businesses", "companies", "products", "services", "operations",
            "marketplaces", "funding-investment", "franchising-licensing",
            "trade-global", "compliance-risk", "online-businesses",
            "offline-businesses", "hybrid-businesses",
        } <= module_ids)

    def test_dimensions_are_unique_and_have_values(self):
        ids = [item["id"] for item in BUSINESS_DIMENSIONS]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertTrue(all(item["values"] for item in BUSINESS_DIMENSIONS))

    def test_business_sizes_and_models_are_independent_dimensions(self):
        sizes = get_business_dimension("business_sizes")["values"]
        models = get_business_dimension("operating_models")["values"]
        self.assertIn("micro", sizes)
        self.assertIn("multinational", sizes)
        self.assertIn("online", models)
        self.assertIn("offline", models)
        self.assertIn("hybrid", models)

    def test_personal_roles_are_not_business_entity_types(self):
        entity_types = get_business_dimension("entity_types")["values"]
        self.assertNotIn("student", entity_types)
        self.assertNotIn("homemaker", entity_types)
        self.assertIn("home_based_business", entity_types)

    def test_unknown_dimension_returns_none(self):
        self.assertIsNone(self.service.get_dimension("not-a-dimension"))

    def test_status_reports_catalog_and_dimension_counts(self):
        status = self.service.get_status()
        self.assertEqual(status["dimension_count"], len(BUSINESS_DIMENSIONS))
        self.assertEqual(status["category_count"], len(self.service.list_categories()["categories"]))

    def test_adult_categories_remain_excluded_by_default(self):
        public_categories = self.service.list_categories()["categories"]
        all_categories = self.service.list_categories(include_adult=True)["categories"]
        self.assertTrue(all(item.get("adult_only") is not True for item in public_categories))
        self.assertGreater(len(all_categories), len(public_categories))


if __name__ == "__main__":
    unittest.main()
