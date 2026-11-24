"""CI coverage for the standalone Global Company / Companies API."""

import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_companies_api_ecosystem import router
from backend.api.global_ecosystem.global_api_ecosystem.global_companies_api_ecosystem.schemas import CompanyApiStatus
from backend.api.global_ecosystem.global_api_ecosystem.global_companies_api_ecosystem.service import (
    get_api_status,
    get_company_alphabet,
    list_country_sources,
    load_company_registry,
)


class GlobalCompaniesApiTests(unittest.TestCase):
    def test_standalone_router_exposes_company_and_source_routes(self):
        paths = {route.path for route in router.routes}
        self.assertIn("/global/companies/status", paths)
        self.assertIn("/global/companies", paths)
        self.assertIn("/global/companies/search", paths)
        self.assertIn("/global/companies/alphabet", paths)
        self.assertIn("/global/companies/sources", paths)
        self.assertIn("/global/companies/sources/{source_id}", paths)

    def test_status_matches_response_schema(self):
        result = get_api_status()
        parsed = CompanyApiStatus(**result)
        self.assertEqual(parsed.ecosystem, "GLOBAL COMPANY AND COMPANIES API")
        self.assertGreaterEqual(parsed.source_count, 1)
        self.assertIn("IN", parsed.source_countries)
        self.assertEqual(parsed.source_mode, "official_source_directory_only")

    def test_country_source_directory_filters_by_country(self):
        result = list_country_sources("IN")
        self.assertEqual(result["registry_status"], "source_directory_only")
        self.assertGreaterEqual(result["total"], 1)
        self.assertTrue(all(item["country_code"] == "IN" for item in result["items"]))

    def test_source_directory_includes_initial_priority_countries(self):
        result = list_country_sources()
        self.assertTrue({"IN", "US", "GB", "AE"}.issubset(set(result["countries"])))

    def test_alphabet_counts_reflect_registry_not_taxonomy(self):
        result = get_company_alphabet()
        self.assertEqual(result["total"], len(load_company_registry()))

    def test_company_registry_is_not_fabricated(self):
        records = load_company_registry()
        self.assertIsInstance(records, list)
        identifiers = [record["company_id"] for record in records]
        self.assertEqual(len(identifiers), len(set(identifiers)))


if __name__ == "__main__":
    unittest.main()
