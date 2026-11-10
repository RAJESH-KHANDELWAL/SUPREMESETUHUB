"""Offline integrity tests for the cloud provider catalog."""
import unittest
from backend.global_ecosystem.global_cloud_ecosystem import list_cloud_providers,get_cloud_provider,validate_cloud_catalog,CLOUD_CAPABILITIES,CLOUD_SCOPES
class CloudCatalogTests(unittest.TestCase):
    def test_catalog_is_populated_and_unique(self):
        rows=list_cloud_providers();self.assertGreaterEqual(len(rows),35)
        self.assertEqual(len({x["id"] for x in rows}),len(rows));self.assertEqual(validate_cloud_catalog(),())
    def test_bharat_and_global_providers(self):
        self.assertTrue(list_cloud_providers(origin="india"));self.assertTrue(list_cloud_providers(origin="global"))
        self.assertIsNotNone(get_cloud_provider("aws"));self.assertIsNotNone(get_cloud_provider("jio_cloud"))
    def test_catalog_does_not_claim_live_connections(self):
        self.assertTrue(all(x["integration_status"]=="catalog_only" and x["live_connection_verified"] is False for x in list_cloud_providers()))
    def test_metadata_is_defensive_copy(self):
        item=get_cloud_provider("aws");item["name"]="corrupted"
        self.assertEqual(get_cloud_provider("aws")["name"],"Amazon Web Services")
    def test_capabilities_and_scope(self):
        self.assertIn("compute",CLOUD_CAPABILITIES);self.assertIn("storage",CLOUD_CAPABILITIES)
        self.assertIn("bharat_india_cloud",CLOUD_SCOPES);self.assertIn("supreme_cloud",CLOUD_SCOPES)
if __name__=="__main__":unittest.main()
