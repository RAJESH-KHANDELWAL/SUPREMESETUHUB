import unittest
from ..models import GovernmentPost
from ..services import register_post
from ..validators import validate_post

class PlantVehicleAndEquipmentOperatorsTests(unittest.TestCase):
    def make_post(self):
        return GovernmentPost(post_id="sample-001", post_title="Plant, vehicle and equipment operator posts", recruiting_authority="Official recruiting authority", operator_grade="As notified", operator_category="Relevant department", licence_or_equipment="India", official_notice_url="https://example.gov.in/notice")

    def test_registers_specialization_metadata(self):
        result = register_post(self.make_post())
        self.assertEqual(result["job_family"], "skilled_trades_and_field_operations")
        self.assertEqual(result["specialization"], "plant_vehicle_and_equipment_operators")

    def test_rejects_missing_required_fields(self):
        post = self.make_post()
        broken = GovernmentPost(post_id="", post_title=post.post_title, recruiting_authority=post.recruiting_authority, operator_grade=post.operator_grade, operator_category=post.operator_category, licence_or_equipment=post.licence_or_equipment)
        with self.assertRaises(ValueError):
            validate_post(broken)

if __name__ == "__main__":
    unittest.main()
