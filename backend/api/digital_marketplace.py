"""Public catalog API for the SUPREME digital-only design marketplace."""
from __future__ import annotations

from typing import Literal

from fastapi import APIRouter, HTTPException, Query

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
):
    """Return only published designs and public previews, never private file keys."""
    try:
        return {"success": True, "data": service.catalog(market, limit, offset)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
