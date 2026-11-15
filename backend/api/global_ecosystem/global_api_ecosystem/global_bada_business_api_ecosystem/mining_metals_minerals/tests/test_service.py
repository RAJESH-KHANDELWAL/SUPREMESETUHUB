import unittest
from mining_metals_minerals.service import MiningMetalsService

class MiningMetalsServiceTests(unittest.TestCase):
    def setUp(self):
        self.service = MiningMetalsService()

    def test_category_count(self):
        self.assertEqual(len(self.service.list_categories()), 12)

    def test_business_domain_count(self):
        self.assertEqual(len(self.service.list_business_domains()), 20)

    def test_all_business_domains_map_to_categories(self):
        category_ids = {item["id"] for item in self.service.list_categories()}
        self.assertTrue(all(item["category_id"] in category_ids for item in self.service.list_business_domains()))

    def test_known_category(self):
        self.assertIsNotNone(self.service.get_category("metal_mining"))

    def test_known_business_domain(self):
        self.assertIsNotNone(self.service.get_business_domain("iron_ore_mining"))

    def test_unknown_category(self):
        self.assertIsNone(self.service.get_category("unknown"))

    def test_unknown_business_domain(self):
        self.assertIsNone(self.service.get_business_domain("unknown"))

if __name__ == "__main__":
    unittest.main()
