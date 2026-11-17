"""Canonical people-life domain taxonomy loaded from catalog.json."""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

_DATA = json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
PEOPLE_LIFE_DOMAINS = tuple({**item, "division":"PEOPLE_LIFE", "status":"CORE_CATALOG_ONLY"} for item in _DATA["domains"])
DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {x["id"]: {"name":x["name"],"purpose":x["scope"]} for x in PEOPLE_LIFE_DOMAINS}

def list_people_life_domains(division: str | None = None) -> list[dict[str, Any]]:
    if division is not None and division.strip().upper() not in {"PEOPLE_LIFE","PEOPLE-LIFE"}:
        return []
    return deepcopy(list(PEOPLE_LIFE_DOMAINS))

def get_people_life_domain(domain_id: str) -> dict[str, Any] | None:
    needle=domain_id.strip().upper()
    return next((deepcopy(x) for x in PEOPLE_LIFE_DOMAINS if x["id"]==needle),None)

def people_life_domain_summary() -> dict[str, Any]:
    counts=Counter("AGE_RESTRICTED" if x.get("age_restricted") else "GENERAL" for x in PEOPLE_LIFE_DOMAINS)
    return {"domain_count":len(PEOPLE_LIFE_DOMAINS),"age_restricted_domain_count":counts["AGE_RESTRICTED"],"general_domain_count":counts["GENERAL"],"coverage_exhaustive":False}

get_domains=list_people_life_domains
get_domain=get_people_life_domain
