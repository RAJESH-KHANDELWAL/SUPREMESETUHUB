import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class CommissionedAndJuniorOfficersTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Commissioned and junior commissioned officer routes", recruiting_authority="Official recruiting authority", military_rank="As notified", arm_or_service="Relevant department", unit_or_command="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "defence_and_uniformed_services")
        self.assertEqual(result["specialization"], "commissioned_and_junior_officers")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, military_rank=post.military_rank, arm_or_service=post.arm_or_service, unit_or_command=post.unit_or_command)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
