import unittest
from automotive_mobility.service import AutomotiveMobilityService
class AutomotiveMobilityServiceTests(unittest.TestCase):
 def setUp(self): self.service=AutomotiveMobilityService()
 def test_category_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known_category(self): self.assertIsNotNone(self.service.get_category("passenger_vehicles"))
 def test_unknown_category(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
