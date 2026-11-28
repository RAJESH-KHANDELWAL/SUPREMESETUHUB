"""Read-only catalog and integration-status routes."""

from fastapi import APIRouter, HTTPException, Query

from .schemas import CategorySummary, EcosystemStatus, ProviderStatus
from .service import ecosystem_status, get_category, list_categories, list_providers

router = APIRouter(prefix="/global-communication", tags=["Global Communication"])


@router.get("/status", response_model=EcosystemStatus)
def get_ecosystem_status():
    """Return honest configuration status; no provider is assumed connected."""
    return ecosystem_status()


@router.get("/categories", response_model=list[CategorySummary])
def get_categories(tier: str | None = Query(default=None)):
    return list_categories(tier=tier)


@router.get("/categories/{category_id}", response_model=CategorySummary)
def get_category_detail(category_id: str):
    category = get_category(category_id)
    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.get("/providers", response_model=list[ProviderStatus])
def get_providers():
    return list_providers()
