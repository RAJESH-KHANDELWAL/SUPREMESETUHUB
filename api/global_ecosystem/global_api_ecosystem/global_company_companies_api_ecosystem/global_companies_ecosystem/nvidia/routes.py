"""Company-specific API routes for NVIDIA."""
from fastapi import APIRouter
from .schemas import CompanyProfile
from .service import get_profile, get_sources, get_adapter_status

router = APIRouter(
    prefix="/global/company-profile-adapters/nvidia",
    tags=["Company Profile: NVIDIA"],
)

@router.get("", response_model=CompanyProfile)
def company_profile():
    """Return company discovery metadata with explicit verification boundaries."""
    return get_profile()

@router.get("/sources")
def company_sources():
    """List declared public sources; no live retrieval is implied."""
    return get_sources()

@router.get("/status")
def company_adapter_status():
    """Expose adapter readiness without misrepresenting connectivity."""
    return get_adapter_status()
