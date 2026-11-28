import unittest
from pathlib import Path
from ..catalog import MODULES,get_module
from ..manager import get_manager
from ..master_catalog import get_individual_master_entries,get_master_summary
from ..policy import redact_metadata,adult_safety_boundary
from ..registry import list_ids
ROOT=Path(__file__).resolve().parents[1]
class IndividualCoreTests(unittest.TestCase):
 def test_unique_inventory(self):
  ids=[x["module_id"] for x in MODULES]; self.assertEqual(len(ids),len(set(ids))); self.assertEqual(len(ids),29)
 def test_master_section_and_counts(self):
  self.assertEqual(len(get_individual_master_entries()),20); summary=get_master_summary(); self.assertEqual(summary["target_unique_entries"],2468); self.assertEqual(summary["current_unique_entries"],246)
 def test_module_mappings_exist_in_master(self):
  valid={x["entry_id"] for x in get_individual_master_entries()}
  for item in MODULES: self.assertTrue(set(item["master_entry_ids"]).issubset(valid),item["module_id"])
 def test_manager_and_registry(self):
  manager=get_manager(); self.assertEqual(manager.list_modules()["count"],29); self.assertIsNotNone(manager.get_module(MODULES[0]["module_id"])); self.assertEqual(set(list_ids()),{x["module_id"] for x in MODULES})
 def test_sensitive_values_redacted(self): self.assertEqual(redact_metadata({"token":"abc","name":"ok"}),{"token":"[REDACTED]","name":"ok"})
 def test_adult_safety(self): self.assertTrue(adult_safety_boundary()["age_assurance_required"]); self.assertTrue(adult_safety_boundary()["lawful_consenting_adults_only"])
 def test_core_is_not_live(self): self.assertEqual(get_manager().health()["api_calls"],0); self.assertFalse(get_manager().health()["connected"])
if __name__=="__main__": unittest.main()
