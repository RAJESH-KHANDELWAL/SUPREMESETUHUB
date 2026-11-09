"""End-to-end structural and service tests for Company and Platforms ecosystems."""
import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.classification_registry import (
    validate_record_class_registry,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_company_companies_api_ecosystem.global_companies_ecosystem.service import (
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_company_profile,
    list_companies,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.provider_directory import (
    get_platform_provider,
    get_provider_directory_status,
    list_platform_providers,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_platforms_api_ecosystem.service import (
    get_ecosystem_status as get_platform_ecosystem_status,
    get_platform,
    load_platform_registry,
    search_platforms,
)


class CompanyPlatformsRuntimeTests(unittest.TestCase):
    def test_company_classification_registry_is_valid(self):
        result = validate_record_class_registry()
        self.assertTrue(result["structurally_valid"])
        self.assertEqual(
            set(result["record_classes"]),
            {"company", "enterprise", "corporate_group"},
        )
        self.assertFalse(result["freelancer_is_company_record_class"])

    def test_all_company_profile_adapters_are_available(self):
        result = list_companies(limit=100)
        self.assertEqual(result["total"], 26)
        self.assertEqual(len(result["items"]), 26)
        self.assertFalse(result["live_connections"])
        self.assertTrue(all(item["record_type"] == "company" for item in result["items"]))

    def test_company_adapter_search_and_source_status(self):
        result = list_companies(query="open", limit=10)
        self.assertGreaterEqual(result["total"], 1)
        self.assertTrue(any(item["company_id"] == "openai" for item in result["items"]))
        profile = get_company_profile("openai")
        adapter_status = get_company_adapter_status("openai")
        ecosystem_status = get_company_ecosystem_status()
        self.assertEqual(profile["profile_status"], "source_registered_unverified")
        self.assertTrue(profile["sources"])
        self.assertFalse(adapter_status["live_connection"])
        self.assertEqual(ecosystem_status["adapter_count"], 26)
        self.assertEqual(ecosystem_status["live_connections"], 0)

    def test_platform_registry_contains_bharat_global_and_adult_entries(self):
        records = load_platform_registry()
        self.assertEqual(len(records), 76)
        self.assertEqual(sum(1 for item in records if item["country_codes"] == ["IN"]), 28)
        self.assertEqual(sum(1 for item in records if item["adult_only"]), 14)
        self.assertTrue(all(item["verification_status"] == "unverified" for item in records))

    def test_platform_search_filters_bharat_and_adult_records(self):
        bharat = search_platforms(country="IN")
        self.assertEqual(bharat["total"], 28)
        self.assertTrue(all("IN" in item["country_codes"] for item in bharat["items"]))
        adult_default = search_platforms(domain="adult_industry")
        adult_explicit = search_platforms(domain="adult_industry", include_adult=True)
        self.assertEqual(adult_default["total"], 0)
        self.assertEqual(adult_explicit["total"], 14)

    def test_adult_platform_profiles_require_explicit_inclusion(self):
        self.assertIsNone(get_platform("onlyfans"))
        profile = get_platform("onlyfans", include_adult=True)
        self.assertIsNotNone(profile)
        self.assertTrue(profile["adult_only"])
        self.assertGreaterEqual(profile["minimum_age"], 18)

    def test_platform_provider_packages_are_discoverable(self):
        default = list_platform_providers()
        expanded = list_platform_providers(include_adult=True)
        status = get_provider_directory_status()
        self.assertEqual(len(default), 4)
        self.assertEqual(len(expanded), 18)
        self.assertEqual(status["adult_provider_count"], 14)
        self.assertEqual(status["live_connections"], 0)
        self.assertIsNone(get_platform_provider("onlyfans"))
        self.assertEqual(
            get_platform_provider("onlyfans", include_adult=True)["minimum_age"],
            18,
        )

    def test_platform_ecosystem_status_reports_registry(self):
        status = get_platform_ecosystem_status()
        self.assertEqual(status["profile_count"], 76)
        self.assertEqual(status["status"], "ready_with_records")
        self.assertFalse(status["live_external_connections"])

    def test_company_and_platform_routes_are_mounted_in_global_api_router(self):
        from fastapi import FastAPI
        from backend.api.global_api_ecosystem_routes import router

        test_app = FastAPI()
        test_app.include_router(router)
        paths = set(test_app.openapi()["paths"])
        self.assertIn(
            "/api/v1/global-api-ecosystem/global/company-profile-adapters",
            paths,
        )
        self.assertIn(
            "/api/v1/global-api-ecosystem/global/companies",
            paths,
        )
        self.assertIn(
            "/api/v1/global-api-ecosystem/global/platforms/directory",
            paths,
        )
        self.assertIn(
            "/api/v1/global-api-ecosystem/global/platforms/providers",
            paths,
        )


if __name__ == "__main__":
    unittest.main()
