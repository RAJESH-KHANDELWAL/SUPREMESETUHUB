import unittest
from personal_lifestyle_wellness.service import PersonalWellnessService
class PersonalWellnessServiceTests(unittest.TestCase):
 def setUp(self): self.service=PersonalWellnessService()
 def test_category_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known_category(self): self.assertIsNotNone(self.service.get_category("personal_care"))
 def test_unknown_category(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
