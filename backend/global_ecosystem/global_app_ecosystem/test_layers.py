"""Cross-layer smoke tests for GLOBAL APP catalog boundaries."""
import unittest
from backend.api.global_ecosystem.global_api_ecosystem.global_app_api_ecosystem.service import EcosystemService as ApiService
from backend.core.global_ecosystem.global_core_ecosystem.global_app_core_ecosystem import GlobalAppCoreService
from backend.engine.global_ecosystem.global_engine_ecosystem.global_app_engine_ecosystem.provider_engine import AppProviderEngine
from backend.database.global_ecosystem.global_database_ecosystem.global_app_database_ecosystem import AppProviderRecord
class GlobalAppLayerTests(unittest.TestCase):
 def test_api_reads_canonical_catalog(self):
  service=ApiService();status=service.get_status()
  self.assertGreaterEqual(status["provider_count"],70)
  self.assertFalse(status["live_connection_verified"])
  self.assertEqual(service.get_provider("zoho")["name"],"Zoho")
  self.assertEqual(len(service.search_providers("WhatsApp")),1)
 def test_core_validates_catalog_without_executing(self):
  service=GlobalAppCoreService()
  self.assertEqual(service.resolve_provider("google")["name"],"Google")
  self.assertEqual(service.validate_app_type("web_app")["id"],"web_app")
  self.assertEqual(service.catalog_snapshot()["layer"],"CORE")
  with self.assertRaises(KeyError):service.resolve_provider("not-a-provider")
 def test_engine_requires_explicit_handler(self):
  engine=AppProviderEngine("google")
  self.assertEqual(engine.status()["status"],"NOT_CONFIGURED")
  with self.assertRaises(RuntimeError):engine.execute("launch")
  configured=AppProviderEngine("google",lambda operation,payload:{"operation":operation,"payload":payload})
  self.assertEqual(configured.execute("open",{"app":"gmail"})["result"]["operation"],"open")
 def test_database_record_contract(self):
  row=AppProviderRecord("google","Google","platform_vendor","global","consumer_enterprise")
  self.assertEqual(row.provider_id,"google")
  with self.assertRaises(ValueError):AppProviderRecord("","","","","")
if __name__=="__main__":unittest.main()
