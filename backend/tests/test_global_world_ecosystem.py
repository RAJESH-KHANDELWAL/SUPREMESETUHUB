import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_world_api_ecosystem.catalog import DOMAINS
from backend.api.global_ecosystem.global_api_ecosystem.global_world_api_ecosystem.routes import router
from backend.api.global_ecosystem.global_api_ecosystem.global_world_api_ecosystem.service import GlobalWorldService


class GlobalWorldEcosystemTests(unittest.TestCase):
    def setUp(self):
        self.service = GlobalWorldService()

    def test_catalog_has_broad_world_coverage(self):
        self.assertGreaterEqual(len(DOMAINS), 25)
        ids = {item["id"] for item in DOMAINS}
        self.assertIn("education-students-learning", ids)
        self.assertIn("jobs-careers-workforce", ids)
        self.assertIn("entrepreneurship-startups-enterprise", ids)
        self.assertIn("micro-small-traditional-work", ids)
        self.assertIn("future-emerging-industries", ids)

    def test_adult_domains_are_hidden_by_default(self):
        result = self.service.list_domains()
        self.assertTrue(all(not item.get("adult_only") for item in result["domains"]))
        self.assertEqual(result["count"], len(result["domains"]))

    def test_adult_domains_are_separately_classified(self):
        result = self.service.list_domains(include_adult=True)
        adult = [item for item in result["domains"] if item.get("adult_only")]
        self.assertGreaterEqual(len(adult), 2)
        self.assertTrue(all(item.get("minimum_age") == 18 for item in adult))

    def test_search_and_domain_lookup(self):
        results = self.service.search_domains("student")
        self.assertTrue(any(item["id"] == "education-students-learning" for item in results))
        self.assertIsNotNone(self.service.get_domain("jobs-careers-workforce"))
        self.assertIsNone(self.service.get_domain("adult-media-entertainment"))
        self.assertIsNotNone(self.service.get_domain("adult-media-entertainment", include_adult=True))

    def test_router_exposes_discovery_endpoints(self):
        paths = {route.path for route in router.routes}
        self.assertIn("/api/v1/global-world/status", paths)
        self.assertIn("/api/v1/global-world/domains", paths)
        self.assertIn("/api/v1/global-world/domains/search", paths)
        self.assertIn("/api/v1/global-world/ecosystems", paths)


if __name__ == "__main__":
    unittest.main()
