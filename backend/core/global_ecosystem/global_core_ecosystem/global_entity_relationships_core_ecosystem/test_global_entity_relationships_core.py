"""Contract tests for Global Entity Relationships CORE."""
import unittest
import json
from pathlib import Path
from .catalog import ROOT_ID,get_catalog,list_categories,RELATIONSHIP_TYPES
from .manager import get_manager
from backend.core.global_ecosystem.global_core_ecosystem.manager import GlobalEcosystemManager
from .policy import RelationshipPolicy,RelationshipPolicyError
class GlobalEntityRelationshipsCoreTests(unittest.TestCase):
 def test_root_name_and_id_standard(self):
  root=get_catalog()[0]; self.assertEqual(root["ecosystem_id"],ROOT_ID); self.assertTrue(root["name"].startswith("GLOBAL ")); self.assertTrue(root["name"].endswith(" CORE ECOSYSTEM"))
 def test_all_children_follow_global_subject_core_standard(self):
  children=list_categories(); self.assertEqual(len(children),36); self.assertEqual(len({x["ecosystem_id"] for x in children}),len(children))
  for item in children: self.assertTrue(item["name"].startswith("GLOBAL ")); self.assertTrue(item["name"].endswith(" CORE ECOSYSTEM")); self.assertTrue(item["ecosystem_id"].startswith("GLOBAL-")); self.assertTrue(item["ecosystem_id"].endswith("-CORE-ECOSYSTEM"))
 def test_manager_and_tree(self):
  manager=get_manager(); self.assertEqual(manager.status()["category_count"],36); self.assertTrue(manager.tree()["success"]); self.assertEqual(manager.registry.count(),37)
 def test_relationship_types_are_unique(self): self.assertEqual(len(RELATIONSHIP_TYPES),len(set(RELATIONSHIP_TYPES))); self.assertGreaterEqual(len(RELATIONSHIP_TYPES),20)
 def test_verified_claim_requires_source(self):
  item={"relationship_id":"r1","source_entity_id":"e1","target_entity_id":"e2","relationship_type":"owns","verification_status":"VERIFIED","source_urls":["https://example.com"]}; self.assertTrue(RelationshipPolicy.validate(item)); item["source_urls"]=[]
  with self.assertRaises(RelationshipPolicyError): RelationshipPolicy.validate(item)
 def test_self_edge_rejected(self):
  item={"relationship_id":"r2","source_entity_id":"e1","target_entity_id":"e1","relationship_type":"owns","verification_status":"UNVERIFIED"}
  with self.assertRaises(RelationshipPolicyError): RelationshipPolicy.validate(item)
 def test_master_module_index_and_central_registry_are_registered(self):
  backend_root=Path(__file__).resolve().parents[4]
  master=json.loads((backend_root/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json").read_text(encoding="utf-8"))
  module_id="GLOBAL-ENTITY-RELATIONSHIPS-CORE-ECOSYSTEM"
  modules=master["ecosystem_module_index"]["modules"]
  entry=next((x for x in modules if x.get("ecosystem_id")==module_id),None)
  self.assertIsNotNone(entry); self.assertEqual(entry["category_count"],36); self.assertFalse(entry["live_connection_verified"])
  central=GlobalEcosystemManager()
  self.assertTrue(central.exists(module_id))
  self.assertEqual(central.get(module_id)["parent_id"],"GLOBAL-CORE-ECOSYSTEM")
 def test_master_catalog_reference_read_only_2468(self):
  r=get_manager().master_catalog_reference(); self.assertEqual(r["target_unique_entries"],2468); self.assertEqual(r["owner_layer"],"GLOBAL_ENGINE_ECOSYSTEM"); self.assertEqual(r["access_mode"],"READ_ONLY_ON_DEMAND")
if __name__=="__main__": unittest.main()
