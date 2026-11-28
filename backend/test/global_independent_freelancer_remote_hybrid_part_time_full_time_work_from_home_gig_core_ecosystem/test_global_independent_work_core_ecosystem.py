"""Tests for the Global Independent Work CORE Ecosystem."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_core_ecosystem.catalog import (
    ECOSYSTEM_ID,
    PARENT_ECOSYSTEM_ID,
    get_catalog,
    get_work_model,
    list_work_models,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_core_ecosystem.manager import (
    GlobalIndependentWorkCoreManager,
    get_manager,
)


class GlobalIndependentWorkCoreEcosystemTests(unittest.TestCase):
    def test_manager_factory_and_status(self):
        manager = get_manager()
        self.assertIsInstance(manager, GlobalIndependentWorkCoreManager)
        status = manager.status()
        self.assertEqual(status["ecosystem_id"], ECOSYSTEM_ID)
        self.assertEqual(status["parent_id"], PARENT_ECOSYSTEM_ID)
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")

    def test_canonical_work_models(self):
        expected = {
            "FREELANCER", "REMOTE", "HYBRID", "PART_TIME",
            "FULL_TIME", "WORK_FROM_HOME", "GIG",
        }
        models = list_work_models()
        self.assertEqual({item["id"] for item in models}, expected)
        self.assertEqual(get_catalog()["work_model_count"], len(expected))

    def test_lookup_is_case_insensitive_and_unknown_returns_none(self):
        self.assertEqual(get_work_model(" remote ")["id"], "REMOTE")
        self.assertIsNone(get_work_model("NOT_A_WORK_MODEL"))

    def test_catalog_returns_independent_work_model_data(self):
        first = list_work_models()
        first[0]["name"] = "mutated"
        self.assertNotEqual(list_work_models()[0]["name"], "mutated")


if __name__ == "__main__":
    unittest.main()
