"""Tests for the Mistral Core Ecosystem control plane."""
from __future__ import annotations
import unittest
from pathlib import Path
from backend.core.global_ecosystem.global_core_ecosystem.mistral_core_ecosystem.catalog import get_mistral_core_catalog
from backend.core.global_ecosystem.global_core_ecosystem.mistral_core_ecosystem.contracts import TenantContext
from backend.core.global_ecosystem.global_core_ecosystem.mistral_core_ecosystem.manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.mistral_core_ecosystem.master_catalog import CANONICAL_ENTRY_IDS,MASTER_CATALOG_PATH,master_catalog_reference
from backend.core.global_ecosystem.global_core_ecosystem.mistral_core_ecosystem.module_service import MistralProductCoreService

class MistralCoreTests(unittest.TestCase):
 def test_nine_existing_product_packages_and_api_packages_are_registered(self):
  root=Path(__file__).resolve().parents[2]
  rows=get_mistral_core_catalog()["children"]
  self.assertEqual(len(rows),9)
  for row in rows:
   self.assertTrue((root/row["core_module"]).is_dir(),row["core_module"])
   self.assertTrue((root/row["api_catalog_ref"]).is_dir(),row["api_catalog_ref"])
 def test_existing_ai_provider_and_core_facade_references_resolve(self):
  root=Path(__file__).resolve().parents[2]
  catalog=get_mistral_core_catalog()
  self.assertTrue((root/catalog["ai_provider_ref"]).is_dir())
  self.assertTrue((root/catalog["ai_core_facade_ref"]).is_dir())
  self.assertIsNone(catalog["engine_ref"])
  self.assertIsNone(catalog["runtime_ref"])
  self.assertEqual(catalog["layer_availability"]["engine"],"NOT_REGISTERED")
  self.assertEqual(catalog["layer_availability"]["runtime"],"NOT_REGISTERED")
 def test_product_ids_are_unique(self):
  ids=[x["ecosystem_id"] for x in get_mistral_core_catalog()["children"]]
  self.assertEqual(len(ids),len(set(ids)))
 def test_all_eighteen_domains_have_product_coverage(self):
  rows=get_manager().list_domain_inventory()
  self.assertEqual(len(rows),18)
  self.assertTrue(all(x["product_count"]>0 for x in rows))
 def test_master_catalog_is_read_only_reference(self):
  ref=master_catalog_reference()
  self.assertEqual(ref["target_unique_entries"],2468)
  self.assertEqual(ref["canonical_entry_ids"],list(CANONICAL_ENTRY_IDS))
  self.assertEqual(ref["catalogue_entries_added"],0)
  self.assertFalse(ref["catalogue_mutated"])
  self.assertEqual(MASTER_CATALOG_PATH.name,"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json")
 def test_master_catalog_file_is_present_and_loadable(self):
  self.assertTrue(MASTER_CATALOG_PATH.is_file())
  result=get_manager().master_catalog()
  self.assertTrue(result["available"],result)
  self.assertEqual(result["status"],"MASTER_CATALOG_READ_ONLY")
  self.assertEqual(result["current_unique_entries"],246)
  self.assertEqual(result["remaining_unique_entries"],2222)
  self.assertTrue(all(result["mapped_entry_presence"].values()))
 def test_status_is_metadata_only(self):
  status=get_manager().status()
  self.assertEqual(status["module_count"],9)
  self.assertFalse(status["live_connection_verified"])
  self.assertEqual(status["api_calls_performed"],0)
 def test_policy_requires_tenant_and_registered_capability(self):
  service=MistralProductCoreService("chat")
  self.assertFalse(service.authorize_capability("CHAT_COMPLETION_METADATA",None)["success"])
  result=service.authorize_capability("CHAT_COMPLETION_METADATA",TenantContext("tenant-1","actor-1"))
  self.assertTrue(result["success"])
  self.assertFalse(result["data"]["api_call_performed"])
 def test_unknown_product_and_domain_are_rejected(self):
  with self.assertRaises(LookupError): MistralProductCoreService("unknown")
  with self.assertRaises(LookupError): get_manager().get_domain_manager("UNKNOWN_DOMAIN")
 def test_catalog_returns_defensive_copy(self):
  first=get_mistral_core_catalog()
  first["children"][0]["name"]="MUTATED"
  self.assertNotEqual(get_mistral_core_catalog()["children"][0]["name"],"MUTATED")

if __name__=="__main__": unittest.main()
