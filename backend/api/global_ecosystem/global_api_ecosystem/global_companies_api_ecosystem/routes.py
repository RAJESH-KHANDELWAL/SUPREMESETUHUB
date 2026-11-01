"""FastAPI endpoints for singular Company and plural Companies APIs."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import CompanyAlphabetResponse, CompanyApiStatus, CompanyListResponse, CompanyRecord
from .service import get_api_status, get_company, get_company_alphabet, search_companies

router = APIRouter(tags=["GLOBAL COMPANY API", "GLOBAL COMPANIES API"])


def _search(
    q: str | None,
    country: str | None,
    industry: str | None,
    entity_type: str | None,
    verification_status: str | None,
    letter: str | None,
    limit: int,
    offset: int,
):
    return search_companies(q, country, industry, entity_type, verification_status, letter, limit, offset)


@router.get("/global/companies/status", response_model=CompanyApiStatus)
def companies_api_status():
    return get_api_status()


@router.get("/global/companies/alphabet", response_model=CompanyAlphabetResponse)
def companies_alphabet():
    """Return A-Z counts for records currently in the registry."""
    return get_company_alphabet()


@router.get("/global/companies", response_model=CompanyListResponse)
def list_companies(
    q: str | None = Query(default=None, description="Search company name, alias, or description"),
    country: str | None = Query(default=None, min_length=2, max_length=2, description="ISO 3166-1 alpha-2 country code"),
    industry: str | None = Query(default=None),
    entity_type: str | None = Query(default=None),
    verification_status: str | None = Query(default=None),
    letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    """List companies alphabetically, with optional letter and metadata filters."""
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset)


@router.get("/global/companies/search", response_model=CompanyListResponse)
def search_companies_endpoint(
    q: str | None = Query(default=None),
    country: str | None = Query(default=None, min_length=2, max_length=2),
    industry: str | None = Query(default=None),
    entity_type: str | None = Query(default=None),
    verification_status: str | None = Query(default=None),
    letter: str | None = Query(default=None, min_length=1, max_length=1, pattern="^[A-Za-z]$"),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    return _search(q, country, industry, entity_type, verification_status, letter, limit, offset)


@router.get("/global/companies/{company_id}", response_model=CompanyRecord)
def company_details(company_id: str):
    record = get_company(company_id)
    if record is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return record


@router.get("/global/company/{company_id}", response_model=CompanyRecord)
def singular_company_details(company_id: str):
    return company_details(company_id)
