import unittest

from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.governance.registry import (
    APPROVED_REQUIREMENTS,
    list_approved_requirements,
    validate_approved_requirements,
)
from backend.api.global_ecosystem.global_api_ecosystem.global_bada_business_api_ecosystem.governance.routes import router


class BadaBusinessApprovedRequirementsTests(unittest.TestCase):
    def test_approved_requirements_are_unique_and_complete(self):
        result = validate_approved_requirements()
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["count"], len(APPROVED_REQUIREMENTS))

    def test_recorded_user_decisions_include_q8_to_q13_and_q22_to_q35(self):
        ids = {item["id"] for item in APPROVED_REQUIREMENTS}
        expected = {f"Q{i:02d}" for i in range(8, 14)} | {f"Q{i:02d}" for i in range(22, 36)}
        self.assertTrue(expected.issubset(ids))
        self.assertTrue(all(item["decision"] == "YES" for item in APPROVED_REQUIREMENTS))

    def test_registry_returns_defensive_copies(self):
        records = list_approved_requirements()
        records[0]["title"] = "mutated"
        self.assertNotEqual(records[0]["title"], list_approved_requirements()[0]["title"])

    def test_governance_routes_are_registered(self):
        paths = {route.path for route in router.routes}
        self.assertIn("/governance/approved-requirements", paths)
        self.assertIn("/governance/requirements/integrity", paths)


if __name__ == "__main__":
    unittest.main()
