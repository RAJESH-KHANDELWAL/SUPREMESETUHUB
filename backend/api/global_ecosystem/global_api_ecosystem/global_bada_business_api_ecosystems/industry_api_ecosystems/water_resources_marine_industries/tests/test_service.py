import unittest
from water_resources_marine_industries.service import WaterMarineService
class WaterMarineServiceTests(unittest.TestCase):
    def setUp(self): self.service = WaterMarineService()
    def test_count(self): self.assertEqual(len(self.service.list_categories()), 12)
    def test_known(self): self.assertIsNotNone(self.service.get_category("water_resources"))
    def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__ == "__main__": unittest.main()
