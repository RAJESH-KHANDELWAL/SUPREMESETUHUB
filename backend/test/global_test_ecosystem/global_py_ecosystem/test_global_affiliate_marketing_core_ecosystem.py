"""Python contract tests for GLOBAL AFFILIATE MARKETING BUSINESS CORE."""
from __future__ import annotations

import unittest

from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.catalog import (
    AFFILIATE_NETWORK_CATALOG,
    PLATFORM_CATALOG,
    get_platform,
    list_platforms,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.manager import (
    GlobalAffiliateMarketingCoreManager,
    get_manager,
)


class GlobalAffiliateMarketingCoreEcosystemTests(unittest.TestCase):
    def setUp(self) -> None:
        self.manager = GlobalAffiliateMarketingCoreManager()

    def test_manager_factory_returns_core_manager(self) -> None:
        self.assertIsInstance(get_manager(), GlobalAffiliateMarketingCoreManager)

    def test_core_status_identifies_ecosystem_and_layer(self) -> None:
        status = self.manager.status()
        self.assertTrue(status["success"])
        self.assertEqual(
            status["ecosystem_id"],
            "GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM",
        )
        self.assertEqual(status["layer"], "CORE")
        self.assertFalse(status["live_connections_verified"])

    def test_platform_catalog_keeps_three_platforms_separate(self) -> None:
        self.assertEqual(
            {item["platform_id"] for item in PLATFORM_CATALOG},
            {"I-DIGITALPRENEUR", "LEADSGURU", "MILLIONAIRE-TRACK"},
        )
        self.assertEqual(len({item["platform_id"] for item in PLATFORM_CATALOG}), 3)

    def test_network_candidates_are_not_claimed_as_verified(self) -> None:
        self.assertTrue(AFFILIATE_NETWORK_CATALOG)
        self.assertTrue(
            all(item["catalog_status"] == "DISCOVERY_ONLY" for item in AFFILIATE_NETWORK_CATALOG)
        )
        self.assertTrue(
            all(item["verification_status"] == "UNVERIFIED" for item in AFFILIATE_NETWORK_CATALOG)
        )
        self.assertTrue(
            all(item["live_connection_verified"] is False for item in AFFILIATE_NETWORK_CATALOG)
        )

    def test_region_filter_and_platform_lookup(self) -> None:
        self.assertTrue(all(item["region_scope"] == "GLOBAL" for item in list_platforms(region="GLOBAL")))
        self.assertTrue(all(item["region_scope"] == "INDIA" for item in list_platforms(region="INDIA")))
        self.assertEqual(get_platform("I-DIGITALPRENEUR")["name"], "iDigitalPreneur")
        self.assertIsNone(get_platform("NOT-REGISTERED"))

    def test_master_catalog_inventory_counts_and_affiliate_entry(self) -> None:
        inventory = self.manager.master_catalog_inventory()
        self.assertTrue(inventory["success"])
        self.assertEqual(inventory["catalogue_id"], "GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM")
        self.assertEqual(inventory["target_unique_entries"], 2468)
        self.assertEqual(
            inventory["current_unique_entries"] + inventory["remaining_unique_entries"],
            2468,
        )
        self.assertEqual(inventory["source_numbered_entries"], 248)
        self.assertEqual(inventory["cross_reference_entries"], 2)
        self.assertEqual(inventory["section_count"], 13)
        self.assertTrue(
            any(
                entry["entry_id"] == "S08_affiliate_business"
                for entry in inventory["affiliate_business_entries"]
            )
        )

    def test_master_catalog_lookup_is_read_only(self) -> None:
        entry = self.manager.get_master_catalog_entry("S08_affiliate_business")
        self.assertIsNotNone(entry)
        self.assertEqual(entry["entry_id"], "S08_affiliate_business")
        self.assertIsNone(self.manager.get_master_catalog_entry("UNKNOWN_ENTRY"))


if __name__ == "__main__":
    unittest.main()
