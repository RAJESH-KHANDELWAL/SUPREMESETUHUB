import unittest
from fashion_textiles_apparel.service import FashionTextilesService
class FashionTextilesServiceTests(unittest.TestCase):
 def setUp(self): self.service=FashionTextilesService()
 def test_count(self): self.assertEqual(len(self.service.list_categories()),12)
 def test_known(self): self.assertIsNotNone(self.service.get_category("textile_fibres"))
 def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__=="__main__": unittest.main()
