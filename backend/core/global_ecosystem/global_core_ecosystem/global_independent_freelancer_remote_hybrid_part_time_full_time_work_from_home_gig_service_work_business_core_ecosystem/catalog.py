"""GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG SERVICE WORK BUSINESS CORE ECOSYSTEM catalogue and manager foundation."""
from __future__ import annotations
from copy import deepcopy
from typing import Any

ECOSYSTEM_ID = "GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG SERVICE WORK BUSINESS CORE ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
WORK_MODELS: tuple[dict[str, str], ...] = (
    {"id": "FREELANCER", "name": "Independent contract-based work"},
    {"id": "REMOTE", "name": "Work performed remotely"},
    {"id": "HYBRID", "name": "Combination of remote and on-site work"},
    {"id": "PART_TIME", "name": "Part-time engagement"},
    {"id": "FULL_TIME", "name": "Full-time engagement"},
    {"id": "WORK_FROM_HOME", "name": "Work performed from home"},
    {"id": "GIG", "name": "Task-based or short-term independent work"},
)

def list_work_models() -> list[dict[str, str]]:
    """Return a copy of the canonical work-model catalogue."""
    return deepcopy(list(WORK_MODELS))

def get_work_model(model_id: str) -> dict[str, str] | None:
    key = model_id.strip().upper()
    for item in WORK_MODELS:
        if item["id"] == key:
            return dict(item)
    return None

def get_catalog() -> dict[str, Any]:
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID,
        "status": "CORE_CATALOG_ONLY",
        "work_models": list_work_models(),
        "work_model_count": len(WORK_MODELS),
        "live_jobs_verified": False,
        "provider_connections_enabled": False,
    }
