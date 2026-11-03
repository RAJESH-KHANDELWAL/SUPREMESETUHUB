import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ElectricalMechanicalPostsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Electrical and mechanical engineering posts", recruiting_authority="Official recruiting authority", engineering_grade="As notified", electrical_or_mechanical_discipline="Relevant department", plant_or_utility="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "engineering_and_technical")
        self.assertEqual(result["specialization"], "electrical_mechanical_posts")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, engineering_grade=post.engineering_grade, electrical_or_mechanical_discipline=post.electrical_or_mechanical_discipline, plant_or_utility=post.plant_or_utility)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
