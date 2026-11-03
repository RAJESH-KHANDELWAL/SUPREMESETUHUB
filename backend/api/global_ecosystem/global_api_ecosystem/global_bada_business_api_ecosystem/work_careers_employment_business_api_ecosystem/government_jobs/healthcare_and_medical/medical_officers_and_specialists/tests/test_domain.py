import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class MedicalOfficersAndSpecialistsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Medical officer and specialist posts", recruiting_authority="Official recruiting authority", medical_grade="As notified", clinical_specialty="Relevant department", hospital_or_health_unit="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "healthcare_and_medical")
        self.assertEqual(result["specialization"], "medical_officers_and_specialists")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, medical_grade=post.medical_grade, clinical_specialty=post.clinical_specialty, hospital_or_health_unit=post.hospital_or_health_unit)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
