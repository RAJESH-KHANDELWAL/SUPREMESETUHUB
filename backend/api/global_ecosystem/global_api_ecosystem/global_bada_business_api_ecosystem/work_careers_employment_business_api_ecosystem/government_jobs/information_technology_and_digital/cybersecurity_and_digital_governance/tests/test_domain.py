import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class CybersecurityAndDigitalGovernanceTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Cybersecurity and digital governance posts", recruiting_authority="Official recruiting authority", security_or_governance_grade="As notified", cyber_or_governance_unit="Relevant department", security_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "information_technology_and_digital")
        self.assertEqual(result["specialization"], "cybersecurity_and_digital_governance")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, security_or_governance_grade=post.security_or_governance_grade, cyber_or_governance_unit=post.cyber_or_governance_unit, security_specialism=post.security_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
