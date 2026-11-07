"""Routes exposing the core and infrastructure subsystem ecosystem catalog."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException

from backend.engines.subsystem_ecosystem_catalog import (
    get_subsystem_ecosystem,
    list_subsystem_ecosystems,
)

# Keep these routes within GLOBAL API ECOSYSTEM so subsystem and vendor catalogs
# share the same API boundary without collapsing their separate responsibilities.
router = APIRouter(
    prefix="/api/v1/global-api-ecosystem/subsystems",
    tags=["GLOBAL API ECOSYSTEM", "GLOBAL SUBSYSTEM ECOSYSTEMS"],
)


@router.get("")
def global_subsystem_ecosystems():
    items = list_subsystem_ecosystems()
    return {
        "success": True,
        "system": "GLOBAL API ECOSYSTEM",
        "catalog": "GLOBAL SUBSYSTEM ECOSYSTEMS",
        "count": len(items),
        "subsystems": items,
        "note": "Catalog entries link to project code; they do not prove external services are connected or provisioned.",
    }


@router.get("/{subsystem_id}")
def global_subsystem_ecosystem(subsystem_id: str):
    item = get_subsystem_ecosystem(subsystem_id)
    if item is None:
        raise HTTPException(status_code=404, detail="SUBSYSTEM_ECOSYSTEM_NOT_FOUND")
    return {
        "success": True,
        "system": "GLOBAL API ECOSYSTEM",
        "catalog": "GLOBAL SUBSYSTEM ECOSYSTEMS",
        "subsystem": item,
    }
