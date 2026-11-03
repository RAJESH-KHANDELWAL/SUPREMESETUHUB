import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class GovernmentAccountsTaxAndAuditTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Government accounts, taxation and audit posts", recruiting_authority="Official recruiting authority", accounts_or_audit_grade="As notified", department_or_audit_body="Relevant department", finance_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "banking_finance_and_audit")
        self.assertEqual(result["specialization"], "government_accounts_tax_and_audit")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, accounts_or_audit_grade=post.accounts_or_audit_grade, department_or_audit_body=post.department_or_audit_body, finance_specialism=post.finance_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
