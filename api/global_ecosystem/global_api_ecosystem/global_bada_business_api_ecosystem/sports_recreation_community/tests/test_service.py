import unittest
from sports_recreation_community.service import SportsCommunityService
class SportsCommunityServiceTests(unittest.TestCase):
 def setUp(self): self.service=SportsCommunityService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("professional_sports"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
