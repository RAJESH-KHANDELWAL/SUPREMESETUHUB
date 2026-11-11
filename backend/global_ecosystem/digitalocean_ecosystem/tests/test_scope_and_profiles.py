import unittest

from backend.global_ecosystem.digitalocean_ecosystem.workload_domains import (
    GEOGRAPHIC_SCOPES, MATURITY_LEVELS, list_workload_domains,
    find_domain_for_group, validate_scope,
)
from backend.global_ecosystem.digitalocean_ecosystem.deployment_profiles import (
    get_deployment_profile, validate_profiles,
)
from backend.global_ecosystem.digitalocean_ecosystem.governance import (
    controls_for_domain, validate_adult_only_deployment,
)

class DigitalOceanScopeTests(unittest.TestCase):
    def test_bharat_and_global_scopes_exist(self):
        self.assertIn("bharat_india", GEOGRAPHIC_SCOPES)
        self.assertIn("global", GEOGRAPHIC_SCOPES)

    def test_normal_to_supreme_levels_exist(self):
        self.assertEqual(len(MATURITY_LEVELS), 10)
        self.assertEqual(MATURITY_LEVELS[0], "normal")
        self.assertEqual(MATURITY_LEVELS[-1], "supreme")

    def test_workload_domain_mapping(self):
        self.assertTrue(list_workload_domains())
        self.assertEqual(find_domain_for_group("adult_platforms"), "adult_only_services")
        self.assertEqual(find_domain_for_group("ai"), "ai_data")

    def test_scope_validation(self):
        self.assertEqual(validate_scope("bharat_india", "supreme"), [])
        self.assertTrue(validate_scope("unknown", "unlimited"))

    def test_every_maturity_level_has_profile(self):
        self.assertTrue(validate_profiles()["valid"])
        for level in MATURITY_LEVELS:
            self.assertIsNotNone(get_deployment_profile(level))

    def test_profiles_are_not_provider_plan_claims(self):
        self.assertFalse(get_deployment_profile("supreme")["provider_plan_verified"])

    def test_adult_only_controls_are_added(self):
        result = controls_for_domain("adult_only_services")
        self.assertIn("effective_age_assurance", result["controls"])
        self.assertTrue(result["prohibited"])

    def test_adult_only_deployment_requires_safeguards(self):
        self.assertTrue(validate_adult_only_deployment(False, False, False, False))
        self.assertEqual(validate_adult_only_deployment(True, True, True, True), [])

if __name__ == "__main__":
    unittest.main()
