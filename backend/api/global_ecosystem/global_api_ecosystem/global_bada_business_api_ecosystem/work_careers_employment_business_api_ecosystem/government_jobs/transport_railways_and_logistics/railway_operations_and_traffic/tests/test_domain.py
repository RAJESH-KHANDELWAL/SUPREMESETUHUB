import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class RailwayOperationsAndTrafficTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Railway operations and traffic posts", recruiting_authority="Official recruiting authority", railway_operating_grade="As notified", railway_zone_or_division="Relevant department", operating_department="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "transport_railways_and_logistics")
        self.assertEqual(result["specialization"], "railway_operations_and_traffic")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, railway_operating_grade=post.railway_operating_grade, railway_zone_or_division=post.railway_zone_or_division, operating_department=post.operating_department)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
