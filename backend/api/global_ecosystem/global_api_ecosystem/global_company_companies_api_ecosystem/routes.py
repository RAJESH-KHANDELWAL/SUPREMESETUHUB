"""FastAPI endpoints for Company, Enterprise and Corporate Group directories."""
from fastapi import APIRouter, HTTPException, Query
from ..ecosystem_link_registry import get_ecosystem_linkage
from .schemas import CompanyAlphabetResponse, CompanyApiStatus, CompanyListResponse
from .service import get_api_status, get_company_alphabet, search_companies
from .classification_registry import list_record_classes, get_record_class, validate_record_class_registry
from .global_company_world_map import list_world_domains, get_world_domain
from .country_api_ecosystems.registry import COUNTRY_ECOSYSTEM_STATUS
from .provider_api_ecosystems.registry import PROVIDER_ECOSYSTEM_STATUS
from .company_legal_entities_api_ecosystem.routes import router as company_directory_router
from .business_enterprises_api_ecosystem.routes import router as legacy_business_directory_router
from .business_enterprises_api_ecosystem.enterprise_routes import router as enterprise_directory_router
from .corporate_groups_api_ecosystem.routes import router as corporate_groups_router
from .company_classification_standards_api_ecosystem.routes import router as classification_standards_router
from .company_modules_api_ecosystem.routes import router as company_modules_router
from .industry_api_ecosystems.routes import router as industry_router
from .country_api_ecosystems.routes import router as country_router
from .provider_api_ecosystems.routes import router as provider_router
from .sectors.routes import router as sector_router
from .integrations.routes import router as integrations_router
from .services.routes import router as services_router
from .tools.routes import router as tools_router
from .global_companies_ecosystem.routes import router as company_profile_adapters_router
from .company_profile_directory import router as company_profile_directory_router
router=APIRouter(tags=["GLOBAL COMPANY API","GLOBAL COMPANIES API","GLOBAL ENTERPRISE API","GLOBAL CORPORATE GROUPS API"])
router.include_router(company_directory_router)
router.include_router(enterprise_directory_router)
router.include_router(legacy_business_directory_router)
router.include_router(corporate_groups_router)
router.include_router(classification_standards_router)
router.include_router(company_modules_router)
router.include_router(industry_router)
router.include_router(country_router)
router.include_router(provider_router)
router.include_router(sector_router)
router.include_router(integrations_router)
router.include_router(services_router)
router.include_router(tools_router)
router.include_router(company_profile_adapters_router)
router.include_router(company_profile_directory_router)
def _search(q,country,industry,entity_type,verification_status,letter,limit,offset,category=None):
 try: return search_companies(q,country,industry,entity_type,verification_status,letter,limit,offset,category)
 except ValueError as exc: raise HTTPException(status_code=422,detail=str(exc)) from exc
@router.get("/global/companies/status",response_model=CompanyApiStatus)
def companies_api_status(): return get_api_status()
@router.get("/global/company-directory/architecture")
def company_directory_architecture():
 return {"success":True,"ecosystem":"GLOBAL COMPANY / COMPANIES API ECOSYSTEM","architecture_pattern":"modular_domain_packages_with_shared_registry","record_classes":list_record_classes(),"industry_registry_status":"taxonomy_only","country_ecosystem":COUNTRY_ECOSYSTEM_STATUS,"provider_ecosystem":PROVIDER_ECOSYSTEM_STATUS,"profile_storage":"shared_parent_json_registry","live_external_connections":False}
@router.get("/global/company-directory/classes")
def company_directory_classes(): return {"success":True,"count":len(list_record_classes()),"record_classes":list_record_classes()}
@router.get("/global/company-directory/classes/integrity")
def company_directory_class_integrity():
 result=validate_record_class_registry()
 if not result["structurally_valid"]: raise HTTPException(status_code=500,detail=result)
 return {"success":True,**result}
@router.get("/global/company-directory/classes/{record_type}")
def company_directory_class(record_type:str):
 category=get_record_class(record_type)
 if category is None: raise HTTPException(status_code=404,detail={"error":"RECORD_CLASS_NOT_FOUND","record_type":record_type})
 return {"success":True,"category":category}
@router.get("/global/company-directory/world-map")
def company_directory_world_map():
 domains=list_world_domains()
 return {"success":True,"count":len(domains),"domains":domains}
@router.get("/global/company-directory/world-map/{domain_id}")
def company_directory_world_domain(domain_id:str):
 domain=get_world_domain(domain_id)
 if domain is None: raise HTTPException(status_code=404,detail={"error":"WORLD_DOMAIN_NOT_FOUND","domain_id":domain_id})
 return {"success":True,"domain":domain}
@router.get("/global/companies/alphabet",response_model=CompanyAlphabetResponse)
def companies_alphabet(): return get_company_alphabet()
@router.get("/global/companies",response_model=CompanyListResponse)
def list_companies(q:str|None=Query(default=None),country:str|None=Query(default=None,min_length=2,max_length=2),industry:str|None=Query(default=None),entity_type:str|None=Query(default=None),verification_status:str|None=Query(default=None),letter:str|None=Query(default=None,min_length=1,max_length=1,pattern="^[A-Za-z]$"),category:str|None=Query(default=None,description="legacy profile filter"),limit:int=Query(default=50,ge=1,le=200),offset:int=Query(default=0,ge=0)):
 return _search(q,country,industry,entity_type,verification_status,letter,limit,offset,category)
@router.get("/global/companies/search",response_model=CompanyListResponse)
def search_companies_endpoint(q:str|None=Query(default=None),country:str|None=Query(default=None,min_length=2,max_length=2),industry:str|None=Query(default=None),entity_type:str|None=Query(default=None),verification_status:str|None=Query(default=None),letter:str|None=Query(default=None,min_length=1,max_length=1,pattern="^[A-Za-z]$"),category:str|None=Query(default=None),limit:int=Query(default=50,ge=1,le=200),offset:int=Query(default=0,ge=0)):
 return _search(q,country,industry,entity_type,verification_status,letter,limit,offset,category)
@router.get("/global/businesses",response_model=CompanyListResponse)
def list_businesses(q:str|None=Query(default=None),country:str|None=Query(default=None,min_length=2,max_length=2),industry:str|None=Query(default=None),limit:int=Query(default=50,ge=1,le=200),offset:int=Query(default=0,ge=0)):
 return _search(q,country,industry,None,None,None,limit,offset,"business")
@router.get("/global/companies/sources")
def list_company_sources(country:str|None=Query(default=None,min_length=2,max_length=2)):
 from .service import list_country_sources
 return list_country_sources(country)
@router.get("/global/companies/sources/{source_id}")
def company_source_details(source_id:str):
 from .service import get_country_source
 source=get_country_source(source_id)
 if source is None: raise HTTPException(status_code=404,detail="Company data source not found")
 return {"registry_status":"source_directory_only","source":source}
@router.get("/global/companies/{company_id}")
def company_details(company_id:str):
 from .service import get_company
 company=get_company(company_id)
 if company is None: raise HTTPException(status_code=404,detail="Company not found")
 return {"success":True,"item":company}


@router.get("/global/company-directory/ecosystem-links")
def company_ecosystem_links(include_adult: bool = Query(default=False)):
    """Read-only links to canonical Business and Platform taxonomies."""
    return get_ecosystem_linkage(include_adult=include_adult)
