import unittest
from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.domain_catalog import validate_domains
class ExpandedCoreCoverageTests(unittest.TestCase):
 def test_expanded_taxonomy_has_unique_ids(self): self.assertTrue(validate_domains()["valid"])
 def test_expanded_domain_coverage(self):
  m=get_manager()
  for key in ("business_ownership","business_governance","business_finance","accounting_bookkeeping","cash_flow_working_capital","human_resources_people","sales_business_development","ecommerce_marketplaces","export_import_trade","manufacturing_industrial_enterprise","healthcare_enterprise","education_training_enterprise","real_estate_construction_enterprise","energy_environment_enterprise","technology_software_enterprise","sustainability_esg","mergers_acquisitions","business_valuation_exit","business_education_capacity","automation_process_digitalization","business_dispute_resolution"):
   self.assertIsNotNone(m.get_domain(key),key)
 def test_catalog_count_tracks_domain_inventory(self):
  m=get_manager(); self.assertEqual(m.catalog()["domain_count"],len(m.list_domains()))

 def test_bharat_and_global_world_views_cover_every_domain(self):
  from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.domain_catalog import list_scoped_domains
  from backend.core.global_ecosystem.global_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_core_ecosystem.domain_catalog import list_domains
  scoped=list_scoped_domains(); self.assertEqual(len(scoped),len(list_domains())*2)
  self.assertEqual({x["scope_id"] for x in scoped},{"bharat","global_world"})
  self.assertIsNotNone(next((x for x in scoped if x["scoped_domain_id"]=="bharat_msme"),None))
  self.assertIsNotNone(next((x for x in scoped if x["scoped_domain_id"]=="global_world_sme"),None))
