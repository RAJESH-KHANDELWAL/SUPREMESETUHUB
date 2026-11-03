import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class PublicBankOfficersTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Public sector bank officer posts", recruiting_authority="Official recruiting authority", bank_officer_scale="As notified", bank_or_institution="Relevant department", banking_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "banking_finance_and_audit")
        self.assertEqual(result["specialization"], "public_bank_officers")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, bank_officer_scale=post.bank_officer_scale, bank_or_institution=post.bank_or_institution, banking_specialism=post.banking_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
