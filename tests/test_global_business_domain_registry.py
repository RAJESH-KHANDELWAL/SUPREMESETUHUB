import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.domain_registry import (
    DOMAIN_REGISTRY, get_domain, list_domains, search_domains, validate_domain_registry,
)


class GlobalBusinessDomainRegistryTests(unittest.TestCase):
    def test_registry_has_twelve_domain_packages(self):
        self.assertEqual(len(DOMAIN_REGISTRY), 12)
        self.assertEqual(len(list_domains()), 11)
        self.assertEqual(sum(item["subcategory_count"] for item in DOMAIN_REGISTRY), 248)

    def test_subcategory_ids_are_present_and_unique_within_domains(self):
        for domain in DOMAIN_REGISTRY:
            values = domain["subcategory_ids"]
            self.assertTrue(values)
            self.assertEqual(len(values), len(set(values)))
            self.assertTrue(all(value == value.lower() and " " not in value for value in values))

    def test_adult_domain_is_excluded_by_default(self):
        adult = next(item for item in DOMAIN_REGISTRY if item["adult_only"])
        self.assertIsNone(get_domain(adult["id"]))
        self.assertIsNotNone(get_domain(adult["id"], include_adult=True))
        self.assertNotIn(adult["id"], {item["id"] for item in list_domains()})

    def test_search_finds_domain_subcategory(self):
        matches = search_domains("web_development")
        self.assertTrue(any(item["domain_id"] == "freelance_gig_independent_work" for item in matches))

    def test_api_routes_are_registered(self):
        from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.routes import router
        paths = {route.path for route in router.routes}
        self.assertIn("/api/v1/global-ecosystem/business/domains", paths)
        self.assertIn("/api/v1/global-ecosystem/business/domains/search", paths)
        self.assertIn("/api/v1/global-ecosystem/business/domains/integrity", paths)
        self.assertIn("/api/v1/global-ecosystem/business/domains/{domain_id}", paths)

    def test_registry_integrity_is_structurally_valid(self):
        result = validate_domain_registry()
        self.assertTrue(result["structurally_valid"])
        self.assertEqual(result["domain_count"], 12)
        self.assertTrue(result["adult_excluded_by_default"])


if __name__ == "__main__":
    unittest.main()
