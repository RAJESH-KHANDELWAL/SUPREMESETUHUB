import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class AgricultureHorticultureAndExtensionTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Agriculture, horticulture and extension posts", recruiting_authority="Official recruiting authority", agriculture_grade="As notified", agriculture_department="Relevant department", crop_or_extension_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "agriculture_rural_and_environment")
        self.assertEqual(result["specialization"], "agriculture_horticulture_and_extension")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, agriculture_grade=post.agriculture_grade, agriculture_department=post.agriculture_department, crop_or_extension_specialism=post.crop_or_extension_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
