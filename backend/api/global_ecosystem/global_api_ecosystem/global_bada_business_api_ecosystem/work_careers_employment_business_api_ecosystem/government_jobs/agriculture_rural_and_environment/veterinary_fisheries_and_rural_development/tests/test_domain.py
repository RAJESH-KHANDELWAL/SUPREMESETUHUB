import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class VeterinaryFisheriesAndRuralDevelopmentTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Veterinary, fisheries and rural development posts", recruiting_authority="Official recruiting authority", rural_service_grade="As notified", rural_or_animal_husbandry_unit="Relevant department", field_programme="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "agriculture_rural_and_environment")
        self.assertEqual(result["specialization"], "veterinary_fisheries_and_rural_development")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, rural_service_grade=post.rural_service_grade, rural_or_animal_husbandry_unit=post.rural_or_animal_husbandry_unit, field_programme=post.field_programme)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
