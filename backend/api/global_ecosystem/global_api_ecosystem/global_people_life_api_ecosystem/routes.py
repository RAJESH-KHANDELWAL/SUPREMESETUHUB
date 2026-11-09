"""FastAPI routes for global people, work and life taxonomy discovery."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import DomainListResponse, DomainResponse
from .service import PeopleLifeService

router = APIRouter(prefix="/api/v1/global-people-life", tags=["GLOBAL PEOPLE, WORK & LIFE API"])
service = PeopleLifeService()


@router.get("/status")
def status():
    return {"success": True, "ecosystem": "GLOBAL PEOPLE, WORK & LIFE API",
            "status": "CATALOG_ONLY", "live_directory": False}


@router.get("/domains", response_model=DomainListResponse)
def list_domains(include_adult: bool = Query(False, description="Include separately classified 18+ domains")):
    return service.list_domains(include_adult=include_adult)


@router.get("/domains/search")
def search_domains(q: str = Query(min_length=1, max_length=100),
                   include_adult: bool = Query(False)):
    results = service.search_domains(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "domains": results}


@router.get("/domains/{domain_id}", response_model=DomainResponse)
def get_domain(domain_id: str, include_adult: bool = Query(False)):
    domain = service.get_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(status_code=404, detail="PEOPLE_LIFE_DOMAIN_NOT_FOUND")
    return {"success": True, "domain": domain}
