"""Contract and inventory tests for the Global Affiliate Marketing CORE package."""
import unittest

from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager

from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.catalog import (
    AFFILIATE_NETWORK_CATALOG,
    PLATFORM_CATALOG,
    get_platform,
    list_platforms,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.manager import (
    GlobalAffiliateMarketingCoreManager,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.models import (
    AffiliatePlatformIdentity,
)
from backend.core.global_ecosystem.global_core_ecosystem.global_bada_business_core_ecosystem.global_affiliate_marketing_business_core_ecosystem.policies import (
    validate_affiliate_disclosure,
    validate_http_url,
    validate_program_activation,
)

class AffiliateMarketingCoreTests(unittest.TestCase):
    def test_inventory_has_unique_ids_and_preserves_three_program_platforms(self):
        records = [*PLATFORM_CATALOG, *AFFILIATE_NETWORK_CATALOG]
        ids = [item["platform_id"] for item in records]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(
            {item["platform_id"] for item in PLATFORM_CATALOG},
            {"I-DIGITALPRENEUR", "LEADSGURU", "MILLIONAIRE-TRACK"},
        )

    def test_network_candidates_are_not_marked_verified_or_live(self):
        self.assertEqual(len(AFFILIATE_NETWORK_CATALOG), 40)
        self.assertTrue(all(item["catalog_status"] == "DISCOVERY_ONLY" for item in AFFILIATE_NETWORK_CATALOG))
        self.assertTrue(all(item["verification_status"] == "UNVERIFIED" for item in AFFILIATE_NETWORK_CATALOG))
        self.assertTrue(all(item["live_connection_verified"] is False for item in AFFILIATE_NETWORK_CATALOG))

    def test_region_filter_is_explicit(self):
        self.assertTrue(all(item["region_scope"] == "GLOBAL" for item in list_platforms(region="GLOBAL")))
        self.assertTrue(all(item["region_scope"] == "INDIA" for item in list_platforms(region="INDIA")))

    def test_lookup_returns_copy_and_unknown_platform_is_none(self):
        record = get_platform("I-DIGITALPRENEUR")
        self.assertIsNotNone(record)
        record["name"] = "changed"
        self.assertEqual(get_platform("I-DIGITALPRENEUR")["name"], "iDigitalPreneur")
        self.assertIsNone(get_platform("NOT-REGISTERED"))

    def test_identity_model_preserves_unverified_state(self):
        identity = AffiliatePlatformIdentity.from_record(get_platform("LEADSGURU"))
        self.assertEqual(identity.verification_status, "UNVERIFIED")
        self.assertIsNone(identity.terms_url)

    def test_global_hierarchy_registers_affiliate_core_under_bada_business(self):
        record = GlobalEcosystemManager().get("GLOBAL-AFFILIATE-MARKETING-BUSINESS-CORE-ECOSYSTEM")
        self.assertIsNotNone(record)
        self.assertEqual(record["parent_id"], "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM")

    def test_master_catalog_bridge_validates_2468_source(self):
        inventory = GlobalAffiliateMarketingCoreManager().master_catalog_inventory()
        self.assertEqual(inventory["target_unique_entries"], 2468)
        self.assertEqual(inventory["current_unique_entries"], 246)
        self.assertEqual(inventory["remaining_unique_entries"], 2222)
        self.assertEqual(inventory["source_numbered_entries"], 248)
        self.assertEqual(inventory["cross_reference_entries"], 2)
        self.assertEqual(inventory["section_count"], 13)
        self.assertEqual(inventory["affiliate_business_entries"][0]["entry_id"], "S08_affiliate_business")

    def test_policy_requires_safe_url_and_visible_disclosure(self):
        self.assertEqual(validate_http_url("https://example.com/terms"), "https://example.com/terms")
        self.assertIn("affiliate", validate_affiliate_disclosure("This is an affiliate link and I may earn a commission.").lower())
        with self.assertRaises(ValueError):
            validate_http_url("javascript:alert(1)")
        with self.assertRaises(ValueError):
            validate_affiliate_disclosure("Thanks")

    def test_active_program_requires_verified_terms(self):
        with self.assertRaises(ValueError):
            validate_program_activation("ACTIVE", "UNVERIFIED", "https://example.com/terms")
        validate_program_activation("ACTIVE", "VERIFIED", "https://example.com/terms")

if __name__ == "__main__":
    unittest.main()
