"""Read-only bridge to backend/GLOBAL_SUPREME_ECOSYSTEM_CATALOG.json."""
import json
from pathlib import Path
from .constants import MASTER_CATALOG_PATH

def master_catalog_path(): return Path(__file__).resolve().parents[5] / MASTER_CATALOG_PATH
def load_master_catalog():
    with master_catalog_path().open(encoding="utf-8") as stream: return json.load(stream)
def get_individual_master_entries():
    data=load_master_catalog()
    section=next((x for x in data.get("sections",[]) if x.get("section_id")=="human_individual_ecosystem"),{})
    return list(section.get("entries",[]))
def get_master_summary():
    data=load_master_catalog(); expansion=data.get("expansion",{})
    return {"catalogue_id":data.get("catalogue_id"),"target_unique_entries":expansion.get("target_unique_entries"),"current_unique_entries":expansion.get("current_unique_entries"),"remaining_unique_entries":expansion.get("remaining_unique_entries"),"individual_entry_count":len(get_individual_master_entries()),"read_only":True}
