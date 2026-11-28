"""Authenticated API for central multi-tenant spaces and website gates."""
from __future__ import annotations

from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field

from backend.security.dependencies import get_current_user
from backend.tenancy.service import (
    SUPPORTED_SITES,
    TenantNotFoundError,
    TenantService,
    TenantValidationError,
)

router = APIRouter(prefix="/api/v1/tenancy", tags=["Multi-tenant access"])
service = TenantService()


class SiteBindingInput(BaseModel):
    site_id: str
    gate_count: int = Field(default=1)


class TenantCreateInput(BaseModel):
    tenant_name: str = Field(min_length=2, max_length=160)
    tenant_type: str = Field(default="BUSINESS", min_length=2, max_length=48)
    site_bindings: list[SiteBindingInput] = Field(min_length=1, max_length=2)


class TenantMemberInput(BaseModel):
    user_id: str = Field(min_length=1, max_length=128)
    gate_level: int = Field(ge=1, le=4)


class TenantRecordInput(BaseModel):
    domain_key: str = Field(min_length=1, max_length=100)
    record_type: str = Field(min_length=1, max_length=100)
    min_gate: int = Field(default=1, ge=1, le=4)
    payload: dict[str, Any]


def _user_id(current_user: dict) -> str:
    value = str(current_user.get("user_id") or "").strip()
    if not value:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    return value


def _is_admin(current_user: dict) -> bool:
    return str(current_user.get("role", "")).upper() in {"ADMIN", "OWNER"}


def _require_tenant_owner(tenant_id: str, current_user: dict) -> dict:
    tenant = service.get_tenant(tenant_id)
    if tenant is None:
        raise HTTPException(status_code=404, detail="TENANT_NOT_FOUND")
    if tenant["owner_user_id"] != _user_id(current_user) and not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="TENANT_OWNER_ACCESS_REQUIRED")
    return tenant


def _require_site_membership(tenant_id: str, site_id: str, current_user: dict) -> dict:
    try:
        membership = service.get_membership(tenant_id, site_id, _user_id(current_user))
    except TenantValidationError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    if membership is None:
        raise HTTPException(status_code=403, detail="TENANT_SITE_MEMBERSHIP_REQUIRED")
    return membership


@router.get("/sites")
def supported_sites(current_user: dict = Depends(get_current_user)):
    return {
        "success": True,
        "sites": [
            {"site_id": site_id, "domain": domain}
            for site_id, domain in SUPPORTED_SITES.items()
        ],
        "gate_counts": [1, 2, 4],
    }


@router.get("/sites/{site_id}/spaces")
def list_site_spaces(
    site_id: str,
    current_user: dict = Depends(get_current_user),
):
    try:
        spaces = service.list_site_spaces(_user_id(current_user), site_id)
    except TenantValidationError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"success": True, "site_id": site_id, "count": len(spaces), "spaces": spaces}


@router.get("/tenants")
def list_my_tenants(current_user: dict = Depends(get_current_user)):
    items = service.list_tenants_for_user(_user_id(current_user))
    return {"success": True, "count": len(items), "tenants": items}


@router.post("/tenants", status_code=201)
def create_tenant(
    payload: TenantCreateInput,
    current_user: dict = Depends(get_current_user),
):
    try:
        tenant = service.create_tenant(
            tenant_name=payload.tenant_name,
            tenant_type=payload.tenant_type,
            owner_user_id=_user_id(current_user),
            site_bindings=[item.model_dump() for item in payload.site_bindings],
        )
    except TenantValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"success": True, "message": "TENANT_CREATED", "tenant": tenant}


@router.get("/tenants/{tenant_id}")
def get_tenant(
    tenant_id: str,
    current_user: dict = Depends(get_current_user),
):
    tenant = service.get_tenant(tenant_id)
    if tenant is None:
        raise HTTPException(status_code=404, detail="TENANT_NOT_FOUND")
    if tenant["owner_user_id"] != _user_id(current_user):
        membership = service.list_tenants_for_user(_user_id(current_user))
        if not any(item["tenant_id"] == tenant_id for item in membership):
            raise HTTPException(status_code=404, detail="TENANT_NOT_FOUND")
    return {"success": True, "tenant": tenant}


@router.get("/tenants/{tenant_id}/sites/{site_id}/members")
def list_members(
    tenant_id: str,
    site_id: str,
    current_user: dict = Depends(get_current_user),
):
    _require_tenant_owner(tenant_id, current_user)
    try:
        members = service.list_members(tenant_id, site_id)
    except TenantValidationError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    return {"success": True, "members": members}


@router.post("/tenants/{tenant_id}/sites/{site_id}/members")
def add_member(
    tenant_id: str,
    site_id: str,
    payload: TenantMemberInput,
    current_user: dict = Depends(get_current_user),
):
    _require_tenant_owner(tenant_id, current_user)
    try:
        member = service.add_member(tenant_id, site_id, payload.user_id, payload.gate_level)
    except TenantNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except TenantValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"success": True, "message": "MEMBER_ACCESS_CONFIGURED", "membership": member}


@router.get("/tenants/{tenant_id}/sites/{site_id}/records")
def list_records(
    tenant_id: str,
    site_id: str,
    domain_key: str | None = None,
    record_type: str | None = None,
    current_user: dict = Depends(get_current_user),
):
    membership = _require_site_membership(tenant_id, site_id, current_user)
    records = service.list_records(
        tenant_id, site_id, int(membership["gate_level"]), domain_key, record_type
    )
    return {
        "success": True,
        "tenant_id": tenant_id,
        "site_id": site_id,
        "gate_level": membership["gate_level"],
        "count": len(records),
        "records": records,
    }


@router.post("/tenants/{tenant_id}/sites/{site_id}/records", status_code=201)
def create_record(
    tenant_id: str,
    site_id: str,
    payload: TenantRecordInput,
    current_user: dict = Depends(get_current_user),
):
    membership = _require_site_membership(tenant_id, site_id, current_user)
    if int(membership["gate_level"]) < payload.min_gate:
        raise HTTPException(status_code=403, detail="INSUFFICIENT_GATE_LEVEL")
    try:
        record = service.create_record(
            tenant_id=tenant_id,
            site_id=site_id,
            domain_key=payload.domain_key,
            record_type=payload.record_type,
            min_gate=payload.min_gate,
            payload=payload.payload,
            created_by=_user_id(current_user),
        )
    except TenantNotFoundError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc
    except TenantValidationError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return {"success": True, "message": "TENANT_RECORD_CREATED", "record": record}


__all__ = ["router", "service"]
