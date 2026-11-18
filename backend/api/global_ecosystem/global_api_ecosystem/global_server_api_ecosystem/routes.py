"""FastAPI routes for GLOBAL SERVER API ECOSYSTEM."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException, status

from .schemas import ServerInventoryCreate
from .services import router as services_router
from .integrations import router as integrations_router
from .tools import router as tools_router
from .service import (
    disable_server,
    get_server,
    get_server_provider,
    get_server_type,
    get_server_ecosystem_status,
    list_server_providers,
    list_server_types,
    list_servers,
    mark_server_authorized,
    register_server,
    list_server_artifacts,
)

router = APIRouter(prefix="/global/server", tags=["GLOBAL SERVER ECOSYSTEM"])
router.include_router(services_router)
router.include_router(integrations_router)
router.include_router(tools_router)


@router.get("/status")
def server_ecosystem_status() -> dict[str, Any]:
    return get_server_ecosystem_status()


@router.get("/providers")
def server_providers() -> dict[str, Any]:
    return list_server_providers()


@router.get("/providers/{provider_id}")
def server_provider(provider_id: str) -> dict[str, Any]:
    result = get_server_provider(provider_id)
    if result is None:
        raise HTTPException(status_code=404, detail="SERVER_PROVIDER_NOT_FOUND")
    return result


@router.get("/types")
def server_types() -> dict[str, Any]:
    return list_server_types()


@router.get("/types/{service_type_id}")
def server_type(service_type_id: str) -> dict[str, Any]:
    result = get_server_type(service_type_id)
    if result is None:
        raise HTTPException(status_code=404, detail="SERVER_TYPE_NOT_FOUND")
    return result


@router.get("/inventory")
def server_inventory() -> dict[str, Any]:
    return list_servers()


@router.get("/inventory/{server_id}")
def server_inventory_item(server_id: str) -> dict[str, Any]:
    result = get_server(server_id)
    if result is None:
        raise HTTPException(status_code=404, detail="SERVER_NOT_FOUND")
    return result


@router.post("/inventory", status_code=status.HTTP_201_CREATED)
def create_server_inventory_item(payload: ServerInventoryCreate) -> dict[str, Any]:
    result = register_server(payload.to_core_payload())
    if not result["success"]:
        raise HTTPException(status_code=422, detail=result)
    return result


@router.post("/inventory/{server_id}/authorize")
def authorize_server_inventory_item(server_id: str) -> dict[str, Any]:
    result = mark_server_authorized(server_id)
    if not result["success"]:
        raise HTTPException(status_code=404, detail="SERVER_NOT_FOUND")
    return result


@router.post("/inventory/{server_id}/disable")
def disable_server_inventory_item(server_id: str) -> dict[str, Any]:
    result = disable_server(server_id)
    if not result["success"]:
        raise HTTPException(status_code=404, detail="SERVER_NOT_FOUND")
    return result


@router.get("/inventory/{server_id}/artifacts")
def server_artifacts(server_id: str) -> dict[str, Any]:
    return list_server_artifacts(server_id)
