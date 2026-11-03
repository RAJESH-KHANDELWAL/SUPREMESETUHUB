import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class NursingAndPharmacyTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Nursing and pharmacy posts", recruiting_authority="Official recruiting authority", clinical_support_grade="As notified", nursing_or_pharmacy="Relevant department", facility_or_ward="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "healthcare_and_medical")
        self.assertEqual(result["specialization"], "nursing_and_pharmacy")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, clinical_support_grade=post.clinical_support_grade, nursing_or_pharmacy=post.nursing_or_pharmacy, facility_or_ward=post.facility_or_ward)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
