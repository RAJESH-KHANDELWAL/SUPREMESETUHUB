import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class DiagnosticsAndPublicHealthTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Diagnostic and public health posts", recruiting_authority="Official recruiting authority", technical_health_grade="As notified", diagnostic_or_public_health="Relevant department", lab_or_field_unit="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "healthcare_and_medical")
        self.assertEqual(result["specialization"], "diagnostics_and_public_health")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, technical_health_grade=post.technical_health_grade, diagnostic_or_public_health=post.diagnostic_or_public_health, lab_or_field_unit=post.lab_or_field_unit)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
