import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class StatisticsEconomicsAndSurveysTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Statistics, economics and survey posts", recruiting_authority="Official recruiting authority", analytical_grade="As notified", statistics_or_economic_unit="Relevant department", quantitative_discipline="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "science_research_and_statistics")
        self.assertEqual(result["specialization"], "statistics_economics_and_surveys")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, analytical_grade=post.analytical_grade, statistics_or_economic_unit=post.statistics_or_economic_unit, quantitative_discipline=post.quantitative_discipline)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
