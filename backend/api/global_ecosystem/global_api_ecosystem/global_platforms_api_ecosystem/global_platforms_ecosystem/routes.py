"""Mounted directory routes for the canonical Global Platforms registry."""
from fastapi import APIRouter, HTTPException, Query

from .service import (
    get_platform_directory_status,
    get_platform_profile,
    list_platforms,
    list_platform_domains,
)

router = APIRouter(prefix="/directory", tags=["GLOBAL PLATFORM DIRECTORY"])


@router.get("/status")
def directory_status():
    return {"success": True, **get_platform_directory_status()}


@router.get("/domains")
def directory_domains(include_adult: bool = Query(default=False)):
    domains = list_platform_domains(include_adult=include_adult)
    return {
        "success": True,
        "count": len(domains),
        "include_adult": include_adult,
        "domains": domains,
    }


@router.get("")
def directory_list(
    q: str | None = Query(default=None),
    domain: str | None = Query(default=None),
    country: str | None = Query(default=None, min_length=2, max_length=2),
    platform_type: str | None = Query(default=None),
    verification_status: str | None = Query(default=None),
    include_adult: bool = Query(default=False),
    limit: int = Query(default=50, ge=1, le=200),
    offset: int = Query(default=0, ge=0),
):
    try:
        return {"success": True, **list_platforms(
            query=q,
            domain=domain,
            country=country,
            platform_type=platform_type,
            verification_status=verification_status,
            include_adult=include_adult,
            limit=limit,
            offset=offset,
        )}
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc


@router.get("/{platform_id}")
def directory_detail(
    platform_id: str,
    include_adult: bool = Query(default=False),
):
    profile = get_platform_profile(platform_id, include_adult=include_adult)
    if profile is None:
        raise HTTPException(status_code=404, detail="PLATFORM_NOT_FOUND")
    return {"success": True, "item": profile}
