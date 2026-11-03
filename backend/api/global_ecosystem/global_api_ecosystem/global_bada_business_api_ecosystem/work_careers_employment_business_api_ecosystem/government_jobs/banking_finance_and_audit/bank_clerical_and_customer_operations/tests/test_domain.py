import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class BankClericalAndCustomerOperationsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Public bank clerical and customer operations", recruiting_authority="Official recruiting authority", bank_clerical_grade="As notified", bank_or_branch="Relevant department", customer_or_cash_function="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "banking_finance_and_audit")
        self.assertEqual(result["specialization"], "bank_clerical_and_customer_operations")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, bank_clerical_grade=post.bank_clerical_grade, bank_or_branch=post.bank_or_branch, customer_or_cash_function=post.customer_or_cash_function)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
