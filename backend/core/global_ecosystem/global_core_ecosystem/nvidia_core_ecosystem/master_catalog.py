from pathlib import Path
import json
from .constants import MASTER_PATH,MASTER_TARGET
SOURCE=Path(__file__).resolve().parents[4]/"GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json"
def reference():return {"catalog_id":"GLOBAL_TO_SUPREME_MASTER_ECOSYSTEM","path":MASTER_PATH,"target_unique_entries":MASTER_TARGET,"access_mode":"READ_ONLY_ON_DEMAND","loaded":False,"copied":False,"mutated":False,"catalog_entries_added":0}
def load_metadata():
 if not SOURCE.exists():raise FileNotFoundError(SOURCE)
 d=json.loads(SOURCE.read_text(encoding="utf-8"));return {"catalog_id":d.get("catalog_id"),"expansion":d.get("expansion"),"read_only":True}
