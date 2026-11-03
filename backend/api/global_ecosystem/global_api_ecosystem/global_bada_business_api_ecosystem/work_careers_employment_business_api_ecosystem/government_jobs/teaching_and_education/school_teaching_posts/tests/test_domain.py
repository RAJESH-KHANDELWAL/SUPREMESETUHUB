import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class SchoolTeachingPostsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="School teaching posts", recruiting_authority="Official recruiting authority", teacher_grade="As notified", school_level="Relevant department", subject="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "teaching_and_education")
        self.assertEqual(result["specialization"], "school_teaching_posts")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, teacher_grade=post.teacher_grade, school_level=post.school_level, subject=post.subject)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
