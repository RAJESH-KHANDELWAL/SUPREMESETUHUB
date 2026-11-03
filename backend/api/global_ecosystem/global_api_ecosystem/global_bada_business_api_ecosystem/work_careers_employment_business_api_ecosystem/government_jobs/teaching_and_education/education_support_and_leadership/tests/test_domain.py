import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class EducationSupportAndLeadershipTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Education leadership and specialist support posts", recruiting_authority="Official recruiting authority", leadership_or_support_grade="As notified", school_or_institution="Relevant department", specialist_function="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "teaching_and_education")
        self.assertEqual(result["specialization"], "education_support_and_leadership")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, leadership_or_support_grade=post.leadership_or_support_grade, school_or_institution=post.school_or_institution, specialist_function=post.specialist_function)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
