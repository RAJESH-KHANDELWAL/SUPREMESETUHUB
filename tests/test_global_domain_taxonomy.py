import unittest

from backend.global_ecosystem.domain_taxonomy import (
    DOMAIN_TAXONOMY,
    get_domain,
    get_domain_by_name,
    get_domain_catalog,
    list_domains,
    search_domains,
    validate_domain_taxonomy,
)


class GlobalDomainTaxonomyTests(unittest.TestCase):
    def test_catalog_contains_29_unique_domain_definitions(self):
        self.assertEqual(len(DOMAIN_TAXONOMY), 29)
        ids = [item["id"] for item in DOMAIN_TAXONOMY]
        self.assertEqual(len(ids), len(set(ids)))

    def test_lookup_by_id_is_case_and_whitespace_insensitive(self):
        self.assertEqual(
            get_domain("  GLOBAL_FINANCE_ECOSYSTEM ")["name"],
            "Finance & Fintech",
        )
        self.assertIsNone(get_domain("not_a_real_domain"))

    def test_lookup_by_display_name(self):
        self.assertEqual(
            get_domain_by_name(" education & knowledge ")["id"],
            "global_education_ecosystem",
        )
        self.assertIsNone(get_domain_by_name("unknown"))

    def test_search_checks_id_name_and_description(self):
        self.assertEqual(search_domains("quantum")[0]["id"], "global_quantum_computing_ecosystem")
        self.assertEqual(search_domains("water-quality")[0]["id"], "global_water_ecosystem")
        self.assertEqual(search_domains("   "), [])

    def test_returned_records_do_not_mutate_source_catalogue(self):
        result = list_domains()
        result[0]["name"] = "tampered"
        self.assertEqual(get_domain("global_education_ecosystem")["name"], "Education & Knowledge")

    def test_catalog_marks_records_as_taxonomy_only(self):
        result = get_domain_catalog()
        self.assertEqual(result["registry_status"], "taxonomy_only")
        self.assertEqual(result["count"], 29)
        self.assertIn("bharat_india", result["geographic_scopes"])

    def test_integrity_validation_passes(self):
        result = validate_domain_taxonomy()
        self.assertTrue(result["structurally_valid"], result["issues"])
        self.assertTrue(all(result["checks"].values()))


if __name__ == "__main__":
    unittest.main()
