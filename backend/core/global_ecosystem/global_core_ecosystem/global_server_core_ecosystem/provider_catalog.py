"""Provider-neutral server provider catalog; metadata only."""
from __future__ import annotations
from copy import deepcopy
import json
from pathlib import Path
_DATA=json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
SERVER_PROVIDERS=tuple(_DATA["providers"])
def get_provider_catalog():
    return deepcopy(list(SERVER_PROVIDERS))
def get_provider(provider_id: str):
    needle=provider_id.strip().upper()
    for item in SERVER_PROVIDERS:
        if item["provider_id"]==needle: return deepcopy(item)
    return None
def provider_summary():
    return {"provider_count":len(SERVER_PROVIDERS),"provider_coverage_exhaustive":False,"live_connections_verified":False}
