import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class AdministrativeServicesTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Civil and allied administrative service posts", recruiting_authority="Official recruiting authority", service_cadre="As notified", administrative_authority="Relevant department", district_or_department="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "administration_and_secretariat")
        self.assertEqual(result["specialization"], "administrative_services")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, service_cadre=post.service_cadre, administrative_authority=post.administrative_authority, district_or_department=post.district_or_department)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
