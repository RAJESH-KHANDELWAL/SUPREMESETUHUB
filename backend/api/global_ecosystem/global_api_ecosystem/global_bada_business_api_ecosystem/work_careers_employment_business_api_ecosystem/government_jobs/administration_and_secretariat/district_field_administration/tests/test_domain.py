import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class DistrictFieldAdministrationTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="District and field administration posts", recruiting_authority="Official recruiting authority", field_cadre="As notified", district_or_block="Relevant department", jurisdiction="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "administration_and_secretariat")
        self.assertEqual(result["specialization"], "district_field_administration")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, field_cadre=post.field_cadre, district_or_block=post.district_or_block, jurisdiction=post.jurisdiction)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
