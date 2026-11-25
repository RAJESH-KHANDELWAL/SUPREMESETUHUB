"""Read-only API endpoints for infrastructure catalog and model contracts."""
from __future__ import annotations
from typing import Any
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from backend.engine.global_ecosystem.global_engine_ecosystem.global_infrastructure_engine_ecosystem import get_infrastructure_engine
from backend.infrastructure.global_ecosystem.global_infrastructure_ecosystem import GlobalInfrastructureEcosystemService

router = APIRouter(prefix="/infrastructure", tags=["GLOBAL INFRASTRUCTURE API ECOSYSTEM"])
_ecosystem = GlobalInfrastructureEcosystemService()
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
            "core": "NOT_REGISTERED; legacy CORE package intentionally absent",
            "engine": _engine.status()["state"],
            "database": "CANONICAL_OWNER_BACKEND_DATABASE_SERVICE; GLOBAL CATALOG IS READ_ONLY",
            "storage": "CANONICAL_OWNER_BACKEND_STORAGE_SERVICE; ARTIFACT ADAPTER NOT ENABLED",
        },
        "provider_connections_verified": False,
        "provider_operations_enabled": False,
    }

@router.get("/catalog")
def infrastructure_catalog() -> dict[str, Any]:
    return {"success": True, "catalog": _ecosystem.get_catalog(), "modules": _ecosystem.get_modules()}

@router.get("/models")
def infrastructure_models() -> dict[str, Any]:
    return {"success": True, "models": [], "status": "MODEL_CATALOG_NOT_REGISTERED"}

@router.post("/validate-resource")
def validate_infrastructure_resource(payload: ResourceValidationRequest) -> dict[str, Any]:
    raise HTTPException(
        status_code=503,
        detail={
            "success": False,
            "status": "CORE_VALIDATION_UNAVAILABLE",
            "message": "The legacy Infrastructure CORE is intentionally absent; resource validation is not enabled in this API.",
            "resource_id": payload.resource_id,
        },
    )
