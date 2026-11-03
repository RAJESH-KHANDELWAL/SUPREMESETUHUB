import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class UpperDivisionAssistantsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Senior clerical and establishment posts", recruiting_authority="Official recruiting authority", senior_clerical_grade="As notified", office_or_section="Relevant department", subject_allocation="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "clerical_and_records")
        self.assertEqual(result["specialization"], "upper_division_assistants")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, senior_clerical_grade=post.senior_clerical_grade, office_or_section=post.office_or_section, subject_allocation=post.subject_allocation)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
