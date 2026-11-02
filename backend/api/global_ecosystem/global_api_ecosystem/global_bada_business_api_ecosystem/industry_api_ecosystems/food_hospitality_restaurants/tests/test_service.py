import unittest
from food_hospitality_restaurants.service import FoodHospitalityService
class FoodHospitalityServiceTests(unittest.TestCase):
 def setUp(self): self.service=FoodHospitalityService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("restaurants_dining"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
