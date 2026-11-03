import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class ForestWildlifeAndEnvironmentTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Forest, wildlife and environmental posts", recruiting_authority="Official recruiting authority", environmental_service_rank="As notified", forest_or_environment_circle="Relevant department", conservation_specialism="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "agriculture_rural_and_environment")
        self.assertEqual(result["specialization"], "forest_wildlife_and_environment")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, environmental_service_rank=post.environmental_service_rank, forest_or_environment_circle=post.forest_or_environment_circle, conservation_specialism=post.conservation_specialism)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
