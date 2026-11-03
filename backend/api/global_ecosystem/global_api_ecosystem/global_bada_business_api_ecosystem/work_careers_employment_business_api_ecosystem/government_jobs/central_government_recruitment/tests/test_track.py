"""Regression tests for the central government recruitment track package.

These tests validate taxonomy structure and API resource behavior only.
They do not claim that any vacancy is currently open or independently verified.
"""
import unittest

from ..categories import CATEGORY_ID, TRACK_ID, get_track_definition
from ..services import get_track_api_resource, get_track_status
from ..validators import validate_track_definition


class CentralGovernmentRecruitmentTrackTests(unittest.TestCase):
    def test_track_identity_is_stable(self):
        self.assertEqual(CATEGORY_ID, "government_jobs")
        self.assertEqual(TRACK_ID, "central_government_recruitment")

    def test_track_definition_has_required_classification(self):
        definition = get_track_definition()
        self.assertEqual(definition["id"], TRACK_ID)
        self.assertTrue(definition["name"].strip())
        self.assertTrue(definition["description"].strip())
        self.assertTrue(definition.get("authority_scope"))
        self.assertTrue(definition.get("role_families"))

    def test_validator_accepts_registered_track(self):
        result = validate_track_definition()
        self.assertTrue(result["valid"], result)
        self.assertEqual(result["category_id"], CATEGORY_ID)
        self.assertEqual(result["track_id"], TRACK_ID)

    def test_api_resource_preserves_domain_specific_fields(self):
        resource = get_track_api_resource()
        self.assertEqual(resource["id"], TRACK_ID)
        self.assertEqual(resource["category_id"], CATEGORY_ID)
        self.assertTrue(resource["role_families"])
        self.assertEqual(resource["taxonomy_status"], "taxonomy_only")
        self.assertFalse(resource["live_vacancies_available"])

    def test_status_does_not_claim_live_vacancy_verification(self):
        status = get_track_status()
        self.assertTrue(status["success"])
        self.assertTrue(status["structurally_valid"])
        self.assertFalse(status["live_vacancies_available"])
        self.assertEqual(status["taxonomy_status"], "taxonomy_only")


if __name__ == "__main__":
    unittest.main()
