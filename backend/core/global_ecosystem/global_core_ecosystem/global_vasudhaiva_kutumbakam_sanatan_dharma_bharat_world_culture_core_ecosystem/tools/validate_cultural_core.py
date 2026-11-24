"""Validate cultural Core inventory, source references and domain packages."""
import json
from pathlib import Path
from ..domain_catalog import DOMAIN_DEFINITIONS,PILLARS

def validate():
    root=Path(__file__).resolve().parents[1]
    manifest=json.loads((root/"ecosystem_manifest.json").read_text(encoding="utf-8"))
    index=json.loads((root/"resource_ecosystem_index.json").read_text(encoding="utf-8"))
    ids=list(DOMAIN_DEFINITIONS); errors=[]
    if len(ids)!=13 or len(set(ids))!=len(ids): errors.append("DOMAIN_REGISTRY_INVALID")
    if len(PILLARS)!=4: errors.append("PILLAR_COUNT_INVALID")
    if manifest.get("domain_count")!=len(ids): errors.append("MANIFEST_DOMAIN_COUNT_MISMATCH")
    if manifest.get("pillar_count")!=len(PILLARS): errors.append("MANIFEST_PILLAR_COUNT_MISMATCH")
    if {x.get("domain_id") for x in index.get("domain_families",[])}!=set(ids): errors.append("RESOURCE_INDEX_DOMAIN_SET_MISMATCH")
    if index.get("resource_count") is not None: errors.append("UNVERIFIED_RESOURCE_COUNT_MUST_REMAIN_NULL")
    for domain_id,item in DOMAIN_DEFINITIONS.items():
        package=root/item["package_name"]
        if not (package/"__init__.py").is_file(): errors.append(f"MISSING_DOMAIN_INIT:{domain_id}")
        if not (package/"manager.py").is_file(): errors.append(f"MISSING_DOMAIN_MANAGER:{domain_id}")
    return {"success":not errors,"pillar_count":len(PILLARS),"domain_count":len(ids),"resource_count":index.get("resource_count"),"errors":errors}
if __name__=="__main__":
    import sys
    result=validate(); print(json.dumps(result,indent=2)); sys.exit(0 if result["success"] else 1)
