import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class TrafficFireAndEmergencyTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Traffic, fire and emergency response posts", recruiting_authority="Official recruiting authority", response_rank="As notified", traffic_fire_or_emergency="Relevant department", response_station="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "police_and_public_safety")
        self.assertEqual(result["specialization"], "traffic_fire_and_emergency")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, response_rank=post.response_rank, traffic_fire_or_emergency=post.traffic_fire_or_emergency, response_station=post.response_station)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
