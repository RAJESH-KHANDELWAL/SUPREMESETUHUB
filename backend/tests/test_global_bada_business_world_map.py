import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_catalog import BUSINESS_CATEGORIES
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_world_business_map import GLOBAL_WORLD_BUSINESS_MAP
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.service import BusinessEcosystemService


class GlobalBadaBusinessWorldMapTests(unittest.TestCase):
    def setUp(self):
        self.service = BusinessEcosystemService()

    def test_all_global_world_domains_are_mapped(self):
        self.assertGreaterEqual(len(GLOBAL_WORLD_BUSINESS_MAP), 32)
        ids = [item["world_domain_id"] for item in GLOBAL_WORLD_BUSINESS_MAP]
        self.assertEqual(len(ids), len(set(ids)))

    def test_business_category_references_exist(self):
        category_ids = {item["id"] for item in BUSINESS_CATEGORIES}
        for domain in GLOBAL_WORLD_BUSINESS_MAP:
            for category_id in domain["business_category_ids"]:
                self.assertIn(category_id, category_ids, domain["world_domain_id"])

    def test_adult_domains_are_excluded_by_default(self):
        visible = self.service.list_global_world_map()
        self.assertTrue(all(not item.get("adult_only") for item in visible["global_world_domains"]))
        self.assertGreater(
            len(GLOBAL_WORLD_BUSINESS_MAP),
            visible["count"],
        )

    def test_adult_domains_can_be_included_as_catalog_filter(self):
        visible = self.service.list_global_world_map(include_adult=True)
        self.assertEqual(visible["count"], len(GLOBAL_WORLD_BUSINESS_MAP))

    def test_people_and_relationship_domains_keep_separate_owners(self):
        people = self.service.get_global_world_domain("people-life-households-family")
        relationships = self.service.get_global_world_domain("relationships-love-romance")
        jobs = self.service.get_global_world_domain("jobs-careers-workforce")
        self.assertEqual(people["owner_ecosystem"], "global-people-life")
        self.assertEqual(relationships["owner_ecosystem"], "global-relationship-intimacy")
        self.assertEqual(jobs["owner_ecosystem"], "global-people-life")

    def test_unknown_world_domain_returns_none(self):
        self.assertIsNone(self.service.get_global_world_domain("not-a-real-domain"))


if __name__ == "__main__":
    unittest.main()
