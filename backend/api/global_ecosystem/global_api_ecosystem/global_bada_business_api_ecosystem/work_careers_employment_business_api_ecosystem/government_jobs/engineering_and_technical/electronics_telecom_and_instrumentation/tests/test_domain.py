import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ElectronicsTelecomAndInstrumentationTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Electronics, telecom and instrumentation posts", recruiting_authority="Official recruiting authority", technical_grade="As notified", electronics_telecom_or_instrumentation="Relevant department", network_or_control_site="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "engineering_and_technical")
        self.assertEqual(result["specialization"], "electronics_telecom_and_instrumentation")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, technical_grade=post.technical_grade, electronics_telecom_or_instrumentation=post.electronics_telecom_or_instrumentation, network_or_control_site=post.network_or_control_site)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
