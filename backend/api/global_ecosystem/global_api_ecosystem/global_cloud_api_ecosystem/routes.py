"""HTTP routes for GLOBAL CLOUD API ECOSYSTEM."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import EcosystemStatus
from .service import EcosystemService

router = APIRouter(prefix="/api/v1/global-cloud", tags=["GLOBAL CLOUD API ECOSYSTEM"])
service = EcosystemService()


@router.get("/status", response_model=EcosystemStatus)
def get_status():
    return service.get_status()


@router.get("/providers")
def list_providers():
    return service.list_providers()


@router.get("/providers/{provider_id}")
def get_provider(provider_id: str):
    provider = service.get_provider(provider_id)
    if provider is None:
        raise HTTPException(status_code=404, detail={"error": "PROVIDER_NOT_FOUND", "provider_id": provider_id})
    return {"success": True, "provider": provider}


@router.get("/search")
def search_providers(q: str = Query(min_length=1, max_length=100)):
    providers = service.search_providers(q)
    return {"success": True, "count": len(providers), "providers": providers}
