from fastapi import APIRouter, HTTPException, Query

from .schemas import BusinessEcosystemStatus
from .service import BusinessEcosystemService


router = APIRouter(
    prefix="/api/v1/global-ecosystem/business",
    tags=["GLOBAL BADA BUSINESS API ECOSYSTEM"],
)

service = BusinessEcosystemService()


@router.get("/status", response_model=BusinessEcosystemStatus)
def get_status():
    return service.get_status()


@router.get("/modules")
def list_modules():
    return service.list_modules()


@router.get("/modules/{module_id}")
def get_module(module_id: str):
    module = service.get_module(module_id)
    if module is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_MODULE_NOT_FOUND", "module_id": module_id})
    return {"success": True, "ecosystem_id": service.ECOSYSTEM_ID, "module": module}


@router.get("/catalog")
def list_business_categories(
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
    include_adult: bool = Query(default=False, description="Include 18+ adult-industry categories"),
):
    return service.list_categories(channel=channel, include_adult=include_adult)


@router.get("/catalog/search")
def search_business_categories(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = service.search_categories(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "categories": results}


@router.get("/catalog/{category_id}")
def get_business_category(
    category_id: str,
    include_adult: bool = Query(default=False),
):
    category = service.get_category(category_id, include_adult=include_adult)
    if category is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "BUSINESS_CATEGORY_NOT_FOUND", "category_id": category_id},
        )
    return {"success": True, "category": category}


@router.get("/world-map")
def list_global_world_business_map(
    include_adult: bool = Query(default=False, description="Include separately classified 18+ domain references; this is not age verification"),
):
    return service.list_global_world_map(include_adult=include_adult)


@router.get("/world-map/{domain_id}")
def get_global_world_business_domain(
    domain_id: str,
    include_adult: bool = Query(default=False),
):
    domain = service.get_global_world_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "GLOBAL_WORLD_DOMAIN_NOT_FOUND", "domain_id": domain_id},
        )
    return {"success": True, "domain": domain}


@router.get("/world-catalog")
def list_full_global_world_catalog(
    include_adult: bool = Query(default=False, description="Include separately classified 18+ domains; this is not age verification"),
):
    return service.list_global_world_catalog(include_adult=include_adult)


@router.get("/world-catalog/search")
def search_full_global_world_catalog(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = service.search_global_world_catalog(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "global_world_domains": results}


@router.get("/world-catalog/{domain_id}")
def get_full_global_world_catalog_domain(
    domain_id: str,
    include_adult: bool = Query(default=False),
):
    domain = service.get_global_world_catalog_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(
            status_code=404,
            detail={"error": "GLOBAL_WORLD_DOMAIN_NOT_FOUND", "domain_id": domain_id},
        )
    return {"success": True, "domain": domain}
