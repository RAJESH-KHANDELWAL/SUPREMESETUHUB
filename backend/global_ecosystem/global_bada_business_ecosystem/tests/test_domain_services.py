"""Tests for Bada Business course, event, registration and referral services."""
from datetime import date
import unittest

from backend.global_ecosystem.global_bada_business_ecosystem.global_network_marketing_direct_selling_business_ecosystem.catalog import (
    find_platform, get_business_ecosystem, validate_business_ecosystems,
)
from backend.global_ecosystem.global_bada_business_ecosystem.courses.catalog import (
    get_course, list_courses, search_courses, validate_course_catalog,
)
from backend.global_ecosystem.global_bada_business_ecosystem.events.service import (
    get_event, list_events,
)
from backend.global_ecosystem.global_bada_business_ecosystem.registration.service import (
    create_registration_draft, validate_registration,
)
from backend.global_ecosystem.global_bada_business_ecosystem.referrals.service import (
    extract_referral_code, normalize_referral_url,
)


class CourseCatalogTests(unittest.TestCase):
    def test_catalog_integrity(self):
        self.assertEqual(validate_course_catalog(), ())

    def test_case_insensitive_lookup_and_copy(self):
        course = get_course(" LFP_DIGITAL ")
        self.assertIsNotNone(course)
        course["name"] = "mutated"
        self.assertNotEqual(get_course("lfp_digital")["name"], "mutated")

    def test_search_framework(self):
        self.assertTrue(search_courses("cash flow management"))

    def test_excludes_known_past_event_when_requested(self):
        self.assertIsNone(get_course("not-a-program"))
        courses = list_courses(include_past_events=False)
        self.assertNotIn("idea_to_ipo", [item["program_id"] for item in courses])


class EventTests(unittest.TestCase):
    def test_unknown_event_date_is_not_guessed(self):
        event = get_event("bb_impact", on_date=date(2026, 11, 10))
        self.assertEqual(event["lifecycle_status"], "DATE_NOT_PUBLISHED")

    def test_past_webinar_date_is_derived(self):
        event = get_event("idea_to_ipo", on_date=date(2026, 11, 10))
        self.assertEqual(event["lifecycle_status"], "PAST")


class RegistrationTests(unittest.TestCase):
    def test_valid_draft_is_not_marked_submitted(self):
        payload = {
            "full_name": "Test User",
            "mobile_number": "+919876543210",
            "email": "test@example.com",
            "pincode": "302013",
        }
        draft = create_registration_draft("lfp_digital", payload)
        self.assertEqual(draft.status, "DRAFT_NOT_SUBMITTED")

    def test_invalid_registration_returns_field_errors(self):
        errors = validate_registration({"full_name": "x"})
        self.assertIn("email", errors)
        self.assertIn("mobile_number", errors)


class NetworkMarketingRegistryTests(unittest.TestCase):
    def test_registry_integrity(self):
        self.assertEqual(validate_business_ecosystems(), ())

    def test_youtag_apps_share_one_business_parent(self):
        wellness = find_platform("youtag_wellness_app")
        recharges = find_platform("youtag_recharges_app")
        self.assertEqual(wellness["parent_ecosystem_id"], recharges["parent_ecosystem_id"])
        self.assertEqual(wellness["parent_ecosystem_id"], "global_youtag_business_ecosystem")

    def test_affiliate_platforms_are_separate_namespaces(self):
        self.assertEqual(find_platform("leadsguru")["category"], "affiliate_marketing")
        self.assertIsNotNone(get_business_ecosystem("global_affiliate_marketing_business_ecosystem"))


class ReferralTests(unittest.TestCase):
    def test_referral_code_is_added_and_extracted(self):
        url = normalize_referral_url("https://www.badabusiness.com/lfp?x=1", "BIRK076336")
        self.assertEqual(extract_referral_code(url), "BIRK076336")
        self.assertIn("x=1", url)

    def test_untrusted_host_is_rejected(self):
        with self.assertRaises(ValueError):
            normalize_referral_url("https://example.com/lfp", "CODE")


if __name__ == "__main__":
    unittest.main()
