"""Canonical domain taxonomy for human languages; no provider calls or execution."""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from typing import Any

from .constants import STATUS

_DATA_PATH = Path(__file__).with_name("catalog.json")
_DATA = json.loads(_DATA_PATH.read_text(encoding="utf-8"))
DOMAIN_DEFINITIONS: dict[str, dict[str, Any]] = {
    item["id"]: {"name": item["name"], "purpose": item["scope"]}
    for item in _DATA["domains"]
}
HUMAN_LANGUAGE_DOMAINS = tuple(
    {
        **item,
        "division": "HUMAN",
        "status": STATUS,
        "consent_required": bool(item.get("age_restricted", False)),
    }
    for item in _DATA["domains"]
)


def list_human_language_domains(division: str | None = None) -> list[dict[str, Any]]:
    if division is not None and division.strip().upper() not in {"HUMAN", "HUMAN-LANGUAGES"}:
        return []
    return deepcopy(list(HUMAN_LANGUAGE_DOMAINS))


def get_human_language_domain(domain_id: str) -> dict[str, Any] | None:
    needle = domain_id.strip().upper()
    for item in HUMAN_LANGUAGE_DOMAINS:
        if item["id"] == needle:
            return deepcopy(item)
    return None


def human_language_domain_summary() -> dict[str, Any]:
    counts = Counter("AGE_RESTRICTED" if item["age_restricted"] else "GENERAL" for item in HUMAN_LANGUAGE_DOMAINS)
    return {
        "domain_count": len(HUMAN_LANGUAGE_DOMAINS),
        "age_restricted_domain_count": counts["AGE_RESTRICTED"],
        "general_domain_count": counts["GENERAL"],
        "coverage_exhaustive": False,
    }


# Backward-compatible function names used by the original CORE facade.
get_domains = list_human_language_domains
get_domain = get_human_language_domain
