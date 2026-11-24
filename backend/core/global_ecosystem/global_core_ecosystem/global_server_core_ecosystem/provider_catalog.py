"""Canonical provider metadata inventory for Server Core."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
_DATA=json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
SERVER_PROVIDERS=tuple(_DATA.get("providers",[]))
def get_provider_catalog():
    return deepcopy(list(SERVER_PROVIDERS))
def get_provider(provider_id: str):
    needle=str(provider_id).strip().upper()
    if not needle: return None
    for item in SERVER_PROVIDERS:
        if str(item.get("provider_id","")).upper()==needle: return deepcopy(item)
    return None
def provider_summary():
    return {"provider_count":len(SERVER_PROVIDERS),
            "provider_coverage_exhaustive":bool(_DATA.get("provider_coverage_exhaustive",False)),
            "live_provider_connections_verified":0}
def list_provider_inventory():
    return get_provider_catalog()
