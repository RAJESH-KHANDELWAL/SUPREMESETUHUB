"""Offline tests for explainable Global Business Ecosystem intelligence."""
import unittest
from types import SimpleNamespace

from backend.businesses.global_ecosystem.global_business_ecosystem.intelligence import BusinessIntelligence
from backend.businesses.global_ecosystem.global_business_ecosystem.providers import ProviderRegistry
from backend.businesses.global_ecosystem.global_business_ecosystem.recommendations import BusinessActionPlanner


class BusinessIntelligenceTests(unittest.TestCase):
    def setUp(self):
        self.engine = BusinessIntelligence()

    def test_complete_profile_has_high_completeness(self):
        profile = SimpleNamespace(
            business_id="B-1", name="Acme", legal_name="Acme Pvt Ltd",
            category="Manufacturing", industry="Manufacturing",
            business_type="SMALL_BUSINESS", location="Jaipur",
            headquarters="Jaipur", website="https://example.test",
            public_contact="hello@example.test", employee_count=8,
            annual_revenue_band="UNDER_1_CR", operating_regions=["IN"],
            departments=["sales", "operations"], tags=["b2b"],
            compliance_status="COMPLIANT", verified=True,
        )
        result = self.engine.assess(profile)
        self.assertEqual(result.profile_completeness, 100)
        self.assertEqual(result.maturity_band, "WELL_DOCUMENTED")

    def test_missing_fields_are_explained(self):
        result = self.engine.assess({"business_id": "B-2", "name": "New business"})
        codes = {signal.code for signal in result.signals}
        self.assertIn("MISSING_INDUSTRY", codes)
        self.assertIn("COMPLIANCE_EVIDENCE_INCOMPLETE", codes)
        self.assertEqual(result.generated_by, "SUPREMESETUHUB_RULE_ENGINE")
        self.assertFalse(result.external_verification)

    def test_non_compliance_creates_critical_signal(self):
        result = self.engine.assess({
            "business_id": "B-3", "name": "Test", "industry": "Retail",
            "business_type": "SMALL_BUSINESS", "location": "India",
            "compliance_status": "NON_COMPLIANT",
        })
        self.assertIn("CRITICAL", {signal.level for signal in result.signals})

    def test_action_plan_is_prioritized(self):
        result = self.engine.assess({"business_id": "B-4", "name": "Test"})
        plan = BusinessActionPlanner().build(result)
        self.assertEqual(plan["business_id"], "B-4")
        self.assertGreater(len(plan["tasks"]), 0)

    def test_unknown_provider_is_not_falsely_available(self):
        registry = ProviderRegistry()
        self.assertEqual(registry.capabilities(), [])
        with self.assertRaises(LookupError):
            registry.analyze("not-configured", task="summary", business_context={})

    def test_missing_business_id_is_rejected(self):
        with self.assertRaises(ValueError):
            self.engine.assess({"name": "No ID"})


if __name__ == "__main__":
    unittest.main()
