"""Tests for the Global Independent Work Service Work Business CORE Ecosystem."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_service_work_business_core_ecosystem.catalog import (
    ECOSYSTEM_ID,
    PARENT_ECOSYSTEM_ID,
    get_catalog,
    get_work_model,
    list_work_models,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_service_work_business_core_ecosystem.manager import (
    GlobalIndependentWorkServiceBusinessCoreManager,
    get_manager,
)


class GlobalIndependentWorkServiceWorkBusinessCoreEcosystemTests(unittest.TestCase):
    def test_manager_factory_and_status(self):
        manager = get_manager()
        self.assertIsInstance(manager, GlobalIndependentWorkServiceBusinessCoreManager)
        status = manager.status()
        self.assertEqual(status["ecosystem_id"], ECOSYSTEM_ID)
        self.assertEqual(status["parent_id"], PARENT_ECOSYSTEM_ID)
        self.assertEqual(status["status"], "CORE_CATALOG_ONLY")

    def test_work_model_adapter_exposes_expected_ids(self):
        expected = {
            "FREELANCER", "REMOTE", "HYBRID", "PART_TIME",
            "FULL_TIME", "WORK_FROM_HOME", "GIG",
        }
        self.assertEqual({item["id"] for item in list_work_models()}, expected)
        self.assertEqual(get_catalog()["work_model_count"], len(expected))

    def test_work_model_lookup(self):
        self.assertEqual(get_work_model("gig")["id"], "GIG")
        self.assertIsNone(get_work_model("UNKNOWN"))

    def test_catalog_does_not_claim_live_jobs_or_provider_connections(self):
        catalog = get_catalog()
        self.assertFalse(catalog["live_jobs_verified"])
        self.assertFalse(catalog["provider_connections_enabled"])


if __name__ == "__main__":
    unittest.main()
