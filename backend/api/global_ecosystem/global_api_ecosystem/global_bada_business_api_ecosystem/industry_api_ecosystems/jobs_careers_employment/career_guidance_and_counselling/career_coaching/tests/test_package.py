import unittest
from ..categories import CATEGORY_ID, SUBCATEGORY_ID, get_subcategory_definition, validate_subcategory_definition
from ..catalog import get_subcategory, serialize_subcategory
from ..services import get_subcategory_resource, get_subcategory_status


class IndustrySubcategoryPackageTests(unittest.TestCase):
    def test_subcategory_resolves_from_parent_canonical_catalogue(self):
        item = get_subcategory_definition()
        self.assertEqual(item["id"], SUBCATEGORY_ID)
        self.assertEqual(item["category_id"], CATEGORY_ID)
        self.assertTrue(item["name"])

    def test_catalogue_and_service_contracts(self):
        record, payload = get_subcategory(), serialize_subcategory()
        resource, status = get_subcategory_resource(), get_subcategory_status()
        self.assertEqual(record.id, SUBCATEGORY_ID)
        self.assertEqual(payload["category_id"], CATEGORY_ID)
        self.assertEqual(resource["subcategory"]["id"], SUBCATEGORY_ID)
        self.assertTrue(status["success"])
        self.assertFalse(resource["live_provider_data"])
        self.assertTrue(validate_subcategory_definition()["structurally_valid"])


if __name__ == "__main__":
    unittest.main()
