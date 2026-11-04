"""Global World A-Z discovery endpoints."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import WorldDomainListResponse, WorldDomainResponse
from .service import GlobalWorldService

router = APIRouter(prefix="/api/v1/global-world", tags=["SUPREMESETUHUB GLOBAL WORLD A-Z"])
service = GlobalWorldService()


@router.get("/status")
def get_status():
    return service.status()


@router.get("/domains", response_model=WorldDomainListResponse)
def list_domains(include_adult: bool = Query(False, description="Include separately classified 18+ taxonomy entries; this flag is not age verification")):
    return service.list_domains(include_adult=include_adult)


@router.get("/domains/search")
def search_domains(q: str = Query(min_length=1, max_length=100), include_adult: bool = Query(False, description="Include separately classified 18+ taxonomy entries")):
    results = service.search_domains(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "domains": results}


@router.get("/domains/{domain_id}", response_model=WorldDomainResponse)
def get_domain(domain_id: str, include_adult: bool = Query(False)):
    domain = service.get_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(status_code=404, detail="GLOBAL_WORLD_DOMAIN_NOT_FOUND")
    return {"success": True, "domain": domain}


@router.get("/ecosystems")
def list_linked_ecosystems():
    return {"success": True, "count": len(service.list_domains()["ecosystems"]), "ecosystems": service.list_domains()["ecosystems"]}
