import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class JudicialOfficersTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Judicial officer recruitment", recruiting_authority="Official recruiting authority", judicial_rank="As notified", court_level="Relevant department", jurisdiction="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "judiciary_and_legal")
        self.assertEqual(result["specialization"], "judicial_officers")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, judicial_rank=post.judicial_rank, court_level=post.court_level, jurisdiction=post.jurisdiction)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
