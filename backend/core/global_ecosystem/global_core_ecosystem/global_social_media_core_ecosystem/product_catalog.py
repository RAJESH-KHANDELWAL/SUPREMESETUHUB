"""Validated source-of-record inventory for registered social platforms."""
import json
from copy import deepcopy
from pathlib import Path
from typing import Any
_INDEX=Path(__file__).with_name("product_ecosystem_index.json")
def get_social_media_product_index()->dict[str,Any]:
    data=json.loads(_INDEX.read_text(encoding="utf-8"));items=data.get("platform_ecosystems",[]);ids=[x.get("platform_id") for x in items]
    if len(ids)!=len(set(ids)) or any(not x for x in ids):raise ValueError("SOCIAL_MEDIA_PLATFORM_IDS_INVALID")
    if data.get("platform_count")!=len(items):raise ValueError("SOCIAL_MEDIA_PLATFORM_COUNT_MISMATCH")
    return deepcopy(data)
def list_social_media_platforms(*,domain_id:str|None=None,adult_only:bool|None=None)->list[dict[str,Any]]:
    items=get_social_media_product_index()["platform_ecosystems"]
    if domain_id is not None:items=[x for x in items if x["domain_id"]==domain_id]
    if adult_only is not None:items=[x for x in items if x["adult_only_18_plus"] is adult_only]
    return items
def get_social_media_platform(platform_id:str)->dict[str,Any]|None:
    key=platform_id.strip().casefold()
    return next((x for x in list_social_media_platforms() if x["platform_id"].casefold()==key),None) if key else None
def social_media_platform_summary()->dict[str,Any]:
    data=get_social_media_product_index();items=data["platform_ecosystems"]
    return {"ecosystem_id":data["ecosystem_id"],"platform_count":len(items),"domain_count":data["domain_count"],"adult_only_platform_count":sum(x["adult_only_18_plus"] for x in items),"live_connections_verified":False,"api_calls_performed":0}
