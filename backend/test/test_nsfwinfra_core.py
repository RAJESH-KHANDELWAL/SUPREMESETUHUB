"""NSFWinfra Core control-plane tests; no provider network calls."""
from __future__ import annotations
import json,unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.catalog import get_nsfwinfra_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.contracts import TenantContext
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.master_catalog import MASTER_CATALOG_PATH,CANONICAL_ENTRY_IDS,master_catalog_reference
from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.module_service import NSFWinfraProductCoreService
class NSFWinfraCoreTests(unittest.TestCase):
 def test_ten_existing_products_and_api_refs_exist(self):
  repo=Path(__file__).resolve().parents[2];items=get_nsfwinfra_core_catalog()["children"]
  self.assertEqual(len(items),10)
  for item in items:
   self.assertTrue((repo/item["core_module"]).is_dir(),item["core_module"])
   self.assertTrue((repo/item["api_catalog_ref"]).is_dir(),item["api_catalog_ref"])
 def test_ai_layer_refs_resolve(self):
  repo=Path(__file__).resolve().parents[2];c=get_nsfwinfra_core_catalog()
  for k in ("ai_api_ref","ai_core_ref","ai_provider_ref"):self.assertTrue((repo/c[k]).is_dir(),c[k])
 def test_unique_product_ids_and_coverage(self):
  items=get_nsfwinfra_core_catalog()["children"];ids=[x["ecosystem_id"] for x in items]
  self.assertEqual(len(ids),len(set(ids)))
  inventory=get_manager().list_domain_inventory()
  self.assertGreaterEqual(len(inventory),20)
  self.assertTrue(all(x["product_count"]>0 for x in inventory))
 def test_master_catalog_is_read_only_and_topics_exist(self):
  ref=master_catalog_reference()
  self.assertEqual(ref["target_unique_entries"],2468);self.assertEqual(ref["current_unique_entries"],246);self.assertEqual(ref["remaining_unique_entries"],2222)
  self.assertEqual(ref["canonical_entry_ids"],list(CANONICAL_ENTRY_IDS));self.assertFalse(ref["catalogue_mutated"])
  self.assertTrue(MASTER_CATALOG_PATH.exists())
  self.assertTrue(all(ref["mapped_entry_presence"].values()))
 def test_catalog_status_is_not_live(self):
  s=get_manager().status();self.assertEqual(s["product_count"],10);self.assertFalse(s["live_connection_verified"]);self.assertEqual(s["api_calls_performed"],0)
 def test_tenant_context_and_capability_policy(self):
  s=NSFWInfraProductCoreService("NSFW-IMAGE-GENERATION-CORE-ECOSYSTEM")
  self.assertFalse(s.authorize_capability("IMAGE_GENERATION_CAPABILITY_DISCOVERY",None)["success"])
  self.assertTrue(s.authorize_capability("IMAGE_GENERATION_CAPABILITY_DISCOVERY",TenantContext("t1","a1"))["success"])
  self.assertFalse(s.authorize_capability("UNKNOWN_CAPABILITY",TenantContext("t1","a1"))["success"])
 def test_unknown_product_and_domain_rejected(self):
  with self.assertRaises(LookupError):NSFWInfraProductCoreService("not-a-product")
  with self.assertRaises(LookupError):get_manager().get_domain_manager("NO_DOMAIN")
 def test_catalog_defensive_copy(self):
  c=get_nsfwinfra_core_catalog();c["children"][0]["name"]="corrupt"
  self.assertNotEqual(get_nsfwinfra_core_catalog()["children"][0]["name"],"corrupt")
 def test_age_policy_is_default_deny(self):
  from backend.core.global_ecosystem.global_core_ecosystem.nsfwinfra_core_ecosystem.policy import NSFWinfraCorePolicy
  p=NSFWinfraCorePolicy.age_and_content_policy()
  self.assertEqual(p["default_adult_access"],"DENY");self.assertFalse(p["execution_performed"])
if __name__=="__main__":unittest.main()
