import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class OtherRanksAndTechnicalTradesTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Other-rank and defence technical trade posts", recruiting_authority="Official recruiting authority", other_rank_or_trade="As notified", service_branch="Relevant department", trade_or_equipment="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "defence_and_uniformed_services")
        self.assertEqual(result["specialization"], "other_ranks_and_technical_trades")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, other_rank_or_trade=post.other_rank_or_trade, service_branch=post.service_branch, trade_or_equipment=post.trade_or_equipment)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
