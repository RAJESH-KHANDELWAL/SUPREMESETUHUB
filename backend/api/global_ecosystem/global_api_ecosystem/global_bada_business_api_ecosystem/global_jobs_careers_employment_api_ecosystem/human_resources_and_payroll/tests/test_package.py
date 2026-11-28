import unittest
from ..categories import CATEGORY_ID, get_category_definition, validate_category_definition
from ..catalog import get_category, serialize_category
from ..services import get_category_resource, get_category_status, list_subcategory_resources


class IndustryCategoryPackageTests(unittest.TestCase):
    def test_category_is_bound_to_canonical_domain_catalogue(self):
        item = get_category_definition()
        self.assertEqual(item["id"], CATEGORY_ID)
        self.assertTrue(item["name"])
        self.assertTrue(item["subcategories"])

    def test_catalogue_and_service_contracts(self):
        record, payload = get_category(), serialize_category()
        resource, status = get_category_resource(), get_category_status()
        self.assertEqual(record.id, CATEGORY_ID)
        self.assertEqual(payload["id"], CATEGORY_ID)
        self.assertEqual(resource["category"]["id"], CATEGORY_ID)
        self.assertTrue(status["success"])
        self.assertFalse(resource["live_provider_data"])

    def test_subcategory_ids_are_unique_and_individually_listed(self):
        definitions = get_category_definition()["subcategories"]
        resources = list_subcategory_resources()
        self.assertEqual(len(definitions), len(set(definitions)))
        self.assertEqual({item["id"] for item in resources}, set(definitions))
        self.assertTrue(validate_category_definition()["structurally_valid"])


if __name__ == "__main__":
    unittest.main()
