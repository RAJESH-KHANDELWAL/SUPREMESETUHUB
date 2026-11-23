import unittest
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_service_work_business_core_ecosystem.manager import get_manager
class ExpandedBusinessCoverageTests(unittest.TestCase):
 def test_every_expanded_service_maps(self): self.assertTrue(get_manager().validate_mappings()["valid"])
 def test_expanded_service_categories(self):
  m=get_manager()
  for key in ("business_ownership_services","business_governance_services","business_finance_services","accounting_bookkeeping_services","human_resources_people_services","sales_business_development_services","ecommerce_marketplaces_services","export_import_trade_services","manufacturing_industrial_enterprise_services","healthcare_enterprise_services","education_training_enterprise_services","real_estate_construction_enterprise_services","energy_environment_enterprise_services","technology_software_enterprise_services","sustainability_esg_services","mergers_acquisitions_services","business_valuation_exit_services","automation_process_digitalization_services","business_dispute_resolution_services"):
   self.assertIsNotNone(m.get_service(key),key)
 def test_classification_requires_verification(self):
  item=get_manager().classify_service("business_finance_services")
  self.assertTrue(item["verification_required"]); self.assertEqual(item["execution_status"],"not_executed")

 def test_bharat_and_global_world_views_cover_every_service(self):
  from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_msme_sme_startup_solo_preneur_solo_preneurship_business_men_business_women_women_preneur_women_preneurship_men_preneur_men_preneurship_entrepreneur_entrepreneurship_research_innovation_service_work_business_core_ecosystem.service_catalog import list_scoped_services, list_services
  scoped=list_scoped_services(); self.assertEqual(len(scoped),len(list_services())*2)
  self.assertEqual({x["scope_id"] for x in scoped},{"bharat","global_world"})
  self.assertIsNotNone(next((x for x in scoped if x["scoped_service_id"]=="bharat_msme_development"),None))
  self.assertIsNotNone(next((x for x in scoped if x["scoped_service_id"]=="global_world_sme_growth_advisory"),None))
