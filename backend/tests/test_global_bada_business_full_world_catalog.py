import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_catalog import BUSINESS_CATEGORIES
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_world_catalog import GLOBAL_WORLD_CATALOG
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.service import BusinessEcosystemService


class FullGlobalWorldCatalogueTests(unittest.TestCase):
    def setUp(self):
        self.service = BusinessEcosystemService()

    def test_catalog_contains_all_32_world_domains(self):
        self.assertEqual(len(GLOBAL_WORLD_CATALOG), 32)
        ids = [item["id"] for item in GLOBAL_WORLD_CATALOG]
        self.assertEqual(len(ids), len(set(ids)))

    def test_each_business_category_reference_exists(self):
        category_ids = {item["id"] for item in BUSINESS_CATEGORIES}
        for domain in GLOBAL_WORLD_CATALOG:
            for category_id in domain["business_category_ids"]:
                self.assertIn(category_id, category_ids, domain["id"])

    def test_full_catalog_has_subgroups(self):
        for domain in GLOBAL_WORLD_CATALOG:
            self.assertTrue(domain["groups"], domain["id"])

    def test_adult_domains_hidden_by_default(self):
        result = self.service.list_global_world_catalog()
        self.assertEqual(result["count"], 30)
        self.assertTrue(all(not item.get("adult_only") for item in result["global_world_domains"]))

    def test_adult_domains_only_included_by_explicit_catalog_filter(self):
        result = self.service.list_global_world_catalog(include_adult=True)
        self.assertEqual(result["count"], 32)

    def test_people_and_jobs_are_owned_by_people_life(self):
        people = self.service.get_global_world_catalog_domain("people-life-households-family")
        jobs = self.service.get_global_world_catalog_domain("jobs-careers-workforce")
        self.assertEqual(people["owner_ecosystem"], "global-people-life")
        self.assertEqual(jobs["owner_ecosystem"], "global-people-life")

    def test_catalog_search_finds_subgroups(self):
        results = self.service.search_global_world_catalog("aquaculture")
        self.assertEqual(results[0]["id"], "agriculture-food-natural-resources")


if __name__ == "__main__":
    unittest.main()
