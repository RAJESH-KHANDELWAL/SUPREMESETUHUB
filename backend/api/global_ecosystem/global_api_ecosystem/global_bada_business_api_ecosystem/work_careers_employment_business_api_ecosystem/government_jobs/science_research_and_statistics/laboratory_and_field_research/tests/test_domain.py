import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class LaboratoryAndFieldResearchTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Laboratory and field research posts", recruiting_authority="Official recruiting authority", research_support_grade="As notified", laboratory_or_field_station="Relevant department", research_method="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "science_research_and_statistics")
        self.assertEqual(result["specialization"], "laboratory_and_field_research")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, research_support_grade=post.research_support_grade, laboratory_or_field_station=post.laboratory_or_field_station, research_method=post.research_method)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
