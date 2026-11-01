"""FastAPI endpoints for singular Company and plural Companies APIs."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import CompanyApiStatus, CompanyListResponse, CompanyRecord
from .service import get_api_status, get_company, search_companies

router = APIRouter(tags=["GLOBAL COMPANY API", "GLOBAL COMPANIES API"])


@router.get("/global/companies/status", response_model=CompanyApiStatus)
def companies_api_status():
    """Return API and registry readiness."""
    return get_api_status()


@router.get("/global/companies", response_model=CompanyListResponse)
def list_companies(
    q: str | None = Query(default=None, description="Search company name, alias, or description"),
    country: str | None = Query(default=None, min_length=2, max_length=2, description="ISO 3166-1 alpha-2 country code"),
    industry: str | None = Query(default=None),
    entity_type: str | None = Query(default=None),
    verification_status: str | None = Query(default=None),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    """List/search businesses and companies with filters and pagination."""
    return search_companies(q, country, industry, entity_type, verification_status, limit, offset)


@router.get("/global/companies/search", response_model=CompanyListResponse)
def search_companies_endpoint(
    q: str | None = Query(default=None),
    country: str | None = Query(default=None, min_length=2, max_length=2),
    industry: str | None = Query(default=None),
    entity_type: str | None = Query(default=None),
    verification_status: str | None = Query(default=None),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    """Explicit search endpoint; uses the same filters as the collection."""
    return search_companies(q, country, industry, entity_type, verification_status, limit, offset)


@router.get("/global/companies/{company_id}", response_model=CompanyRecord)
def company_details(company_id: str):
    """Fetch one company/business profile by stable ID."""
    record = get_company(company_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return record


@router.get("/global/company/{company_id}", response_model=CompanyRecord)
def singular_company_details(company_id: str):
    """Singular Company API alias for integrations expecting /global/company."""
    return company_details(company_id)
