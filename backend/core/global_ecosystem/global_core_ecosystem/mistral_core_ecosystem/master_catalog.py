"""Read-only mapping to the canonical 2468-target master ecosystem catalog."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any

MASTER_CATALOG_PATH=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_RELATIVE_PATH="backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
MASTER_CATALOG_ID="GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM"
MASTER_CATALOG_TARGET=2468
CANONICAL_ENTRY_IDS=("S09_artificial_intelligence","S09_machine_learning")

def master_catalog_reference()->dict[str,Any]:
 return {"catalogue_id":MASTER_CATALOG_ID,"source_path":MASTER_CATALOG_RELATIVE_PATH,
  "target_unique_entries":MASTER_CATALOG_TARGET,"canonical_entry_ids":list(CANONICAL_ENTRY_IDS),
  "access_mode":"READ_ONLY_ON_DEMAND","catalogue_entries_added":0,"catalogue_mutated":False}

def load_master_catalog_summary()->dict[str,Any]:
 if not MASTER_CATALOG_PATH.is_file():
  return {**master_catalog_reference(),"available":False,"status":"MASTER_CATALOG_NOT_FOUND"}
 try: payload=json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError):
  return {**master_catalog_reference(),"available":False,"status":"MASTER_CATALOG_INVALID"}
 if payload.get("catalogue_id")!=MASTER_CATALOG_ID:
  return {**master_catalog_reference(),"available":False,"status":"MASTER_CATALOG_ID_MISMATCH"}
 expansion=payload.get("expansion",{})
 present={entry.get("entry_id") for section in payload.get("sections",[]) for entry in section.get("entries",[])}
 return {**master_catalog_reference(),"available":True,"status":"MASTER_CATALOG_READ_ONLY",
  "schema_version":payload.get("schema_version"),
  "current_unique_entries":expansion.get("current_unique_entries"),
  "remaining_unique_entries":expansion.get("remaining_unique_entries"),
  "mapped_entry_presence":{entry_id:entry_id in present for entry_id in CANONICAL_ENTRY_IDS}}

__all__=["MASTER_CATALOG_PATH","MASTER_CATALOG_RELATIVE_PATH","MASTER_CATALOG_ID",
 "MASTER_CATALOG_TARGET","CANONICAL_ENTRY_IDS","master_catalog_reference","load_master_catalog_summary"]
