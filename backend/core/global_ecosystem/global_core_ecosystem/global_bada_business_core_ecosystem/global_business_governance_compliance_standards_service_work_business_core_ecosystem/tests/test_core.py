from __future__ import annotations
import unittest
from ..catalog import ECOSYSTEM_ID, get_catalog
from ..contracts import BusinessContext, ServiceWorkBusinessRecord
from ..domain_catalog import list_domains
from ..manager import get_manager
from ..policy import validate_record_policy

class BusinessGovernanceCoreTests(unittest.TestCase):
    def test_catalog_identity_and_master_target(self):
        catalog = get_catalog()
        self.assertEqual(catalog["ecosystem_id"], ECOSYSTEM_ID)
        self.assertEqual(catalog["parent_id"], "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM")
        self.assertEqual(catalog["master_catalog"]["target_unique_entries"], 2468)
    def test_unique_domains_include_service_and_work(self):
        domains = list_domains()
        ids = [item["domain_id"] for item in domains]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertIn("BUSINESS_SERVICES_AND_OPERATIONS", ids)
        self.assertIn("PROFESSIONAL_WORK_AND_ENGAGEMENTS", ids)
    def test_context_requires_identity_and_jurisdiction(self):
        BusinessContext("tenant-1", "actor-1", "IN").validate()
        with self.assertRaises(ValueError):
            BusinessContext("", "actor-1", "IN").validate()
    def test_active_compliance_requires_evidence_and_source(self):
        record = ServiceWorkBusinessRecord("r-1","BUSINESS_COMPLIANCE","COMPLIANCE_SERVICE","Regulatory review","IN",lifecycle_status="ACTIVE")
        errors = validate_record_policy(record)
        self.assertIn("APPROVAL_REQUIRES_EVIDENCE_REFERENCES", errors)
        self.assertIn("REGULATED_OR_PUBLIC_DOMAIN_REQUIRES_SOURCE_REFERENCES", errors)
    def test_draft_work_record_is_validation_only(self):
        record = ServiceWorkBusinessRecord("w-1","PROFESSIONAL_WORK_AND_ENGAGEMENTS","ENGAGEMENT","Process mapping","IN")
        result = get_manager().validate_record(record)
        self.assertTrue(result["success"])
        self.assertFalse(result["record_persisted"])
        self.assertFalse(result["work_executed"])
    def test_master_catalog_reference_is_read_only(self):
        ref = get_manager().master_catalog_reference()
        self.assertEqual(ref["target_unique_entries"], 2468)
        self.assertEqual(ref["access_mode"], "READ_ONLY_ON_DEMAND")
        self.assertEqual(ref["source_path"], "backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
    def test_live_connection_is_not_claimed(self):
        self.assertFalse(get_manager().status()["live_connection_verified"])

if __name__ == "__main__":
    unittest.main()
