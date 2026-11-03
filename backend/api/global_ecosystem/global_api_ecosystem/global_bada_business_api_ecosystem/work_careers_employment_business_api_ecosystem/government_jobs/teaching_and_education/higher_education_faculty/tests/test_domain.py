import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class HigherEducationFacultyTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="College and university faculty posts", recruiting_authority="Official recruiting authority", faculty_rank="As notified", institution_type="Relevant department", academic_discipline="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "teaching_and_education")
        self.assertEqual(result["specialization"], "higher_education_faculty")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, faculty_rank=post.faculty_rank, institution_type=post.institution_type, academic_discipline=post.academic_discipline)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
