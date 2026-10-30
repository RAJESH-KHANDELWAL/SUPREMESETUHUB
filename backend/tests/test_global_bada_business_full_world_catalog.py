import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_catalog import BUSINESS_CATEGORIES
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_world_catalog import GLOBAL_WORLD_CATALOG
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.service import BusinessEcosystemService


class FullGlobalWorldCatalogueTests(unittest.TestCase):
    def setUp(self):
        self.service = BusinessEcosystemService()

    def test_catalog_contains_all_world_domains(self):
        self.assertGreaterEqual(len(GLOBAL_WORLD_CATALOG), 32)
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
        self.assertEqual(result["count"], sum(1 for item in GLOBAL_WORLD_CATALOG if not item.get("adult_only")))
        self.assertTrue(all(not item.get("adult_only") for item in result["global_world_domains"]))

    def test_adult_domains_only_included_by_explicit_catalog_filter(self):
        result = self.service.list_global_world_catalog(include_adult=True)
        self.assertEqual(result["count"], len(GLOBAL_WORLD_CATALOG))

    def test_people_and_jobs_are_owned_by_people_life(self):
        people = self.service.get_global_world_catalog_domain("people-life-households-family")
        jobs = self.service.get_global_world_catalog_domain("jobs-careers-workforce")
        self.assertEqual(people["owner_ecosystem"], "global-people-life")
        self.assertEqual(jobs["owner_ecosystem"], "global-people-life")

    def test_offline_online_hybrid_business_catalogue_is_complete(self):
        result = self.service.list_work_business()
        self.assertEqual(result["count"], sum(1 for item in BUSINESS_CATEGORIES if not item.get("adult_only")))
        self.assertTrue(all(item["delivery_modes"] for item in result["sectors"]))
        self.assertEqual(set(result["facets"]["delivery_modes"]), {"offline", "online", "hybrid"})
        self.assertIn("freelance", result["facets"]["work_modes"])
        self.assertIn("business_owner", result["facets"]["work_modes"])

    def test_work_business_catalogue_filters_delivery_mode(self):
        result = self.service.list_work_business(channel="online")
        self.assertTrue(all("online" in item["modes"] for item in result["sectors"]))

    def test_adult_business_sectors_require_explicit_catalogue_filter(self):
        hidden = self.service.list_work_business()
        shown = self.service.list_work_business(include_adult=True)
        self.assertLess(hidden["count"], shown["count"])
        self.assertTrue(all(not item.get("adult_only") for item in hidden["sectors"]))

    def test_catalog_search_finds_subgroups(self):
        results = self.service.search_global_world_catalog("aquaculture")
        self.assertEqual(results[0]["id"], "agriculture-food-natural-resources")


if __name__ == "__main__":
    unittest.main()
