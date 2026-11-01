"""FastAPI endpoints for the modular Company, Business and Freelancer directory."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import CompanyAlphabetResponse, CompanyApiStatus, CompanyListResponse, CompanyRecord
from .service import get_api_status, get_company, get_company_alphabet, search_companies
from .classification_registry import list_record_classes, get_record_class, validate_record_class_registry
from .global_company_world_map import list_world_domains, get_world_domain
from .industry_api_ecosystems.registry import list_industries
from .country_api_ecosystems.registry import COUNTRY_ECOSYSTEM_STATUS
from .provider_api_ecosystems.registry import PROVIDER_ECOSYSTEM_STATUS
from .company_legal_entities_api_ecosystem.routes import router as company_directory_router
from .business_enterprises_api_ecosystem.routes import router as business_directory_router
from .freelancer_independent_professionals_api_ecosystem.routes import router as freelancer_directory_router

router = APIRouter(tags=["GLOBAL COMPANY API", "GLOBAL COMPANIES API", "GLOBAL BUSINESS API", "GLOBAL FREELANCER API"])
router.include_router(company_directory_router)
router.include_router(business_directory_router)
router.include_router(freelancer_directory_router)

def _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category=None):
    try:
        return search_companies(q, country, industry, entity_type, verification_status, letter, limit, offset, category)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/global/companies/status", response_model=CompanyApiStatus)
def companies_api_status():
    return get_api_status()

@router.get("/global/company-directory/architecture")
def company_directory_architecture():
    return {"success": True, "ecosystem": "GLOBAL COMPANY / COMPANIES API ECOSYSTEM", "architecture_pattern": "modular_domain_packages_with_shared_registry", "record_classes": list_record_classes(), "industry_registry_status": "taxonomy_only", "country_ecosystem": COUNTRY_ECOSYSTEM_STATUS, "provider_ecosystem": PROVIDER_ECOSYSTEM_STATUS, "profile_storage": "shared_parent_json_registry", "live_external_connections": False}

@router.get("/global/company-directory/classes")
def company_directory_classes():
    return {"success": True, "count": len(list_record_classes()), "record_classes": list_record_classes()}

@router.get("/global/company-directory/classes/integrity")
def company_directory_class_integrity():
    result = validate_record_class_registry()
    if not result["structurally_valid"]:
        raise HTTPException(status_code=500, detail=result)
    return {"success": True, **result}

@router.get("/global/company-directory/classes/{record_type}")
def company_directory_class(record_type: str):
    category = get_record_class(record_type)
    if category is None:
        raise HTTPException(status_code=404, detail={"error":"RECORD_CLASS_NOT_FOUND","record_type":record_type})
    return {"success": True, "category": category}

@router.get("/global/company-directory/world-map")
def company_directory_world_map():
    domains = list_world_domains()
    return {"success": True, "count": len(domains), "domains": domains}

@router.get("/global/company-directory/world-map/{domain_id}")
def company_directory_world_domain(domain_id: str):
    domain = get_world_domain(domain_id)
    if domain is None:
        raise HTTPException(status_code=404, detail={"error":"WORLD_DOMAIN_NOT_FOUND","domain_id":domain_id})
    return {"success": True, "domain": domain}

@router.get("/global/company-directory/industries")
def company_directory_industries():
    industries = list_industries()
    return {"success": True, "count": len(industries), "registry_status":"taxonomy_only", "industries": industries}

@router.get("/global/companies/alphabet", response_model=CompanyAlphabetResponse)
def companies_alphabet():
    return get_company_alphabet()

@router.get("/global/companies", response_model=CompanyListResponse)
def list_companies(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), industry: str | None = Query(default=None), entity_type: str | None = Query(default=None), verification_status: str | None = Query(default=None), letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"), category: str | None = Query(default=None, description="company, business or freelancer"), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category)

@router.get("/global/companies/search", response_model=CompanyListResponse)
def search_companies_endpoint(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), industry: str | None = Query(default=None), entity_type: str | None = Query(default=None), verification_status: str | None = Query(default=None), letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"), category: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category)

@router.get("/global/businesses", response_model=CompanyListResponse)
def list_businesses(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), industry: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, None, None, None, limit, offset, "business")

@router.get("/global/freelancers", response_model=CompanyListResponse)
def list_freelancers(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2), industry: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, None, None, None, limit, offset, "freelancer")

@router.get("/global/companies/sources")
def list_company_sources(country: str | None = Query(default=None, min_length=2, max_length=2)):
    from .service import list_country_sources
    return list_country_sources(country)

@router.get("/global/companies/sources/{source_id}")
def company_source_details(source_id: str):
    from .service import get_country_source
    source = get_country_source(source_id)
    if source is None:
        raise HTTPException(status_code=404, detail="Company data source not found")
    return {"registry_status":"source_directory_only","source":source}

@router.get("/global/companies/{company_id}", response_model=CompanyRecord)
def company_details(company_id: str):
    record = get_company(company_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return record

@router.get("/global/company/{company_id}", response_model=CompanyRecord)
def singular_company_details(company_id: str):
    return company_details(company_id)
