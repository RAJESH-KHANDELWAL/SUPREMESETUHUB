import unittest
from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.domain_catalog import validate_domains
class CoreTests(unittest.TestCase):
 def test_unique_domains(self): self.assertTrue(validate_domains()["valid"])
 def test_all_requested_segments(self):
  m=get_manager()
  for k in ("msme","sme","startups","solo_preneur","solo_preneurship","business_men","business_women","women_preneur","women_preneurship","men_preneur","men_preneurship","entrepreneurs","entrepreneurship","entrepreneurial_research","innovation"): self.assertIsNotNone(m.get_domain(k),k)
 def test_gender_terms_do_not_restrict_access(self): self.assertTrue(get_manager().policy()["inclusive_access"])
 def test_master_catalog_reference_is_read_only(self): self.assertEqual(get_manager().master_catalog_reference()["access_mode"],"READ_ONLY_ON_DEMAND")
