"""OpenAI company profile API routes."""
from fastapi import APIRouter
from .schemas import CompanyProfileResponse
from .service import get_company_profile, get_source_registry

router = APIRouter(prefix="/global/company-profile-adapters/openai", tags=["Company Profile: OpenAI"])

@router.get("", response_model=CompanyProfileResponse)
def openai_company_profile():
    return get_company_profile()

@router.get("/sources")
def openai_company_sources():
    return get_source_registry()

@router.get("/status")
def openai_company_adapter_status():
    return {
        "company_id": "openai",
        "adapter": "metadata_only",
        "configured": True,
        "live_connection": False,
        "authentication_configured": False,
        "last_sync": None,
        "status": "not_connected",
    }
