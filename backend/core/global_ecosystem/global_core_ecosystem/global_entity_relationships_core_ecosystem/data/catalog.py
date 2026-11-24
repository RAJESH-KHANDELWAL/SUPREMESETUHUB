"""Reference data utilities for the Entity Relationships CORE ecosystem."""
from __future__ import annotations
from pathlib import Path
import json
MASTER_CATALOG_PATH=Path(__file__).resolve().parents[5]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
ROOT_ECOSYSTEM_ID="GLOBAL-ENTITY-RELATIONSHIPS-CORE-ECOSYSTEM"
MASTER_CATALOG_TARGET=2468
DATA_SCOPE="REFERENCE_METADATA_ONLY"
def catalog_reference():
 return {"ecosystem_id":ROOT_ECOSYSTEM_ID,"master_catalog_path":str(MASTER_CATALOG_PATH),"target_unique_entries":MASTER_CATALOG_TARGET,"scope":DATA_SCOPE,"loaded":False}
def load_master_catalog_metadata():
 if not MASTER_CATALOG_PATH.exists(): raise FileNotFoundError(MASTER_CATALOG_PATH)
 payload=json.loads(MASTER_CATALOG_PATH.read_text(encoding="utf-8"))
 return {"catalog_id":payload.get("catalog_id"),"expansion":payload.get("expansion"),"read_only":True}
