"""Authenticated SUPREME PRINT ON DEMAND API routes."""
from __future__ import annotations

from typing import Any, Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from backend.print_on_demand.controller import PrintOnDemandController
from backend.security.dependencies import get_current_user

router = APIRouter(prefix="/api/v1/print-on-demand", tags=["SUPREME PRINT ON DEMAND"])
controller = PrintOnDemandController()

class QuoteRequest(BaseModel):
    product_sku: str = Field(min_length=1, max_length=40)
    market: Literal["IN", "GLOBAL"] = "IN"
    tier: Literal["STANDARD", "PREMIUM"] = "STANDARD"
    demand_score: int = Field(default=3, ge=1, le=5)
    quantity: int = Field(default=1, ge=1, le=100)

class DesignBriefRequest(QuoteRequest):
    design_prompt: str = Field(min_length=1, max_length=600)
    notes: str = Field(default="", max_length=1000)

@router.get("/catalog")
def get_catalog(
    market: Literal["IN", "GLOBAL"] = Query(default="IN"),
    current_user: dict[str, Any] = Depends(get_current_user),
):
    try:
        return {"success": True, "data": controller.catalog(market)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.post("/quote")
def get_quote(
    request: QuoteRequest,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    try:
        quote = controller.quote(**request.model_dump())
        return {"success": True, "data": quote}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.post("/design-briefs", status_code=201)
def create_design_brief(
    request: DesignBriefRequest,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    user_id = str(current_user.get("user_id", "")).strip()
    if not user_id:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    try:
        result = controller.create_brief(user_id=user_id, **request.model_dump())
        return {"success": True, "data": result}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc

@router.get("/design-briefs")
def get_my_design_briefs(
    current_user: dict[str, Any] = Depends(get_current_user),
):
    user_id = str(current_user.get("user_id", "")).strip()
    if not user_id:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    briefs = controller.list_briefs(user_id)
    return {"success": True, "count": len(briefs), "data": briefs}
