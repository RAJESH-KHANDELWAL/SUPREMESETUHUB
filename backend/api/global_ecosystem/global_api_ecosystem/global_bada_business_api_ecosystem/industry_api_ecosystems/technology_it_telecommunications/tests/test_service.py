"""Unit tests for technology_it_telecommunications taxonomy service."""
import unittest
from technology_it_telecommunications.service import TechnologyService

class TechnologyServiceTests(unittest.TestCase):
    def setUp(self): self.service = TechnologyService()
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
