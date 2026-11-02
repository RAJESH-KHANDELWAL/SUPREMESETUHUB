import unittest
from science_research_innovation.service import ScienceResearchService
class ScienceResearchServiceTests(unittest.TestCase):
 def setUp(self): self.service=ScienceResearchService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("scientific_research"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
