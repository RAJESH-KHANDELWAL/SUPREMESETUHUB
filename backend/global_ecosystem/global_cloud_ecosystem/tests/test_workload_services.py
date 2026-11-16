"""Offline tests for top-level cloud workload service packages."""
import importlib
import unittest
from backend.global_ecosystem.global_cloud_ecosystem.workloads import list_cloud_workloads

class WorkloadServiceTests(unittest.TestCase):
    def test_every_workload_has_a_top_level_service_package(self):
        for row in list_cloud_workloads():
            module = importlib.import_module(
                f"backend.global_ecosystem.global_cloud_ecosystem.{row['id']}_cloud_ecosystem"
            )
            self.assertEqual(module.WORKLOAD_ID, row["id"])
            self.assertEqual(module.inspect()["id"], row["id"])

    def test_regular_workload_can_be_planned(self):
        from backend.global_ecosystem.global_cloud_ecosystem.agriculture_food_cloud_ecosystem import plan
        result = plan({})
        self.assertEqual(result["status"], "validated_for_planning_only")
        self.assertEqual(result["provider_execution"], "not_performed")

    def test_adult_workload_requires_safeguards(self):
        from backend.global_ecosystem.global_cloud_ecosystem.adult_entertainment_streaming_cloud_ecosystem import validate, WorkloadValidationError
        with self.assertRaises(WorkloadValidationError):
            validate({})
        safe = {"age_verified": True, "participants_are_adults": True, "consent_confirmed": True, "rights_cleared": True, "content_safety_confirmed": True, "anti_exploitation_controls": True, "privacy_and_legal_controls": True}
        self.assertEqual(validate(safe)["status"], "validated_for_planning_only")
        with self.assertRaises(WorkloadValidationError):
            validate(dict(safe, nonconsensual_intimate_content=True))

if __name__ == "__main__":
    unittest.main()
