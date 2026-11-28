"""Bada Business adapter over the canonical Global Core work-model taxonomy."""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from ...global_independent_freelancer_remote_hybrid_part_time_full_time_work_from_home_gig_core_ecosystem.catalog import (
    get_work_model as get_canonical_work_model,
    list_work_models as list_canonical_work_models,
)

ECOSYSTEM_ID = "GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-SERVICE-WORK-BUSINESS-CORE-ECOSYSTEM"
ECOSYSTEM_NAME = "GLOBAL INDEPENDENT FREELANCER REMOTE HYBRID PART TIME FULL TIME WORK FROM HOME GIG SERVICE WORK BUSINESS CORE ECOSYSTEM"
PARENT_ECOSYSTEM_ID = "GLOBAL-BADA-BUSINESS-CORE-ECOSYSTEM"
CANONICAL_WORK_MODEL_OWNER = "GLOBAL-INDEPENDENT-FREELANCER-REMOTE-HYBRID-PART-TIME-FULL-TIME-WORK-FROM-HOME-GIG-CORE-ECOSYSTEM"

BUSINESS_CAPABILITIES: tuple[dict[str, str], ...] = (
    {"id": "SERVICE_WORK", "name": "Service work"},
    {"id": "SERVICE_WORK_BUSINESS", "name": "Service work business"},
)


def list_work_models() -> list[dict[str, str]]:
    """Expose canonical Global Core work models without maintaining a duplicate."""
    return list_canonical_work_models()


def get_work_model(model_id: str) -> dict[str, str] | None:
    """Look up a work model in its canonical Global Core owner."""
    return get_canonical_work_model(model_id)


def list_business_capabilities() -> list[dict[str, str]]:
    """Return this Bada Business package's owned capability classifications."""
    return deepcopy(list(BUSINESS_CAPABILITIES))


def get_catalog() -> dict[str, Any]:
    work_models = list_work_models()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID,
        "status": "CORE_CATALOG_ONLY",
        "canonical_work_model_owner": CANONICAL_WORK_MODEL_OWNER,
        "work_models": work_models,
        "work_model_count": len(work_models),
        "business_capabilities": list_business_capabilities(),
        "business_capability_count": len(BUSINESS_CAPABILITIES),
        "live_jobs_verified": False,
        "provider_connections_enabled": False,
    }
