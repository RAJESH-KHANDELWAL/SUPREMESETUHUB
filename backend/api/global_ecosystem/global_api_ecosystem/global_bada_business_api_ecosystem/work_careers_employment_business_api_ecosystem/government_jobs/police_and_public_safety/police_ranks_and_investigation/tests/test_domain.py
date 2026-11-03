import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class PoliceRanksAndInvestigationTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Police rank and investigation posts", recruiting_authority="Official recruiting authority", police_rank="As notified", police_branch="Relevant department", police_station_or_unit="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "police_and_public_safety")
        self.assertEqual(result["specialization"], "police_ranks_and_investigation")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, police_rank=post.police_rank, police_branch=post.police_branch, police_station_or_unit=post.police_station_or_unit)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
