"""Offline tests for intelligence integrated with the Big Businesses domain."""
import unittest
from types import SimpleNamespace

from backend.businesses.intelligence import BusinessIntelligence
from backend.businesses.intelligence_service import BigBusinessIntelligenceService
from backend.businesses.recommendations import BusinessActionPlanner


class FakeController:
    def __init__(self, records):
        self.records = records

    def get(self, business_id):
        return self.records.get(business_id)


class BigBusinessIntelligenceTests(unittest.TestCase):
    def test_complete_profile_has_full_completeness(self):
        profile = SimpleNamespace(
            business_id="BB-1", name="Acme", legal_name="Acme Pvt Ltd",
            category="Manufacturing", industry="Manufacturing",
            business_type="ENTERPRISE", location="Jaipur",
            headquarters="Jaipur", website="https://example.test",
            public_contact="hello@example.test", employee_count=800,
            annual_revenue_band="ABOVE_100_CR", operating_regions=["IN"],
            departments=["sales", "operations"], tags=["b2b"],
            compliance_status="COMPLIANT", verified=True,
        )
        result = BusinessIntelligence().assess(profile)
        self.assertEqual(result.profile_completeness, 100)
        self.assertEqual(result.maturity_band, "WELL_DOCUMENTED")

    def test_missing_fields_are_explained(self):
        result = BusinessIntelligence().assess({
            "business_id": "BB-2", "name": "New business",
            "business_type": "LARGE_BUSINESS",
        })
        codes = {signal.code for signal in result.signals}
        self.assertIn("MISSING_INDUSTRY", codes)
        self.assertIn("COMPLIANCE_EVIDENCE_INCOMPLETE", codes)
        self.assertFalse(result.external_verification)

    def test_declared_non_compliance_creates_critical_signal(self):
        result = BusinessIntelligence().assess({
            "business_id": "BB-3", "name": "Test", "industry": "Retail",
            "business_type": "ENTERPRISE", "location": "India",
            "compliance_status": "NON_COMPLIANT",
        })
        self.assertIn("CRITICAL", {signal.level for signal in result.signals})

    def test_action_plan_is_prioritized(self):
        result = BusinessIntelligence().assess({
            "business_id": "BB-4", "name": "Test",
        })
        plan = BusinessActionPlanner().build(result)
        self.assertEqual(plan["business_id"], "BB-4")
        self.assertGreater(len(plan["tasks"]), 0)

    def test_service_only_assesses_large_business_types(self):
        records = {
            "BB-5": SimpleNamespace(
                business_id="BB-5", business_type="ENTERPRISE",
                name="Enterprise", industry="IT", location="India",
            ),
            "SM-1": SimpleNamespace(
                business_id="SM-1", business_type="SMALL_BUSINESS",
                name="Small", industry="Retail", location="India",
            ),
        }
        service = BigBusinessIntelligenceService(controller=FakeController(records))
        self.assertEqual(service.assess("BB-5").business_id, "BB-5")
        with self.assertRaises(LookupError):
            service.assess("SM-1")

    def test_compare_rejects_duplicate_ids(self):
        records = {
            "BB-6": SimpleNamespace(
                business_id="BB-6", business_type="LARGE_BUSINESS",
                name="Large", industry="IT", location="India",
            )
        }
        service = BigBusinessIntelligenceService(controller=FakeController(records))
        with self.assertRaises(ValueError):
            service.compare(["BB-6", "BB-6"])

    def test_missing_business_id_is_rejected(self):
        with self.assertRaises(ValueError):
            BusinessIntelligence().assess({"name": "No ID"})


if __name__ == "__main__":
    unittest.main()
