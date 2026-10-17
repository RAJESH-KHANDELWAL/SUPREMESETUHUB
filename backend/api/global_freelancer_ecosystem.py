"""GLOBAL FREELANCER ECOSYSTEM API.

This first foundation release provides catalog/status plus owner-scoped metadata
records. It does not create jobs, submit applications, handle payments, or claim
that external marketplace providers are connected.
"""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel, Field

from backend.engines.freelancer_ecosystem.manager import FreelancerEcosystemEngine
from backend.security.dependencies import get_current_user


router = APIRouter(
    prefix="/api/v1/global-freelancer-ecosystem",
    tags=["GLOBAL FREELANCER ECOSYSTEM"],
)


class FreelancerRecordCreate(BaseModel):
    record_type: str = Field(min_length=1, max_length=40)
    title: str = Field(min_length=1, max_length=180)
    payload: dict[str, Any] = Field(default_factory=dict)
    storage_asset_ids: list[str] = Field(default_factory=list, max_length=50)
    status: str = Field(default="DRAFT", max_length=20)


def _actor_id(current_user: dict[str, Any]) -> str:
    actor = str(current_user.get("user_id") or current_user.get("id") or "").strip()
    if not actor:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return actor


def _engine() -> FreelancerEcosystemEngine:
    return FreelancerEcosystemEngine()


@router.get("/status")
def freelancer_ecosystem_status() -> dict[str, Any]:
    return _engine().status()


@router.get("/catalog")
def freelancer_ecosystem_catalog() -> dict[str, Any]:
    return {"success": True, **_engine().catalog()}


@router.get("/records")
def list_freelancer_records(
    record_type: str | None = Query(default=None, max_length=40),
    limit: int = Query(default=50, ge=1, le=100),
    current_user: dict[str, Any] = Depends(get_current_user),
) -> dict[str, Any]:
    try:
        records = _engine().list_records(
            owner_id=_actor_id(current_user),
            record_type=record_type,
            limit=limit,
        )
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"success": True, "count": len(records), "records": records}


@router.post("/records", status_code=201)
def create_freelancer_record(
    request: FreelancerRecordCreate,
    current_user: dict[str, Any] = Depends(get_current_user),
) -> dict[str, Any]:
    try:
        record = _engine().create_record(
            owner_id=_actor_id(current_user),
            record_type=request.record_type,
            title=request.title,
            payload=request.payload,
            storage_asset_ids=request.storage_asset_ids,
            status=request.status,
        )
    except PermissionError as exc:
        raise HTTPException(status_code=403, detail="STORAGE_ASSET_ACCESS_DENIED") from exc
    except ValueError as exc:
        raise HTTPException(status_code=422, detail=str(exc)) from exc
    return {"success": True, "record": record}


@router.get("/records/{record_id}")
def get_freelancer_record(
    record_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
) -> dict[str, Any]:
    record = _engine().get_record(record_id, owner_id=_actor_id(current_user))
    if record is None:
        # Do not reveal whether another user's record exists.
        raise HTTPException(status_code=404, detail="FREELANCER_RECORD_NOT_FOUND")
    return {"success": True, "record": record}
