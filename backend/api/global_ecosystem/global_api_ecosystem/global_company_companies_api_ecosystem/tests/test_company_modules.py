"""Tests for the company-specific module index."""
import unittest
from pathlib import Path

from ..company_modules_api_ecosystem.registry import (
    get_company_module,
    list_company_modules,
    search_company_modules,
    validate_company_module_registry,
)
from ..company_modules_api_ecosystem.service import CompanyModulesService


class CompanyModulesRegistryTests(unittest.TestCase):
    def test_registry_has_unique_ids_and_paths(self):
        result = validate_company_module_registry()
        self.assertTrue(result["structurally_valid"])
        self.assertEqual(result["module_count"], 26)
        self.assertEqual(result["duplicate_company_ids"], [])
        self.assertEqual(result["duplicate_package_paths"], [])

    def test_every_registry_entry_points_to_an_existing_package(self):
        package_root = Path(__file__).resolve().parents[1]
        for item in list_company_modules():
            with self.subTest(company_id=item.company_id):
                self.assertTrue((package_root / item.package_path).is_dir())

    def test_lookup_is_case_insensitive(self):
        self.assertEqual(get_company_module("APPLE").company_id, "apple")
        self.assertIsNone(get_company_module("not-a-company-module"))

    def test_search_matches_id_and_name(self):
        self.assertEqual([item.company_id for item in search_company_modules("nvidia")], ["nvidia"])
        self.assertEqual([item.company_id for item in search_company_modules("MICRO")], ["microsoft"])
        self.assertEqual(search_company_modules("   "), [])

    def test_module_index_does_not_claim_profile_data(self):
        service = CompanyModulesService()
        status = service.get_status()
        self.assertEqual(status["catalog_status"], "module_index_only")
        self.assertFalse(status["profile_records_included"])
        self.assertFalse(status["live_company_data_connected"])
        self.assertTrue(all(item.profile_registry_status == "not_connected" for item in list_company_modules()))


if __name__ == "__main__":
    unittest.main()
