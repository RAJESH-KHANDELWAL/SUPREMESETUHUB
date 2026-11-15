"""HTTP routes for the GLOBAL PLATFORMS API ECOSYSTEM."""
from fastapi import APIRouter, HTTPException, Query
from ..ecosystem_link_registry import get_ecosystem_linkage
from .catalog import PLATFORM_TYPES, OWNERSHIP_TYPES, BUSINESS_MODELS, VERIFICATION_STATES
from .schemas import EcosystemStatus, PlatformListResponse
from .service import get_ecosystem_status, list_domains, get_domain, search_platforms, get_platform
from .provider_directory import list_platform_providers, get_platform_provider, get_provider_directory_status
from .global_platforms_ecosystem.routes import router as platform_directory_router

router = APIRouter(prefix="/global/platforms", tags=["GLOBAL PLATFORMS API ECOSYSTEM"])
router.include_router(platform_directory_router)

@router.get("/status", response_model=EcosystemStatus)
def ecosystem_status(): return get_ecosystem_status()

@router.get("/architecture")
def architecture():
    return {"success":True,"architecture_pattern":"modular_domain_packages_with_shared_platform_registry","canonical_entity":"digital_or_service_platform","independent_dimensions":["domain","platform_type","ownership","business_model","country","verification","adult_safety"],"profile_storage":"local_json_read_only","taxonomy_source":"curated_metadata","live_external_connections":False,"reference_boundary":"Business categories are linked by read-only crosswalk references; their canonical source remains Global Bada Business.","provider_directory":get_provider_directory_status()}

@router.get("/domains")
def platform_domains(include_adult: bool = Query(default=False)):
    domains = list_domains(include_adult=include_adult)
    return {"success":True,"count":len(domains),"include_adult":include_adult,"domains":domains}

@router.get("/domains/{domain_id}")
def platform_domain_details(domain_id: str, include_adult: bool = Query(default=False)):
    domain = get_domain(domain_id)
    if domain is None or (domain.get("adult_only") and not include_adult): raise HTTPException(status_code=404, detail="Platform domain not found")
    return {"success":True,"domain":domain}

@router.get("/classification")
def platform_classification():
    return {"platform_types":PLATFORM_TYPES,"ownership_types":OWNERSHIP_TYPES,"business_models":BUSINESS_MODELS,"verification_states":VERIFICATION_STATES}

@router.get("", response_model=PlatformListResponse)
@router.get("/search", response_model=PlatformListResponse)
def platform_search(q: str | None = Query(default=None), domain: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), platform_type: str | None = Query(default=None), verification_status: str | None = Query(default=None), include_adult: bool = Query(default=False), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    try: return search_platforms(q, domain, country, platform_type, verification_status, include_adult, limit, offset)
    except ValueError as exc: raise HTTPException(status_code=422, detail=str(exc)) from exc



@router.get("/providers")
def platform_provider_directory(include_adult: bool = Query(default=False)):
    providers = list_platform_providers(include_adult=include_adult)
    return {"success": True, "count": len(providers), "include_adult": include_adult, "providers": providers}


@router.get("/providers/{provider_id}")
def platform_provider_details(provider_id: str, include_adult: bool = Query(default=False)):
    provider = get_platform_provider(provider_id, include_adult=include_adult)
    if provider is None:
        raise HTTPException(status_code=404, detail="PLATFORM_PROVIDER_NOT_FOUND")
    return {"success": True, "provider": provider}


@router.get("/{platform_id}")
def platform_details(platform_id: str, include_adult: bool = Query(default=False)):
    platform = get_platform(platform_id, include_adult=include_adult)
    if platform is None: raise HTTPException(status_code=404, detail="Platform not found")
    return {"success":True,"item":platform}


@router.get("/ecosystem-links")
def platform_ecosystem_links(include_adult: bool = Query(default=False)):
    """Read-only links to canonical Business and Company taxonomies."""
    return get_ecosystem_linkage(include_adult=include_adult)
