import unittest
from digital_infrastructure_telecommunications.service import DigitalInfrastructureService
class DigitalInfrastructureServiceTests(unittest.TestCase):
    def setUp(self): self.service = DigitalInfrastructureService()
    def test_count(self): self.assertEqual(len(self.service.list_categories()), 12)
    def test_known(self): self.assertIsNotNone(self.service.get_category("telecom_networks"))
    def test_unknown(self): self.assertIsNone(self.service.get_category("unknown"))
if __name__ == "__main__": unittest.main()
