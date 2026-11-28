import unittest
from security_defence_safety_services.service import SecurityDefenceService
class SecurityDefenceServiceTests(unittest.TestCase):
 def setUp(self): self.service=SecurityDefenceService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("physical_security"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
