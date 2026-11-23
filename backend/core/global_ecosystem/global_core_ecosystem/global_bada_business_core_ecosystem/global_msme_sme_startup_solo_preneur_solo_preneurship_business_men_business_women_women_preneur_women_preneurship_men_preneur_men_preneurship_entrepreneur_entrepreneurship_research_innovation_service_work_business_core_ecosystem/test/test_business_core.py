import unittest
from ..manager import get_manager
class BusinessTests(unittest.TestCase):
 def test_all_services_map_to_canonical_domains(self): self.assertTrue(get_manager().validate_mappings()["valid"])
 def test_service_segments(self):
  m=get_manager()
  for k in ("msme_development","sme_growth_advisory","startup_formation","solo_business_setup","business_men_networking","business_women_networking","women_led_business_advisory","men_led_business_advisory","market_customer_research","innovation_consulting"): self.assertIsNotNone(m.get_service(k),k)
 def test_classification_does_not_claim_execution(self): self.assertEqual(get_manager().classify_service("msme_development")["execution_status"],"not_executed")
