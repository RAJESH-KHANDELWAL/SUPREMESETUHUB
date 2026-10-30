"""Unit tests for Government, Public Services & Social Impact."""
import unittest
from government_public_services_social_impact.service import PublicImpactService
class PublicImpactServiceTests(unittest.TestCase):
 def setUp(self): self.service=PublicImpactService()
 def test_category_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known_category(self): self.assertIsNotNone(self.service.get_category("government_departments"))
 def test_unknown_category(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
