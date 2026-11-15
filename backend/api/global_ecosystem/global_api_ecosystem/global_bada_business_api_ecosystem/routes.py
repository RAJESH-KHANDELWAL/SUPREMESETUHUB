from fastapi import APIRouter, HTTPException, Query

from .schemas import BusinessEcosystemStatus
from .service import BusinessEcosystemService
from backend.global_ecosystem.global_bada_business_ecosystem.platform_resources import get_catalog as get_platform_resource_catalog
from ..ecosystem_link_registry import get_ecosystem_linkage
from .global_kamasutra_intimacy_relationship_sex_chudai_porn_adult_health_wellness_api_ecosystem import router as kamasutra_business_router

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

from .integrations.routes import router as integrations_router
router.include_router(integrations_router)
router.include_router(kamasutra_business_router, prefix="/kamasutra")


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



# Dedicated Global Services API facade; canonical service category data remains in its domain package.
from .global_services_api_ecosystem import router as global_services_api_router
router.include_router(global_services_api_router)

# Unified Work & Business discovery API; canonical work, freelance and jobs catalogues remain in their owning packages.
from .global_work_business_api_ecosystem import router as global_work_business_api_router
router.include_router(global_work_business_api_router)

# Cultural service, work and business API; mounted under the Global Bada Business API.
from .global_vasudhaiva_kutumbakam_sanatan_dharma_bharat_world_culture_service_work_business_api_ecosystem import router as global_culture_service_work_business_api_router
router.include_router(global_culture_service_work_business_api_router)

# Mount the independent business registration and compliance discovery API.
from .global_business_governance_compliance_standards_api_ecosystem.global_business_compliance_api_ecosystem.routes import router as business_compliance_router
router.include_router(business_compliance_router)

# Mount the independent manufacturer-to-customer distribution channel API.
from .global_distribution_channels_api_ecosystem.routes import router as distribution_channels_router

router.include_router(distribution_channels_router)

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


# Mount versioned national and international economic-activity classification standards.
from .global_business_governance_compliance_standards_api_ecosystem.global_classification_standards_business_api_ecosystem.routes import router as classification_standards_router
router.include_router(classification_standards_router)


# Expose the user-approved scope and acceptance decisions through this ecosystem.
from .global_business_governance_compliance_standards_api_ecosystem.governance.routes import router as governance_router
router.include_router(governance_router)

# Business lifecycle, trust, jurisdictional compliance and BI API contracts.
from .business_capabilities.routes import router as business_capabilities_router
router.include_router(business_capabilities_router)


# Universal A-Z India + Global work/business taxonomy API.
from .global_universal_work_business_taxonomy_api_ecosystem.routes import router as universal_work_business_taxonomy_router
router.include_router(universal_work_business_taxonomy_router)


# Dedicated Work, Jobs & Careers subcategory APIs.
from .global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.routes import router as work_careers_router
router.include_router(work_careers_router)

# Mount every independent Work & Careers job-family package at its canonical API path.
from .global_freelancer_gig_independent_work_business_api_ecosystem.jobs_careers_employment_api_ecosystem.specialization_routes import router as work_careers_specializations_router
router.include_router(work_careers_specializations_router)

# Independent freelance specialization APIs and their work-type catalogues.
from .global_freelancer_gig_independent_work_business_api_ecosystem.specializations import router as freelance_specializations_router
router.include_router(freelance_specializations_router)


@router.get("/ecosystem-links")
def business_ecosystem_links(include_adult: bool = Query(default=False)):
    """Read-only links to canonical Company and Platform taxonomies."""
    return get_ecosystem_linkage(include_adult=include_adult)


@router.get("/platform-resources")
def list_bada_business_platform_resources():
    """Return Bada Business links/program resources from the canonical ecosystem."""
    return get_platform_resource_catalog()
