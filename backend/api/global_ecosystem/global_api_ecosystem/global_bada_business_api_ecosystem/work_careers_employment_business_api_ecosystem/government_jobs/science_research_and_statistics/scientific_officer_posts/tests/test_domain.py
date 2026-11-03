import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ScientificOfficerPostsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Scientific officer and scientist posts", recruiting_authority="Official recruiting authority", scientist_grade="As notified", research_institution="Relevant department", scientific_discipline="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "science_research_and_statistics")
        self.assertEqual(result["specialization"], "scientific_officer_posts")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, scientist_grade=post.scientist_grade, research_institution=post.research_institution, scientific_discipline=post.scientific_discipline)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
