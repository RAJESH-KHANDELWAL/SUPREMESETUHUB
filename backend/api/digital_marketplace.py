"""Public digital catalog and owner-managed listing API."""
from __future__ import annotations

from typing import Literal
from fastapi import APIRouter, Body, HTTPException, Query

from backend.digital_marketplace.service import DigitalMarketplaceService

router = APIRouter(
    prefix="/api/v1/digital-marketplace",
    tags=["SUPREME DIGITAL MARKETPLACE"],
)
service = DigitalMarketplaceService()


@router.get("/catalog")
def get_digital_catalog(
    market: Literal["IN", "GLOBAL"] = Query(default="IN"),
    limit: int = Query(default=24, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    category: str | None = Query(default=None, max_length=80),
    search: str | None = Query(default=None, max_length=100),
):
    """Return published previews and prices only; never expose private file keys."""
    try:
        return {
            "success": True,
            "data": service.catalog(market, limit, offset, category, search),
        }
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.post("/designs", status_code=201)
def save_digital_design(payload: dict = Body(...)):
    """Create/update a draft or publish a listing. Owner-only via private-by-default middleware.

    private_storage_key must reference private storage and must never be a public URL.
    Image generation and file upload are separate integrations; this route only manages
    catalog metadata and pricing.
    """
    try:
        result = service.save_design(payload)
        return {"success": True, "data": result}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
