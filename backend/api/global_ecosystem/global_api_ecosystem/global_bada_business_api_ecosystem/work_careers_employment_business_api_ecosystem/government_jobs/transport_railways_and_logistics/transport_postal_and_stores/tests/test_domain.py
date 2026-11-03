import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class TransportPostalAndStoresTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Transport, postal and government logistics posts", recruiting_authority="Official recruiting authority", logistics_grade="As notified", transport_or_postal_unit="Relevant department", logistics_function="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "transport_railways_and_logistics")
        self.assertEqual(result["specialization"], "transport_postal_and_stores")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, logistics_grade=post.logistics_grade, transport_or_postal_unit=post.transport_or_postal_unit, logistics_function=post.logistics_function)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
