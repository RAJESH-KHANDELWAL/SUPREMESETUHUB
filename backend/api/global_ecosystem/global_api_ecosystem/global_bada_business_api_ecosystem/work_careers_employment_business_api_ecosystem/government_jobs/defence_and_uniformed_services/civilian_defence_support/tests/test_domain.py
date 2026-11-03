import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class CivilianDefenceSupportTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Civilian defence establishment posts", recruiting_authority="Official recruiting authority", civilian_pay_level="As notified", defence_establishment="Relevant department", support_function="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "defence_and_uniformed_services")
        self.assertEqual(result["specialization"], "civilian_defence_support")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, civilian_pay_level=post.civilian_pay_level, defence_establishment=post.defence_establishment, support_function=post.support_function)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
