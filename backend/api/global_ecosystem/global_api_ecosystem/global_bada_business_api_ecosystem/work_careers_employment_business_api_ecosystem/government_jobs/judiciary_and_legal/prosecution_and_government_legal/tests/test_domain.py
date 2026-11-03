import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ProsecutionAndGovernmentLegalTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Prosecution and government legal posts", recruiting_authority="Official recruiting authority", legal_officer_grade="As notified", prosecution_or_department="Relevant department", legal_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "judiciary_and_legal")
        self.assertEqual(result["specialization"], "prosecution_and_government_legal")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, legal_officer_grade=post.legal_officer_grade, prosecution_or_department=post.prosecution_or_department, legal_specialism=post.legal_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
