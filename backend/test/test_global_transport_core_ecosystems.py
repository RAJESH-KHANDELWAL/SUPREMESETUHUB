"""Tests for transport CORE ownership and the Bada Business adapter."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_transport_road_rail_air_mobility_core_ecosystem import (
    GlobalTransportCoreManager,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_transport_logistics_supply_chain_service_work_business_core_ecosystem import (
    GlobalTransportBusinessCoreManager,
)

class GlobalTransportCoreTests(unittest.TestCase):
    def test_transport_core_registers_four_requested_domains(self):
        result = GlobalTransportCoreManager().list_domains()
        self.assertTrue(result["success"])
        self.assertEqual(
            {item["domain_id"] for item in result["domains"]},
            {"ROAD_TRANSPORT", "RAIL_TRANSPORT", "AIR_TRANSPORT", "MOBILITY"},
        )

    def test_business_adapter_has_five_separate_capability_groups(self):
        result = GlobalTransportBusinessCoreManager().list_capability_groups()
        self.assertTrue(result["success"])
        self.assertEqual(
            {item["group_id"] for item in result["capability_groups"]},
            {"LOGISTICS", "SUPPLY_CHAIN", "SERVICES", "WORK", "BUSINESS"},
        )

    def test_business_adapter_references_transport_core_without_claiming_live_operations(self):
        status = GlobalTransportBusinessCoreManager().status()
        self.assertEqual(
            status["transport_core_id"],
            "GLOBAL-TRANSPORT-ROAD-RAIL-AIR-MOBILITY-CORE-ECOSYSTEM",
        )
        self.assertFalse(status["live_jobs_verified"])
        self.assertFalse(status["live_transactions_verified"])

if __name__ == "__main__":
    unittest.main()
