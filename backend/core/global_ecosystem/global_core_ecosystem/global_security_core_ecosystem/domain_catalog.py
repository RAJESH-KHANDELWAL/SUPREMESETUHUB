"""Canonical security domain taxonomy."""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
_DATA=json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
SECURITY_DOMAINS=tuple({**item,"status":"CORE_CATALOG_ONLY"} for item in _DATA["domains"])
def get_domains():
    return deepcopy(list(SECURITY_DOMAINS))
def get_domain(domain_id: str):
    needle=domain_id.strip().upper()
    for item in SECURITY_DOMAINS:
        if item["id"]==needle: return deepcopy(item)
    return None
def domain_summary():
    return {"domain_count":len(SECURITY_DOMAINS),"coverage_exhaustive":False}
