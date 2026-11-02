import unittest
from supply_chain_warehousing_distribution.service import SupplyChainDistributionService
class SupplyChainDistributionServiceTests(unittest.TestCase):
 def setUp(self): self.service = SupplyChainDistributionService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()), 12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("procurement"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__ == "__main__": unittest.main()
