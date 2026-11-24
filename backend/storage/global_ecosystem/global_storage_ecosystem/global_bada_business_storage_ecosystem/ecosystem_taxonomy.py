"""GLOBAL BADA BUSINESS grouped taxonomy loader."""
import json
from pathlib import Path
TAXONOMY_PATH=Path(__file__).resolve().parent/"taxonomy"/"global_bada_business_storage_taxonomy.json"
def load_taxonomy()->dict:
 with TAXONOMY_PATH.open("r",encoding="utf-8") as f:data=json.load(f)
 if data.get("ecosystem_id")!="GLOBAL_BADA_BUSINESS_STORAGE_ECOSYSTEM":raise ValueError("Unexpected ecosystem taxonomy")
 return data
def list_ecosystems()->list[dict]:
 return [{"ecosystem_id":x["ecosystem_id"],"category":x["group"],"folder":x["folder"],"status":"CATALOG_ONLY"} for x in load_taxonomy()["groups"]]
def find_ecosystem(value:str)->dict|None:
 needle=value.strip().upper()
 return next((x for x in list_ecosystems() if x["ecosystem_id"]==needle or x["category"]==needle or x["folder"].upper()==needle),None)
