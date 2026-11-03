import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class CourtAdministrationAndRegistryTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Court administration and registry posts", recruiting_authority="Official recruiting authority", court_staff_grade="As notified", court_or_registry="Relevant department", court_function="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "judiciary_and_legal")
        self.assertEqual(result["specialization"], "court_administration_and_registry")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, court_staff_grade=post.court_staff_grade, court_or_registry=post.court_or_registry, court_function=post.court_function)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
