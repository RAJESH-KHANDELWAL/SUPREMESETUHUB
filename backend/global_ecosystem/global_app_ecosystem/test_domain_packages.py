"""Domain package and scope coverage tests for GLOBAL APP."""
import unittest
from .scope import APP_CAPABILITY_LEVELS, list_domain_ids
from . import list_domain_packages, get_domain_package

class AppDomainPackageTests(unittest.TestCase):
    def test_all_scope_domains_have_packages(self):
        ids = list_domain_ids()
        profiles = list_domain_packages()
        self.assertEqual(len(ids), len(profiles))
        self.assertEqual({p["id"] for p in profiles}, set(ids))

    def test_normal_to_supreme_capability_levels(self):
        ids = [item["id"] for item in APP_CAPABILITY_LEVELS]
        self.assertEqual(ids[0], "normal_basic")
        self.assertEqual(ids[-1], "supreme_long_horizon")

    def test_adult_domains_are_explicitly_guarded(self):
        for domain_id in ("adult_age_restricted_platform_apps", "adult_dating_relationship_apps",
                          "adult_creator_subscription_apps", "adult_entertainment_streaming_apps",
                          "sexual_wellness_education_apps", "adult_content_safety_rights_apps"):
            profile = get_domain_package(domain_id)
            self.assertIsNotNone(profile)
            self.assertTrue(profile.get("safeguards"))

if __name__ == "__main__":
    unittest.main()
