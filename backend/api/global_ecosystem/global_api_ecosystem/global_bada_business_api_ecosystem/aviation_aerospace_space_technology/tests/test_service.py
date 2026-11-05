import unittest
from aviation_aerospace_space_technology.service import AviationAerospaceService
class AviationAerospaceServiceTests(unittest.TestCase):
 def setUp(self): self.service=AviationAerospaceService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("commercial_aviation"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
