"""Organization CRUD API backed by the existing organization service."""

from __future__ import annotations

from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from backend.organizations.service import OrganizationService
from backend.schemas.organization import (
    OrganizationCreateRequest,
    OrganizationUpdateRequest,
)
from backend.security.dependencies import get_current_user

router = APIRouter(prefix="/organizations", tags=["Organizations"])
service = OrganizationService()


def _initialize() -> None:
    service.initialize()


def _row_to_dict(row) -> dict:
    keys = (
        "organization_id",
        "organization_name",
        "display_name",
        "owner_id",
        "email",
        "phone",
        "website",
        "organization_type",
        "status",
    )
    data = dict(zip(keys, row))
    data.setdefault("verified", False)
    data.setdefault("enabled", data.get("status") == "ACTIVE")
    return data


def _is_admin(user: dict) -> bool:
    return str(user.get("role", "")).upper() in {"ADMIN", "OWNER"}


def _visible_to_user(organization, user: dict) -> bool:
    return _is_admin(user) or str(organization.owner_id or "") == str(
        user.get("user_id", "")
    )


@router.get("/")
def list_organizations(
    current_user: dict = Depends(get_current_user),
):
    _initialize()
    rows = service.get_all_organizations()
    items = [_row_to_dict(row) for row in rows]
    if not _is_admin(current_user):
        owner_id = str(current_user.get("user_id", ""))
        items = [item for item in items if str(item.get("owner_id") or "") == owner_id]
    return {"success": True, "count": len(items), "data": items}


@router.get("/{organization_id}")
def get_organization(
    organization_id: str,
    current_user: dict = Depends(get_current_user),
):
    _initialize()
    organization = service.get_organization(organization_id)
    if organization is None or not _visible_to_user(organization, current_user):
        raise HTTPException(status_code=404, detail="ORGANIZATION_NOT_FOUND")
    return {"success": True, "data": organization.to_dict()}


@router.post("/", status_code=201)
def create_organization(
    payload: OrganizationCreateRequest,
    current_user: dict = Depends(get_current_user),
):
    _initialize()
    organization_id = f"ORG-{uuid4().hex.upper()}"
    owner_id = str(current_user.get("user_id") or "").strip()
    if not owner_id:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")
    organization = service.create_organization(
        organization_id=organization_id,
        organization_name=payload.organization_name.strip(),
        display_name=payload.display_name.strip(),
        owner_id=owner_id,
        email=payload.email,
        phone=payload.phone,
        website=payload.website,
        organization_type=payload.organization_type.strip().upper(),
        status="ACTIVE",
    )
    service.save_organization(organization)
    return {"success": True, "message": "ORGANIZATION_CREATED", "data": organization.to_dict()}


@router.put("/{organization_id}")
def update_organization(
    organization_id: str,
    payload: OrganizationUpdateRequest,
    current_user: dict = Depends(get_current_user),
):
    _initialize()
    existing = service.get_organization(organization_id)
    if existing is None or not _visible_to_user(existing, current_user):
        raise HTTPException(status_code=404, detail="ORGANIZATION_NOT_FOUND")

    # Ownership is server-controlled; clients cannot transfer an organization.
    service.update_organization(
        organization_id=organization_id,
        organization_name=payload.organization_name.strip(),
        display_name=payload.display_name.strip(),
        owner_id=existing.owner_id,
        email=payload.email,
        phone=payload.phone,
        website=payload.website,
        organization_type=payload.organization_type.strip().upper(),
        status=payload.status.strip().upper(),
    )
    updated = service.get_organization(organization_id)
    return {"success": True, "message": "ORGANIZATION_UPDATED", "data": updated.to_dict()}


@router.delete("/{organization_id}")
def delete_organization(
    organization_id: str,
    current_user: dict = Depends(get_current_user),
):
    _initialize()
    existing = service.get_organization(organization_id)
    if existing is None or not _visible_to_user(existing, current_user):
        raise HTTPException(status_code=404, detail="ORGANIZATION_NOT_FOUND")
    service.delete_organization(organization_id)
    return {"success": True, "organization_id": organization_id, "deleted": True}
