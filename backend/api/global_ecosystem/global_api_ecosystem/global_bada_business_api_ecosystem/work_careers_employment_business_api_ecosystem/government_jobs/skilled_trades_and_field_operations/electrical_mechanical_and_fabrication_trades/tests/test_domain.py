import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ElectricalMechanicalAndFabricationTradesTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Electrical, mechanical and fabrication trades", recruiting_authority="Official recruiting authority", trade_grade="As notified", technical_trade="Relevant department", trade_certificate="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "skilled_trades_and_field_operations")
        self.assertEqual(result["specialization"], "electrical_mechanical_and_fabrication_trades")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, trade_grade=post.trade_grade, technical_trade=post.technical_trade, trade_certificate=post.trade_certificate)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
