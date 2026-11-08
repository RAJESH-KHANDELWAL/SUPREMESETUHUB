"""Offline tests for STORAGE taxonomy, hierarchy and metadata."""
import unittest
from .catalog import ROOT_ID,get_catalog,get_provider_catalog,get_category_catalog
from .manager import GlobalStorageEcosystemManager
from .models import StorageObject,StorageEcosystemIdentity
from .ecosystem_registry import StorageEcosystemRegistry
class StorageTests(unittest.TestCase):
 def test_parent_first_unique_catalog(self):
  rows=get_catalog(); ids=[x["ecosystem_id"] for x in rows]; self.assertEqual(len(ids),len(set(ids))); seen=set()
  for x in rows:
   self.assertTrue(x.get("parent_id") is None or x["parent_id"] in seen); seen.add(x["ecosystem_id"])
  self.assertEqual(rows[0]["ecosystem_id"],ROOT_ID)
 def test_full_taxonomy_counts(self):
  self.assertGreaterEqual(len(get_provider_catalog()),30); self.assertGreaterEqual(len(get_category_catalog()),20)
 def test_manager_tree_and_edges(self):
  m=GlobalStorageEcosystemManager(); s=m.status(); self.assertTrue(s["success"]); self.assertEqual(s["count"],len(get_catalog())); self.assertEqual(m.tree()["tree"]["ecosystem_id"],ROOT_ID); self.assertEqual(m.connection_map()["edge_count"],s["count"]-1)
 def test_registry_parent_and_duplicate_guards(self):
  r=StorageEcosystemRegistry()
  with self.assertRaises(ValueError): r.register(StorageEcosystemIdentity("child","Child",parent_id="missing"))
  r.register(StorageEcosystemIdentity("root","Root"))
  with self.assertRaises(ValueError): r.register(StorageEcosystemIdentity("root","Duplicate"))
 def test_object_validation(self):
  with self.assertRaises(ValueError): StorageObject("id","provider","bucket","",size_bytes=1)
  with self.assertRaises(ValueError): StorageObject("id","provider","bucket","key",size_bytes=-1)
if __name__=="__main__": unittest.main()
