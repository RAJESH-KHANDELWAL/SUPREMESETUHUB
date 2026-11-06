"""Unit tests for the manufacturing and factory-services taxonomy."""
import unittest
from manufacturing_industrial_services.catalog import validate_catalog
from manufacturing_industrial_services.service import ManufacturingService

class ManufacturingServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = ManufacturingService()

    def test_catalog_counts_and_unique_ids(self):
        report = validate_catalog()
        self.assertEqual(report["category_count"], 16)
        self.assertEqual(report["business_domain_count"], 20)
        self.assertTrue(report["structurally_valid"])

    def test_every_domain_maps_to_a_category(self):
        category_ids = {item["id"] for item in self.service.list_categories()}
        self.assertTrue(all(item["category_id"] in category_ids for item in self.service.list_business_domains()))

    def test_category_search_and_detail(self):
        self.assertTrue(self.service.list_categories("factory"))
        first = self.service.list_categories()[0]
        self.assertEqual(self.service.get_category(first["id"])["id"], first["id"])
        self.assertIsNone(self.service.get_category("unknown_category"))

    def test_domain_search_filter_and_detail(self):
        results = self.service.list_business_domains("battery")
        self.assertEqual([item["id"] for item in results], ["ev_battery_component_manufacturing"])
        filtered = self.service.list_business_domains(category_id="industrial_manufacturing")
        self.assertTrue(all(item["category_id"] == "industrial_manufacturing" for item in filtered))
        self.assertIsNotNone(self.service.get_business_domain("contract_manufacturing"))
        self.assertIsNone(self.service.get_business_domain("unknown_domain"))

    def test_status_and_integrity(self):
        status = self.service.get_status()
        self.assertEqual(status["status"], "taxonomy_scaffold")
        self.assertEqual(status["business_domain_count"], 20)
        self.assertTrue(self.service.get_integrity()["structurally_valid"])

if __name__ == "__main__":
    unittest.main()
