"""FastAPI endpoints for the unified Company, Business and Freelancer directory."""
from fastapi import APIRouter, HTTPException, Query
from .schemas import CompanyAlphabetResponse, CompanyApiStatus, CompanyListResponse, CompanyRecord
from .service import get_api_status, get_company, get_company_alphabet, search_companies

router = APIRouter(tags=["GLOBAL COMPANY API", "GLOBAL COMPANIES API", "GLOBAL BUSINESS API", "GLOBAL FREELANCER API"])

def _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category=None):
    try:
        return search_companies(q, country, industry, entity_type, verification_status, letter, limit, offset, category)
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/global/companies/status", response_model=CompanyApiStatus)
def companies_api_status():
    return get_api_status()

@router.get("/global/companies/alphabet", response_model=CompanyAlphabetResponse)
def companies_alphabet():
    return get_company_alphabet()

@router.get("/global/companies", response_model=CompanyListResponse)
def list_companies(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2),
                   industry: str | None = Query(default=None), entity_type: str | None = Query(default=None),
                   verification_status: str | None = Query(default=None), letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"),
                   category: str | None = Query(default=None, description="company, business or freelancer"),
                   limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category)

@router.get("/global/companies/search", response_model=CompanyListResponse)
def search_companies_endpoint(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2),
                              industry: str | None = Query(default=None), entity_type: str | None = Query(default=None),
                              verification_status: str | None = Query(default=None), letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"),
                              category: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200),
                              offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset, category)

@router.get("/global/businesses", response_model=CompanyListResponse)
def list_businesses(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2),
                    industry: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, None, None, None, limit, offset, "business")

@router.get("/global/freelancers", response_model=CompanyListResponse)
def list_freelancers(q: str | None = Query(default=None), country: str | None = Query(default=None, min_length=2, max_length=2),
                     industry: str | None = Query(default=None), limit: int = Query(default=50, ge=1, le=200), offset: int = Query(default=0, ge=0)):
    return _search(q, country, industry, None, None, None, limit, offset, "freelancer")

@router.get("/global/companies/sources")
def list_company_sources(country: str | None = Query(default=None, min_length=2, max_length=2)):
    from .service import list_country_sources
    return list_country_sources(country)

@router.get("/global/companies/sources/{source_id}")
def company_source_details(source_id: str):
    from .service import get_country_source
    source = get_country_source(source_id)
    if source is None: raise HTTPException(status_code=404, detail="Company data source not found")
    return {"registry_status": "source_directory_only", "source": source}

@router.get("/global/companies/{company_id}", response_model=CompanyRecord)
def company_details(company_id: str):
    record = get_company(company_id)
    if record is None: raise HTTPException(status_code=404, detail="Company not found")
    return record

@router.get("/global/company/{company_id}", response_model=CompanyRecord)
def singular_company_details(company_id: str):
    return company_details(company_id)
