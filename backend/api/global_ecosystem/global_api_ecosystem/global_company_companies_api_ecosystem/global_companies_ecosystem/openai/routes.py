"""OpenAI company profile API routes."""
from fastapi import APIRouter
from .schemas import CompanyProfileResponse
from .service import get_company_profile, get_source_registry

router = APIRouter(prefix="/global/company-directory/company-profiles/openai", tags=["Company Profiles: OpenAI"])

@router.get("", response_model=CompanyProfileResponse)
def openai_company_profile():
    """Return conservative company metadata and its declared source provenance."""
    return get_company_profile()

@router.get("/sources")
def openai_company_sources():
    """Return registered sources; this endpoint does not imply live connectivity."""
    return get_source_registry()
