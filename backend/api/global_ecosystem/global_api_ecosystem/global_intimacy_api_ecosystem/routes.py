"""Read-only discovery routes for relationship and intimacy ecosystem."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import IntimacyCategory, IntimacyEcosystemStatus, IntimacyProvider
from .service import get_ecosystem_status, list_categories, list_providers

router = APIRouter(
    prefix="/api/v1/global-intimacy-ecosystem",
    tags=["GLOBAL RELATIONSHIP AND INTIMACY ECOSYSTEM"],
)


@router.get("/status", response_model=IntimacyEcosystemStatus)
def ecosystem_status():
    """Describe catalog readiness without implying live provider connections."""
    return get_ecosystem_status()


@router.get("/categories", response_model=list[IntimacyCategory])
def categories():
    """List relationship, intimacy, sexual-health, and adult-industry categories."""
    return list_categories()


@router.get("/providers", response_model=list[IntimacyProvider])
def providers(category_id: str | None = Query(default=None, max_length=64)):
    """List catalog providers, optionally filtered by a category identifier."""
    if category_id:
        key = category_id.strip().upper()
        if key not in {item["category_id"] for item in list_categories()}:
            raise HTTPException(status_code=404, detail="CATEGORY_NOT_FOUND")
    return list_providers(category_id)
