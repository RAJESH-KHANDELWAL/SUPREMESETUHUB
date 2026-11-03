import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class MultiTaskingAndFacilityFieldStaffTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Multi-tasking, facility and field support posts", recruiting_authority="Official recruiting authority", support_pay_level="As notified", facility_or_field_unit="Relevant department", work_assignment="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "skilled_trades_and_field_operations")
        self.assertEqual(result["specialization"], "multi_tasking_and_facility_field_staff")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, support_pay_level=post.support_pay_level, facility_or_field_unit=post.facility_or_field_unit, work_assignment=post.work_assignment)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
