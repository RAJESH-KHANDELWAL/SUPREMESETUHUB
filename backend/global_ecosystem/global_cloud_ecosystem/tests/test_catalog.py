"""Offline integrity tests for cloud provider and workload catalogs."""
import unittest

from backend.global_ecosystem.global_cloud_ecosystem import (
    list_cloud_providers, get_cloud_provider, validate_cloud_catalog,
    CLOUD_CAPABILITIES, CLOUD_SCOPES,
    list_cloud_workloads, get_cloud_workload, validate_cloud_workloads,
)


class CloudCatalogTests(unittest.TestCase):
    def test_catalog_is_populated_and_unique(self):
        rows = list_cloud_providers()
        self.assertGreaterEqual(len(rows), 35)
        self.assertEqual(len({x["id"] for x in rows}), len(rows))
        self.assertEqual(validate_cloud_catalog(), ())

    def test_bharat_and_global_providers(self):
        self.assertTrue(list_cloud_providers(origin="india"))
        self.assertTrue(list_cloud_providers(origin="global"))
        self.assertIsNotNone(get_cloud_provider("aws"))
        self.assertIsNotNone(get_cloud_provider("jio_cloud"))

    def test_catalog_does_not_claim_live_connections(self):
        self.assertTrue(all(
            x["integration_status"] == "catalog_only"
            and x["live_connection_verified"] is False
            for x in list_cloud_providers()
        ))

    def test_metadata_is_defensive_copy(self):
        item = get_cloud_provider("aws")
        item["name"] = "corrupted"
        self.assertEqual(get_cloud_provider("aws")["name"], "Amazon Web Services")

    def test_capabilities_and_scope(self):
        self.assertIn("compute", CLOUD_CAPABILITIES)
        self.assertIn("storage", CLOUD_CAPABILITIES)
        self.assertIn("bharat_india_cloud", CLOUD_SCOPES)
        self.assertIn("supreme_cloud", CLOUD_SCOPES)

    def test_workload_catalog_covers_normal_to_supreme(self):
        rows = list_cloud_workloads()
        self.assertGreaterEqual(len(rows), 25)
        self.assertEqual(
            {x["tier"] for x in rows},
            {"normal", "standard", "advanced", "supreme"},
        )
        self.assertEqual(validate_cloud_workloads(), ())

    def test_bharat_and_global_workload_coverage(self):
        self.assertTrue(list_cloud_workloads(region="bharat_india"))
        self.assertTrue(list_cloud_workloads(region="global_world"))
        self.assertIsNotNone(get_cloud_workload("agriculture_food"))
        self.assertIsNotNone(get_cloud_workload("multi_cloud_sovereign"))

    def test_lawful_adult_industry_workloads_are_included_with_safeguards(self):
        rows = list_cloud_workloads(adult_industry=True)
        self.assertGreaterEqual(len(rows), 4)
        required = {
            "adults_only_age_assurance",
            "documented_informed_consent",
            "content_and_distribution_rights_cleared",
            "block_minors_and_nonconsensual_intimate_content",
            "anti_exploitation_and_takedown_workflows",
            "privacy_security_and_legal_compliance",
        }
        for row in rows:
            if row["id"].startswith("adult_"):
                self.assertTrue(required.issubset(set(row["guardrails"])))
        self.assertIsNotNone(get_cloud_workload("adult_entertainment_streaming"))

    def test_workload_catalog_does_not_claim_live_provider_connections(self):
        self.assertTrue(all(
            x["integration_status"] == "workload_taxonomy_only"
            and x["live_provider_connection_verified"] is False
            for x in list_cloud_workloads()
        ))

    def test_workload_metadata_is_defensive_copy(self):
        item = get_cloud_workload("adult_entertainment_streaming")
        item["name"] = "corrupted"
        self.assertNotEqual(
            get_cloud_workload("adult_entertainment_streaming")["name"],
            "corrupted",
        )


if __name__ == "__main__":
    unittest.main()
