import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_business_governance_compliance_standards_api_ecosystem.governance.registry import (
    APPROVED_REQUIREMENTS,
    APPROVED_SCOPE_CONSTRAINTS,
    list_approved_requirements,
    list_scope_constraints,
    validate_approved_requirements,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.global_business_governance_compliance_standards_api_ecosystem.governance.routes import router


class BadaBusinessApprovedRequirementsTests(unittest.TestCase):
    def test_only_explicitly_confirmed_questions_are_recorded(self):
        ids = {item["id"] for item in APPROVED_REQUIREMENTS}
        expected = {"Q10", "Q11", "Q12", "Q14", "Q21"} | {f"Q{i:02d}" for i in range(22, 36)}
        self.assertEqual(ids, expected)
        self.assertNotIn("Q08", ids)
        self.assertNotIn("Q09", ids)
        self.assertNotIn("Q13", ids)
        self.assertNotIn("Q15", ids)
        self.assertTrue(all(item["decision"] == "YES" for item in APPROVED_REQUIREMENTS))

    def test_scope_constraints_preserve_folder_ownership(self):
        ids = {item["id"] for item in APPROVED_SCOPE_CONSTRAINTS}
        self.assertEqual(len(ids), len(APPROVED_SCOPE_CONSTRAINTS))
        self.assertIn("SCOPE-API-ONLY", ids)
        self.assertIn("SCOPE-NO-AI-HERE", ids)
        self.assertIn("SCOPE-EDUCATION-IN-BADA", ids)
        self.assertIn("SCOPE-FINANCE-EXTERNAL", ids)
        self.assertIn("SCOPE-FOUR-ECOSYSTEM-BOUNDARIES", ids)
        self.assertIn("SCOPE-BUSINESS-ANALYTICS", ids)

    def test_registry_integrity(self):
        result = validate_approved_requirements()
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["count"], len(APPROVED_REQUIREMENTS))

    def test_registry_returns_defensive_copies(self):
        records = list_approved_requirements()
        records[0]["title"] = "mutated"
        self.assertNotEqual(records[0]["title"], list_approved_requirements()[0]["title"])
        constraints = list_scope_constraints()
        constraints[0]["decision"] = "mutated"
        self.assertNotEqual(constraints[0]["decision"], list_scope_constraints()[0]["decision"])

    def test_governance_routes_are_registered(self):
        paths = {route.path for route in router.routes}
        self.assertIn("/governance/approved-requirements", paths)
        self.assertIn("/governance/requirements/integrity", paths)
        self.assertIn("/governance/scope-constraints", paths)


if __name__ == "__main__":
    unittest.main()
