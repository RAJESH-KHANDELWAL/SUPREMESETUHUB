import unittest
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_hospitality_hotels_resorts_restaurants_api_ecosystem.service import FoodHospitalityService
class FoodHospitalityServiceTests(unittest.TestCase):
 def setUp(self): self.service=FoodHospitalityService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),11)
 def test_known(self): self.assertIsNotNone(self.service.get_category("restaurants_dining"))
 def test_food_safety_moved(self): self.assertIsNone(self.service.get_category("food_safety_quality"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
