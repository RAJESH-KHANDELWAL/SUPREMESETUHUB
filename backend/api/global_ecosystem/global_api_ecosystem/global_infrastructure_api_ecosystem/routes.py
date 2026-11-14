"""Read-only API endpoints for infrastructure catalog and model contracts."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from backend.core.global_ecosystem.global_core_ecosystem.global_infrastructure_core_ecosystem import (
    GlobalInfrastructureCoreService,
)
from backend.engine.global_ecosystem.global_engine_ecosystem.global_infrastructure_engine_ecosystem import (
    get_infrastructure_engine,
)
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import (
    GlobalInfrastructureEcosystemService,
)
from backend.infrastructure.global_models.global_infrastructure_models import (
    get_model_catalog,
)

router = APIRouter(
    prefix="/infrastructure",
    tags=["GLOBAL INFRASTRUCTURE API ECOSYSTEM"],
)

_ecosystem = GlobalInfrastructureEcosystemService()
_core = GlobalInfrastructureCoreService()
_engine = get_infrastructure_engine()


class ResourceValidationRequest(BaseModel):
    resource_id: str
    resource_type: str
    category: str
    metadata: dict[str, Any] = Field(default_factory=dict)

    class Config:
        extra = "forbid"


@router.get("/status")
def infrastructure_status() -> dict[str, Any]:
    overview = _ecosystem.get_overview()
    return {
        "success": True,
        "ecosystem": "GLOBAL INFRASTRUCTURE API ECOSYSTEM",
        "overview": overview,
        "layers": {
            "api": "ROUTES_REGISTERED",
            "core": _core.describe()["status"],
            "engine": _engine.status()["state"],
            "database": "EXISTING_BACKEND_DATABASE_SERVICE; NO NEW DATABASE CREATED",
            "storage": "EXISTING_BACKEND_STORAGE_SERVICE; NO NEW STORAGE CREATED",
        },
        "provider_connections_verified": False,
        "provider_operations_enabled": False,
    }


@router.get("/catalog")
def infrastructure_catalog() -> dict[str, Any]:
    return {
        "success": True,
        "catalog": _ecosystem.get_catalog(),
        "modules": _ecosystem.get_modules(),
    }


@router.get("/models")
def infrastructure_models() -> dict[str, Any]:
    return {"success": True, "models": get_model_catalog()}


@router.post("/validate-resource")
def validate_infrastructure_resource(
    payload: ResourceValidationRequest,
) -> dict[str, Any]:
    result = _core.validate_resource(payload.dict())
    if not result.get("success"):
        raise HTTPException(status_code=422, detail=result)
    return result
