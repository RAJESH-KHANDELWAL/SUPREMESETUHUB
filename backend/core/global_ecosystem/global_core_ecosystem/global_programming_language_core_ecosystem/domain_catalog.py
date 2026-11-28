"""Canonical programming-language domain taxonomy loaded from catalog.json."""
from __future__ import annotations
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

_DATA = json.loads(Path(__file__).with_name("catalog.json").read_text(encoding="utf-8"))
PROGRAMMING_LANGUAGE_DOMAINS = tuple({
    **item, "division": "PROGRAMMING", "status": "CORE_CATALOG_ONLY"
} for item in _DATA["domains"])
DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    item["id"]: {"name": item["name"], "purpose": item["scope"]}
    for item in PROGRAMMING_LANGUAGE_DOMAINS
}

def list_programming_language_domains(division: str | None = None) -> list[dict[str, Any]]:
    if division is not None and division.strip().upper() not in {"PROGRAMMING", "PROGRAMMING-LANGUAGES"}:
        return []
    return deepcopy(list(PROGRAMMING_LANGUAGE_DOMAINS))

def get_programming_language_domain(domain_id: str) -> dict[str, Any] | None:
    needle = domain_id.strip().upper()
    return next((deepcopy(x) for x in PROGRAMMING_LANGUAGE_DOMAINS if x["id"] == needle), None)

def programming_language_domain_summary() -> dict[str, Any]:
    counts = Counter(item["division"] for item in PROGRAMMING_LANGUAGE_DOMAINS)
    return {"domain_count": len(PROGRAMMING_LANGUAGE_DOMAINS), "division_counts": dict(counts), "coverage_exhaustive": False}

get_domains = list_programming_language_domains
get_domain = get_programming_language_domain
