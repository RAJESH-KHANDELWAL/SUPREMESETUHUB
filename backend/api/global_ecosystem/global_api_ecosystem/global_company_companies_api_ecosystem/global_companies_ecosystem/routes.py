"""Mounted company-specific profile adapters and aggregate directory routes."""
from importlib import import_module

from fastapi import APIRouter, HTTPException, Query

from .service import (
    COMPANY_ADAPTER_IDS,
    get_company_adapter_status,
    get_company_ecosystem_status,
    get_company_profile,
    get_company_sources,
    list_companies,
)

router = APIRouter(tags=["GLOBAL COMPANY PROFILE ADAPTERS"])
for company_id in COMPANY_ADAPTER_IDS:
    module = import_module(f".{company_id}.routes", package=__package__)
    router.include_router(module.router)


@router.get("/global/company-profile-adapters")
def list_company_profile_adapters(
    q: str | None = Query(default=None),
    limit: int = Query(default=50, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
):
    try:
        return {"success": True, **list_companies(query=q, limit=limit, offset=offset)}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/global/company-profile-adapters/status")
def company_profile_adapter_status():
    return {"success": True, **get_company_ecosystem_status()}


@router.get("/global/company-profile-adapters/{company_id}/sources")
def company_profile_adapter_sources(company_id: str):
    result = get_company_sources(company_id)
    if result is None:
        raise HTTPException(status_code=404, detail="COMPANY_ADAPTER_NOT_FOUND")
    return result


@router.get("/global/company-profile-adapters/{company_id}/adapter-status")
def company_profile_adapter_health(company_id: str):
    result = get_company_adapter_status(company_id)
    if result is None:
        raise HTTPException(status_code=404, detail="COMPANY_ADAPTER_NOT_FOUND")
    return result


@router.get("/global/company-profile-adapters/{company_id}")
def company_profile_adapter_details(company_id: str):
    result = get_company_profile(company_id)
    if result is None:
        raise HTTPException(status_code=404, detail="COMPANY_ADAPTER_NOT_FOUND")
    return result
