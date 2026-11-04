import unittest

from fastapi import FastAPI

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_capabilities.registry import (
    BUSINESS_LIFECYCLE_STAGES,
    get_analytics_contract,
    get_compliance_framework,
    validate_capability_registry,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.business_capabilities.routes import connected_module_inventory, router
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.routes import router as ecosystem_router


class BadaBusinessCapabilitiesTests(unittest.TestCase):
    def test_business_lifecycle_covers_idea_to_closure(self):
        stages = BUSINESS_LIFECYCLE_STAGES
        self.assertEqual(stages[0]["id"], "idea")
        self.assertEqual(stages[-1]["id"], "closure")
        self.assertEqual([stage["sequence"] for stage in stages], list(range(1, len(stages) + 1)))

    def test_compliance_framework_does_not_claim_unverified_legal_coverage(self):
        framework = get_compliance_framework()
        self.assertEqual(framework["coverage_claim"], "none")
        self.assertEqual(framework["jurisdiction_records"], [])
        self.assertFalse("verified" in framework["framework_status"] and framework["jurisdiction_records"])

    def test_business_intelligence_is_a_contract_not_fake_live_metrics(self):
        analytics = get_analytics_contract()
        self.assertEqual(analytics["analytics_status"], "event_contract_only_no_live_metrics_store")
        self.assertIn("api_usage", {item["id"] for item in analytics["capabilities"]})
        self.assertIn("other ecosystems own their analytics", analytics["ownership"])

    def test_capability_registry_integrity(self):
        result = validate_capability_registry()
        self.assertTrue(result["valid"], result)
        self.assertFalse(result["live_verification_enabled"])
        self.assertFalse(result["legal_datasets_verified"])
        self.assertFalse(result["analytics_store_enabled"])

    def test_capability_routes_are_mounted_in_the_main_ecosystem(self):
        app = FastAPI()
        app.include_router(ecosystem_router)
        paths = set(app.openapi()["paths"])
        self.assertIn("/api/v1/global-ecosystem/business/capabilities/lifecycle", paths)
        self.assertIn("/api/v1/global-ecosystem/business/capabilities/architecture/modules", paths)

    def test_connected_module_inventory_reads_the_live_router(self):
        result = connected_module_inventory()
        self.assertTrue(result["success"])
        self.assertGreater(result["endpoint_count"], 0)
        module_ids = {item["id"] for item in result["modules"]}
        self.assertIn("integrations", module_ids)
        self.assertIn("industries", module_ids)
        self.assertIn("industries/agriculture-food-natural-resources", module_ids)
        self.assertIn("industries/education-learning-training", module_ids)
        self.assertIn("capabilities", module_ids)
        self.assertIn("governance", module_ids)
        self.assertEqual(result["ai_automation_in_scope"], False)

    def test_capability_routes_are_registered(self):
        app = FastAPI()
        app.include_router(router)
        paths = set(app.openapi()["paths"])
        self.assertIn("/capabilities/lifecycle", paths)
        self.assertIn("/capabilities/trust-safety", paths)
        self.assertIn("/capabilities/compliance/framework", paths)
        self.assertIn("/capabilities/business-intelligence", paths)
        self.assertIn("/capabilities/architecture/modules", paths)


if __name__ == "__main__":
    unittest.main()
