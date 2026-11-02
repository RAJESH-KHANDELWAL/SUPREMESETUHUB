"""Verify both Work & Careers classification axes and registry counts."""
import unittest
from ..api_ecosystem import get_api_ecosystem, list_registry_categories, list_registry_professional_fields
from ..professional_fields.catalog import validate_professional_fields

class WorkCareersRegistryTests(unittest.TestCase):
    def test_top_level_registry_counts(self):
        result = get_api_ecosystem()
        self.assertEqual(result["employment_context_category_count"], 24)
        self.assertEqual(result["professional_field_count"], 12)
        self.assertEqual(result["professional_subcategory_count"], 81)
        self.assertEqual(result["taxonomy_status"], "taxonomy_only")

    def test_category_ecosystems(self):
        records = list_registry_categories()
        self.assertEqual(len(records), 24)
        self.assertEqual(len({item["category_id"] for item in records}), 24)

    def test_professional_field_ecosystems(self):
        records = list_registry_professional_fields()
        self.assertEqual(len(records), 12)
        self.assertEqual(sum(item["subcategory_count"] for item in records), 81)

    def test_professional_field_integrity(self):
        result = validate_professional_fields()
        self.assertTrue(result["structurally_valid"], result)
        self.assertEqual(result["field_count"], 12)
        self.assertEqual(result["subcategory_count"], 81)

if __name__ == "__main__":
    unittest.main()
