"""Provider inventory for security metadata; performs no provider API calls."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
_DATA=json.loads(Path(__file__).with_name("provider_catalog.json").read_text(encoding="utf-8"))
SECURITY_PROVIDERS=tuple(_DATA["providers"])
def get_provider_catalog():
    return deepcopy(list(SECURITY_PROVIDERS))
def get_provider(provider_id: str):
    needle=provider_id.strip().upper()
    for item in SECURITY_PROVIDERS:
        if item["provider_id"]==needle: return deepcopy(item)
    return None
def provider_summary():
    return {"provider_count":len(SECURITY_PROVIDERS),"enabled_provider_count":sum(bool(x.get("enabled")) for x in SECURITY_PROVIDERS),"coverage_exhaustive":False}
