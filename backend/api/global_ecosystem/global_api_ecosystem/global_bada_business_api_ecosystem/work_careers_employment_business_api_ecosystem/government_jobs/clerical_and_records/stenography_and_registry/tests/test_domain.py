import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class StenographyAndRegistryTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Stenography, registry and records posts", recruiting_authority="Official recruiting authority", stenography_or_registry_grade="As notified", registry_or_officer="Relevant department", shorthand_or_registry_skill="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "clerical_and_records")
        self.assertEqual(result["specialization"], "stenography_and_registry")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, stenography_or_registry_grade=post.stenography_or_registry_grade, registry_or_officer=post.registry_or_officer, shorthand_or_registry_skill=post.shorthand_or_registry_skill)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
