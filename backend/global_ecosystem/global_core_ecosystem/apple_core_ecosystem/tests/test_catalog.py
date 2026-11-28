"""Apple Core inventory and package structure tests."""
import json
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.catalog import get_apple_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.product_catalog import list_apple_offerings
from backend.core.global_ecosystem.global_core_ecosystem.apple_core_ecosystem.domain_catalog import apple_domain_summary
ROOT=Path(__file__).resolve().parents[1]
FAMILIES=["apple_app_store_connect_core_ecosystem","apple_app_store_server_core_ecosystem","apple_device_management_core_ecosystem","apple_icloud_cloudkit_core_ecosystem","apple_pay_core_ecosystem","apple_push_notification_core_ecosystem","apple_sign_in_with_apple_core_ecosystem","apple_storekit_core_ecosystem"]
STANDARD_DIRS=["authentication","capabilities","docs","events","lifecycle","models","schemas","security","services","tests"]
class TestAppleCoreCatalog(unittest.TestCase):
 def test_provider_inventory(self):
  c=get_apple_core_catalog(); self.assertEqual(c["provider"],"apple"); self.assertEqual(len(c["children"]),8); self.assertEqual(len(list_apple_offerings()),8)
  self.assertTrue(all(x["api_available"] is None for x in list_apple_offerings())); self.assertTrue(all(x["live_connection_verified"] is False for x in list_apple_offerings()))
 def test_domains(self):
  d=apple_domain_summary(); self.assertEqual(d["domain_count"],6); self.assertEqual(d["offering_count"],8); self.assertEqual(d["live_connections_verified"],0)
 def test_package_structure(self):
  for family in FAMILIES:
   package=ROOT/family; self.assertTrue(package.is_dir(),family)
   for folder in STANDARD_DIRS:self.assertTrue((package/folder).is_dir(),f"{family}/{folder}")
   manifest=json.loads((package/"ecosystem_manifest.json").read_text(encoding="utf-8")); self.assertEqual(manifest["provider"],"apple")
   compile((package/"ecosystem_config.py").read_text(encoding="utf-8"),str(package/"ecosystem_config.py"),"exec")
if __name__=="__main__":unittest.main()
