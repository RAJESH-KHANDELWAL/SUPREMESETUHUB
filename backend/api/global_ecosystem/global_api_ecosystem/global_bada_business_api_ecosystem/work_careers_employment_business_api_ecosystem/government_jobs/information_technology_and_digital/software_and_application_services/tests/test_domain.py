import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class SoftwareAndApplicationServicesTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Software and application development posts", recruiting_authority="Official recruiting authority", it_grade="As notified", digital_department="Relevant department", software_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "information_technology_and_digital")
        self.assertEqual(result["specialization"], "software_and_application_services")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, it_grade=post.it_grade, digital_department=post.digital_department, software_specialism=post.software_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
