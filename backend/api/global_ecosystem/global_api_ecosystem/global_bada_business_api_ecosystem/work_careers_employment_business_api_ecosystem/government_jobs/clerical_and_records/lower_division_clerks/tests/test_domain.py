import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class LowerDivisionClerksTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Entry-level clerical and data processing posts", recruiting_authority="Official recruiting authority", clerical_grade="As notified", typing_or_data_skill="Relevant department", office_unit="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "clerical_and_records")
        self.assertEqual(result["specialization"], "lower_division_clerks")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, clerical_grade=post.clerical_grade, typing_or_data_skill=post.typing_or_data_skill, office_unit=post.office_unit)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
