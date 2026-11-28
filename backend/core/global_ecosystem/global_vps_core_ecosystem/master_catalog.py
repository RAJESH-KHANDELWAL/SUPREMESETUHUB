"""Read-only VPS mapping to verified master taxonomy IDs."""
import json
from pathlib import Path
from typing import Any
MASTER_CATALOG_PATH=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_ENTRY_IDS=("S09_cloud_computing","S10_global_server")
def get_master_catalog_mapping()->dict[str,Any]:
 if not MASTER_CATALOG_PATH.exists():return {"success":False,"status":"MASTER_CATALOG_NOT_FOUND","entries":[]}
 data=json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"));found=[]
 for section in data.get("sections",[]):
  for entry in section.get("entries",[]):
   if entry.get("entry_id") in MASTER_ENTRY_IDS:found.append({"section_id":section.get("section_id"),**entry})
 return {"success":set(MASTER_ENTRY_IDS).issubset({e.get("entry_id") for e in found}),"status":"READ_ONLY_MAPPING","target_unique_entries":data.get("expansion",{}).get("target_unique_entries"),"taxonomy_entries_added":0,"entries":found}
