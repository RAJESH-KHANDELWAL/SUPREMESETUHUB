from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from backend.integrations.connectors.manager import ConnectorManager
from backend.integrations.connectors.registry import connector_registry


router = APIRouter(
    prefix="/api/v1/connectors",
    tags=["External Connectors"],
)


connector_manager = ConnectorManager(
    registry=connector_registry
)


@router.get("/status")
def connector_status():
    """
    Return the current connector architecture status.
    """
    return connector_manager.status()


@router.get("/")
def list_connectors(
    category: str | None = Query(
        default=None
    ),
):
    """
    List registered external connectors.
    """

    return {
        "success": True,
        "category": category,
        "connectors": connector_manager.list_connectors(
            category=category
        ),
    }


@router.get("/{name}")
def connector_details(
    name: str,
):
    """
    Return details for one registered connector.
    """

    try:
        connector = connector_registry.get(name)

    except ValueError as exc:
        raise HTTPException(
            status_code=404,
            detail=str(exc),
        ) from exc

    data = connector.public_info()

    data["adapter"] = (
        "READY"
        if connector_manager.has_adapter(name)
        else "NOT_CONFIGURED"
    )

    return {
        "success": True,
        "connector": data,
    }
