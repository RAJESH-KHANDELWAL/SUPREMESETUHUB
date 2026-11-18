import unittest

from global_agriculture_ecosystem.models import CropPlan, Farm
from global_agriculture_ecosystem.planning import estimate_irrigation_water_m3
from global_agriculture_ecosystem.validation import validate_crop_plan, validate_farm
from global_agriculture_ecosystem.catalog import list_modules

class AgricultureTests(unittest.TestCase):
    def test_catalog_has_nine_modules(self):
        self.assertEqual(len(list_modules()), 9)

    def test_farm_validation(self):
        farm = Farm("F-1", "Demo Farm", "IN", "Rajasthan", 2.0)
        self.assertEqual(validate_farm(farm), [])

    def test_crop_plan_validation(self):
        plan = CropPlan("F-1", "Wheat", 1.5, "Rabi")
        self.assertEqual(validate_crop_plan(plan), [])

    def test_irrigation_estimate(self):
        result = estimate_irrigation_water_m3(1, 5, 0.8, 2)
        self.assertAlmostEqual(result.water_depth_mm, 8)
        self.assertAlmostEqual(result.water_volume_m3, 80)

    def test_rejects_zero_area(self):
        with self.assertRaises(ValueError):
            estimate_irrigation_water_m3(0, 5, 0.8)

if __name__ == "__main__":
    unittest.main()
