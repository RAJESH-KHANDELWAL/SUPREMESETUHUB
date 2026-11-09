"""HTTP routes for the GLOBAL AI catalogue and contracts."""
from fastapi import APIRouter, HTTPException, Query

from .schemas import EcosystemStatus
from .service import EcosystemService

router = APIRouter(prefix="/ai", tags=["GLOBAL AI API ECOSYSTEM"])
service = EcosystemService()


@router.get("/status", response_model=EcosystemStatus)
def get_status():
    return service.get_status()


@router.get("/providers")
def list_providers():
    items = service.list_providers()
    return {"success": True, "count": len(items), "providers": items}


@router.get("/providers/{provider_id}")
def get_provider(provider_id: str):
    item = service.get_provider(provider_id)
    if item is None:
        raise HTTPException(status_code=404, detail={"error": "PROVIDER_NOT_FOUND", "provider_id": provider_id})
    return {"success": True, "provider": item}


@router.get("/search")
def search_catalog(q: str = Query(min_length=1, max_length=100)):
    term = q.strip().casefold()
    providers = service.search_providers(term)
    capabilities = [item for item in service.list_capabilities() if term in item["capability_id"] or term in item["name"].casefold()]
    return {"success": True, "query": q, "providers": providers, "capabilities": capabilities}


@router.get("/capabilities")
def list_capabilities():
    items = service.list_capabilities()
    return {"success": True, "count": len(items), "items": items}


@router.get("/models")
def list_models():
    return {"success": True, **service.get_models()}


@router.get("/architecture")
def get_architecture():
    items = service.list_architecture()
    return {"success": True, "count": len(items), "layers": items}


@router.get("/services")
def list_services():
    items = service.list_services()
    return {"success": True, "count": len(items), "items": items}


@router.get("/tools")
def list_tools():
    items = service.list_tools()
    return {"success": True, "count": len(items), "items": items}


@router.get("/integrations")
def list_integrations():
    items = service.list_integrations()
    return {"success": True, "count": len(items), "items": items}
