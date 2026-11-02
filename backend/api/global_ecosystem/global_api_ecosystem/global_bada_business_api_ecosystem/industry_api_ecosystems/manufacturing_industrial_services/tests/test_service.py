"""Unit tests for manufacturing_industrial_services taxonomy service."""
import unittest
from manufacturing_industrial_services.service import ManufacturingService

class ManufacturingServiceTests(unittest.TestCase):
    def setUp(self): self.service = ManufacturingService()
    def test_catalog_and_unique_ids(self):
        items = self.service.list_categories()
        self.assertGreaterEqual(len(items), 10)
        self.assertEqual(len({item["id"] for item in items}), len(items))
    def test_search_and_detail(self):
        first = self.service.list_categories()[0]
        self.assertTrue(self.service.list_categories(query=first["id"]))
        self.assertEqual(self.service.get_category(first["id"])["id"], first["id"])
        self.assertIsNone(self.service.get_category("not_a_real_category"))
    def test_status(self):
        self.assertEqual(self.service.get_status()["status"], "taxonomy_scaffold")

if __name__ == "__main__": unittest.main()
