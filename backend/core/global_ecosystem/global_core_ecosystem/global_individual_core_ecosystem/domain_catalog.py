from .catalog import MODULES
from .master_catalog import get_individual_master_entries

def domain_inventory():
    master={x["entry_id"]:x for x in get_individual_master_entries()}
    return [{"module_id":m["module_id"],"name":m["name"],"master_entries":[master[x] for x in m["master_entry_ids"] if x in master]} for m in MODULES]
def domain_summary():
    entries=get_individual_master_entries(); mapped={x for m in MODULES for x in m["master_entry_ids"]}
    return {"master_entry_count":len(entries),"mapped_count":sum(e["entry_id"] in mapped for e in entries),"unmapped_entry_ids":[e["entry_id"] for e in entries if e["entry_id"] not in mapped]}
