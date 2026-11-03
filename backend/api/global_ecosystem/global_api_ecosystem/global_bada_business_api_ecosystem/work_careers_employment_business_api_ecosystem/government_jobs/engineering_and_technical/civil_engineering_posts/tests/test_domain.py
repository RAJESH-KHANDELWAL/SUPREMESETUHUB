import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class CivilEngineeringPostsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Civil engineering government posts", recruiting_authority="Official recruiting authority", engineering_grade="As notified", civil_discipline="Relevant department", project_or_site="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "engineering_and_technical")
        self.assertEqual(result["specialization"], "civil_engineering_posts")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, engineering_grade=post.engineering_grade, civil_discipline=post.civil_discipline, project_or_site=post.project_or_site)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
