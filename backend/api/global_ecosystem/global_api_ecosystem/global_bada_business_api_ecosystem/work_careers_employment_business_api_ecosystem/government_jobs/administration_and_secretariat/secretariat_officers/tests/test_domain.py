import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class SecretariatOfficersTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Secretariat and section officer posts", recruiting_authority="Official recruiting authority", secretariat_grade="As notified", ministry_or_department="Relevant department", file_and_policy_subject="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "administration_and_secretariat")
        self.assertEqual(result["specialization"], "secretariat_officers")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, secretariat_grade=post.secretariat_grade, ministry_or_department=post.ministry_or_department, file_and_policy_subject=post.file_and_policy_subject)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
