"""Unit tests for Bada Business CORE programs domain."""

import unittest

from .manager import BadaBusinessProgramsManager
from .policies import normalize_program_id, validate_enrollment_request


class ProgramPolicyTests(unittest.TestCase):
    def test_normalize_program_id(self):
        self.assertEqual(normalize_program_id(" LFP-Digital "), "lfp_digital")

    def test_enrollment_request_requires_contact_fields(self):
        with self.assertRaises(ValueError):
            validate_enrollment_request(
                {"program_id": "lfp_digital"},
                {"name": "Test"},
            )

    def test_enrollment_request_has_no_side_effects(self):
        result = validate_enrollment_request(
            {"program_id": "lfp_digital"},
            {"name": "Test User", "mobile_number": "9999999999", "email": "test@example.com"},
        )
        self.assertTrue(result["valid"])
        self.assertFalse(result["registration_submitted"])
        self.assertFalse(result["payment_processed"])


class ProgramServiceTests(unittest.TestCase):
    def setUp(self):
        self.manager = BadaBusinessProgramsManager()

    def test_canonical_programs_are_discoverable(self):
        result = self.manager.list_programs()
        self.assertTrue(result["success"])
        self.assertGreaterEqual(result["count"], 3)

    def test_known_program_can_be_loaded(self):
        result = self.manager.get_program("lfp-digital")
        self.assertTrue(result["success"])
        self.assertEqual(result["program"]["program_id"], "lfp_digital")

    def test_unknown_program_is_not_found(self):
        result = self.manager.get_program("not-a-real-program")
        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "PROGRAM_NOT_FOUND")

    def test_status_does_not_claim_live_registration(self):
        status = self.manager.status()
        self.assertFalse(status["live_registration_enabled"])
        self.assertFalse(status["payment_processing_enabled"])


if __name__ == "__main__":
    unittest.main()
