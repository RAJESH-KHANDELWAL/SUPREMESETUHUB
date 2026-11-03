import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class InfrastructureNetworkAndDatabaseTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="IT infrastructure and database posts", recruiting_authority="Official recruiting authority", infrastructure_grade="As notified", it_operations_unit="Relevant department", platform_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "information_technology_and_digital")
        self.assertEqual(result["specialization"], "infrastructure_network_and_database")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, infrastructure_grade=post.infrastructure_grade, it_operations_unit=post.it_operations_unit, platform_specialism=post.platform_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
