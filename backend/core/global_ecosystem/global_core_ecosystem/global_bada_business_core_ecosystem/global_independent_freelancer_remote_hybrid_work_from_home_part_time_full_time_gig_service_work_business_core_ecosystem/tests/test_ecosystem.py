import unittest
from ..domain_catalog import list_domains,get_domain,search_domains
from ..manager import get_manager
from ..policy import is_allowed
class IndependentWorkTests(unittest.TestCase):
 def test_unique_ids(self):
  ids=[x["domain_id"] for x in list_domains()]; self.assertEqual(len(ids),len(set(ids)))
 def test_categories_registered(self):
  for key in ["ai_automation","app_development","bookkeeping_accounting","business_consulting","coaching_training","creative_commissions","data_analysis","delivery_gig_work","digital_marketing","driving_transport_gigs","graphic_design","home_service_gigs","jobs_careers_employment_core_ecosystem","legal_consulting","microtasks","photography","professional_contracting","seo","social_media_management","software_engineering","translation_localization","tutoring","video_audio_production","virtual_assistance","web_development","writing_editing"]: self.assertIsNotNone(get_domain(key))
 def test_remote_and_gig_search(self): self.assertTrue(search_domains("remote")); self.assertTrue(search_domains("gig"))
 def test_manager(self): self.assertEqual(get_manager().status()["status"],"HEALTHY")
 def test_payments_restricted(self): self.assertFalse(is_allowed("PROCESS_PAYMENTS"))
if __name__=="__main__": unittest.main()
