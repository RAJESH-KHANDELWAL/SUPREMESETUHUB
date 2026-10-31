from fastapi import APIRouter, HTTPException, Query

from .schemas import BusinessEcosystemStatus
from .service import BusinessEcosystemService

from .global_world_catalog import (
    get_domain as get_universal_domain,
    list_domains as list_universal_domains,
    search_subcategories as search_universal_subcategories,
    validate_registry as validate_universal_registry,
)


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



@router.get("/work-business/facets")
def get_work_business_facets():
    from .sectors import get_sector_facets
    return {"success": True, "facets": get_sector_facets()}


@router.get("/work-business")
def list_work_business(
    channel: str | None = Query(default=None, pattern="^(online|offline|hybrid)$"),
    include_adult: bool = Query(default=False, description="Include separately classified 18+ business sectors; this is not age verification"),
):
    try:
        return service.list_work_business(channel, include_adult)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc))


@router.get("/work-business/{sector_id}")
def get_work_business_sector(sector_id: str, include_adult: bool = Query(default=False)):
    sector = service.get_work_business_sector(sector_id, include_adult)
    if sector is None:
        raise HTTPException(status_code=404, detail={"error": "BUSINESS_SECTOR_NOT_FOUND", "sector_id": sector_id})
    return {"success": True, "sector": sector}


@router.get("/taxonomy/integrity")
def get_taxonomy_integrity():
    """Validate category references and Global World/crosswalk consistency."""
    result = service.get_taxonomy_integrity()
    if not result["success"]:
        raise HTTPException(status_code=500, detail=result)
    return result


@router.get("/universal/domains")
def list_universal_work_business_domains(
    include_adult: bool = Query(default=False, description="Include separately restricted 18+ taxonomy; this flag is not age verification"),
):
    domains = list_universal_domains(include_adult=include_adult)
    return {"success": True, "count": len(domains), "registry_status": "taxonomy_catalog_only", "domains": domains}


@router.get("/universal/domains/{domain_id}")
def get_universal_work_business_domain(
    domain_id: str,
    include_adult: bool = Query(default=False),
):
    domain = get_universal_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(status_code=404, detail={"error": "UNIVERSAL_DOMAIN_NOT_FOUND", "domain_id": domain_id})
    return {"success": True, "domain": domain}


@router.get("/universal/search")
def search_universal_work_business_taxonomy(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = search_universal_subcategories(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "results": results}


@router.get("/universal/integrity")
def get_universal_work_business_integrity():
    return {"success": True, **validate_universal_registry()}


# Mount the India + Global Industry Ecosystems API under the existing Bada Business API.
from .industry_api_ecosystems.routes import router as industry_api_ecosystems_router

router.include_router(industry_api_ecosystems_router)

@router.get("/domains")
def list_domain_packages(
    include_adult: bool = Query(default=False, description="Include restricted 18+ taxonomy; this flag is not age verification"),
):
    """List the direct-root India + Global domain packages."""
    return service.list_domains(include_adult=include_adult)


@router.get("/domains/search")
def search_domain_packages(
    q: str = Query(min_length=1, max_length=100),
    include_adult: bool = Query(default=False),
):
    results = service.search_domains(q, include_adult=include_adult)
    return {"success": True, "count": len(results), "results": results}


@router.get("/domains/integrity")
def get_domain_package_integrity():
    """Validate domain package IDs, subcategories and adult default exclusion."""
    result = service.get_domain_registry_integrity()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return {"success": True, **result}


@router.get("/domains/{domain_id}")
def get_domain_package(
    domain_id: str,
    include_adult: bool = Query(default=False),
):
    domain = service.get_domain(domain_id, include_adult=include_adult)
    if domain is None:
        raise HTTPException(status_code=404, detail={"error": "DOMAIN_PACKAGE_NOT_FOUND", "domain_id": domain_id})
    return {"success": True, "domain": domain}
