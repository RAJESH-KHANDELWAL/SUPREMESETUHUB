"""People, work and life discovery endpoints, mounted under the business ecosystem API."""

from fastapi import APIRouter, HTTPException, Query

from .people_life_service import PeopleLifeEcosystemService


people_life_router = APIRouter(
    prefix="/people-life",
    tags=["GLOBAL PEOPLE, WORK & LIFE ECOSYSTEM"],
)
people_life_service = PeopleLifeEcosystemService()


@people_life_router.get("/domains")
def list_people_life_domains(
    include_adult: bool = Query(default=False, description="Include separately age-gated 18+ domains"),
):
    return people_life_service.list_domains(include_adult=include_adult)


@people_life_router.get("/domains/search")
def search_people_life_domains(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = people_life_service.search_domains(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "domains": results}


@people_life_router.get("/domains/{domain_id}")
def get_people_life_domain(
    domain_id: str,
    include_adult: bool = Query(default=False),
):
    domain = people_life_service.get_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "PEOPLE_LIFE_DOMAIN_NOT_FOUND", "domain_id": domain_id},
        )
    return {"success": True, "domain": domain}
