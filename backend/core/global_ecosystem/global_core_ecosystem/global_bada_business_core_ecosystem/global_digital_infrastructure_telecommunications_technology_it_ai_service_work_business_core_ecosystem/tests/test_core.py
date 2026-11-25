import unittest
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_digital_infrastructure_telecommunications_technology_it_ai_service_work_business_core_ecosystem.catalog import ECOSYSTEM_ID, get_catalog
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_digital_infrastructure_telecommunications_technology_it_ai_service_work_business_core_ecosystem.contracts import TechnologyBusinessContext, ServiceWorkEngagement
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_digital_infrastructure_telecommunications_technology_it_ai_service_work_business_core_ecosystem.domain_catalog import list_domains
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_digital_infrastructure_telecommunications_technology_it_ai_service_work_business_core_ecosystem.manager import get_manager
class DigitalTechnologyCoreTests(unittest.TestCase):
    def test_identity_and_2468_reference(self):
        self.assertEqual(get_catalog()["ecosystem_id"],ECOSYSTEM_ID)
        self.assertEqual(get_catalog()["master_catalog"]["target_unique_entries"],2468)
    def test_unique_domains_cover_service_and_work(self):
        ids=[x["domain_id"] for x in list_domains()]
        self.assertEqual(len(ids),len(set(ids)))
        self.assertIn("PROFESSIONAL_TECHNICAL_WORK",ids)
        self.assertIn("BUSINESS_OPERATIONS_COMMERCIAL_SERVICES",ids)
    def test_context_requires_tenant_and_actor(self):
        get_manager().validate_context(TechnologyBusinessContext("tenant","actor","IN"))
        with self.assertRaises(ValueError): TechnologyBusinessContext("","actor","IN").validate()
    def test_draft_work_validates_without_execution(self):
        item=ServiceWorkEngagement("r1","SOFTWARE_APPLICATION_ENGINEERING","WEB_DEVELOPMENT","Website build","IN")
        result=get_manager().validate_engagement(item)
        self.assertTrue(result["success"])
        self.assertFalse(result["record_persisted"])
        self.assertFalse(result["work_executed"])
    def test_active_work_requires_evidence_and_approval(self):
        item=ServiceWorkEngagement("r2","CLOUD_HOSTING_DATA_CENTRES","CLOUD_MIGRATION","Migration","IN",lifecycle_status="ACTIVE")
        result=get_manager().validate_engagement(item)
        self.assertFalse(result["success"])
        self.assertIn("APPROVAL_REFERENCE_REQUIRED",result["errors"])
        self.assertIn("APPROVAL_REQUIRES_EVIDENCE_REFERENCES",result["errors"])
    def test_provider_registry_is_metadata_only(self):
        ids={x["provider_id"] for x in get_manager().list_providers()}
        self.assertEqual(ids,{"APPLE","AWS","GOOGLE","IBM","MICROSOFT","ORACLE"})
        self.assertIsNone(get_manager().get_provider("UNKNOWN"))
    def test_unknown_domain_is_rejected(self):
        self.assertFalse(get_manager().classify_service("UNKNOWN","consulting")["success"])
    def test_master_catalog_is_read_only(self):
        ref=get_manager().master_catalog_reference()
        self.assertEqual(ref["access_mode"],"READ_ONLY_ON_DEMAND")
        self.assertEqual(ref["target_unique_entries"],2468)
if __name__ == "__main__": unittest.main()
