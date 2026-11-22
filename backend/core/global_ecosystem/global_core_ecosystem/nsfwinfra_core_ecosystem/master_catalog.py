"""Read-only references to the shared 2468 master ecosystem catalog."""
from __future__ import annotations
import json
from pathlib import Path
MASTER_CATALOG_PATH=Path(__file__).resolve().parents[5]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
CANONICAL_ENTRY_IDS=("S09_cloud_computing","S10_global_infrastructure","S10_global_ai_core","S12_ai_research")
def master_catalog_reference()->dict:
 try:
  data=json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
  expansion=data.get("expansion",{})
  present={entry: any(entry==e.get("entry_id") for section in data.get("sections",[]) for e in section.get("entries",[])) for entry in CANONICAL_ENTRY_IDS}
  return {"available":True,"catalogue_id":data.get("catalogue_id"),"source_path":"backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json","target_unique_entries":expansion.get("target_unique_entries"),"current_unique_entries":expansion.get("current_unique_entries"),"remaining_unique_entries":expansion.get("remaining_unique_entries"),"canonical_entry_ids":list(CANONICAL_ENTRY_IDS),"mapped_entry_presence":present,"access_mode":"READ_ONLY","catalogue_mutated":False,"catalogue_entries_added":0}
 except (OSError,ValueError) as exc:
  return {"available":False,"source_path":"backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json","status":"MASTER_CATALOG_UNAVAILABLE","error_type":type(exc).__name__,"access_mode":"READ_ONLY","catalogue_mutated":False}
