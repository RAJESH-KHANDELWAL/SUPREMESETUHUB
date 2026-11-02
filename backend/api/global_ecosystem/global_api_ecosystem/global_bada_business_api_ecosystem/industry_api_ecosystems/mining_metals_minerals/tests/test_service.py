import unittest
from mining_metals_minerals.service import MiningMetalsService
class MiningMetalsServiceTests(unittest.TestCase):
 def setUp(self): self.service=MiningMetalsService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("metal_mining"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
