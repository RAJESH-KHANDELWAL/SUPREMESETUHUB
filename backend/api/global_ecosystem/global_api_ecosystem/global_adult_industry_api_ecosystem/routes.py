"""FastAPI router for the GLOBAL ADULT INDUSTRY ECOSYSTEM catalog."""
from fastapi import APIRouter

from .service import get_adult_industry_status, list_adult_industry_providers

router = APIRouter(
    prefix="/api/v1/global-adult-industry-ecosystem",
    tags=["GLOBAL ADULT INDUSTRY ECOSYSTEM"],
)


@router.get("/status")
def adult_industry_status():
    return get_adult_industry_status()


@router.get("/providers")
def adult_industry_providers():
    providers = list_adult_industry_providers()
    return {
        "success": True,
        "system": "GLOBAL ADULT INDUSTRY ECOSYSTEM",
        "count": len(providers),
        "providers": providers,
        "note": "Catalog entries do not imply API availability or live connectivity.",
    }
