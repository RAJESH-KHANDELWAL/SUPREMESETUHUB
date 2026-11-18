"""FastAPI routes for the social media provider directory."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from .service import get_ecosystem_overview, get_provider_detail, get_provider_directory

router = APIRouter(prefix="/social-media", tags=["Global Social Media Ecosystem"])

@router.get("/")
def ecosystem_overview():
    return get_ecosystem_overview()

@router.get("/providers")
def providers(
    region: str | None = Query(default=None),
    category: str | None = Query(default=None),
):
    return get_provider_directory(region=region, category=category)

@router.get("/providers/{provider_id}")
def provider_detail(provider_id: str):
    provider = get_provider_detail(provider_id)
    if provider is None:
        raise HTTPException(status_code=404, detail="Social media provider not found")
    return provider

__all__ = ["router"]
