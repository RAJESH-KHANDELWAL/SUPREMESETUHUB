import unittest

from backend.global_ecosystem.global_bada_business_ecosystem.business_verticals import (
    get_vertical, list_verticals, search_verticals, validate_adult_business_record,
)


class BusinessVerticalTests(unittest.TestCase):
    def test_catalog_has_broad_verticals(self):
        self.assertGreaterEqual(len(list_verticals()), 20)
        self.assertIsNotNone(get_vertical("agriculture"))
        self.assertIsNotNone(get_vertical("technology_ai"))

    def test_search_finds_direct_selling(self):
        self.assertTrue(search_verticals("direct selling"))

    def test_adult_vertical_requires_safeguards(self):
        errors = validate_adult_business_record({"vertical_id": "adult_entertainment_industry"})
        self.assertIn("adult_participants_verified must be true", errors)
        self.assertIn("consent_documented must be true", errors)

    def test_adult_record_with_required_controls(self):
        record = {
            "vertical_id": "adult_relationship_intimacy",
            "adult_participants_verified": True,
            "consent_documented": True,
            "rights_documented": True,
            "age_assurance_enabled": True,
            "moderation_process_defined": True,
            "privacy_controls_defined": True,
            "jurisdiction_reviewed": True,
        }
        self.assertEqual(validate_adult_business_record(record), [])


if __name__ == "__main__":
    unittest.main()
