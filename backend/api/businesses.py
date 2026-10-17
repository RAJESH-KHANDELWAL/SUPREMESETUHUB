"""Business API routes with explicit authentication and resource authorization."""

from __future__ import annotations

from typing import Any
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException

from backend.businesses.controller import BusinessController
from backend.schemas.business import BusinessCreateRequest, BusinessStatusRequest
from backend.security.dependencies import get_current_user
from backend.supreme.role_governance import role_governance_catalog


router = APIRouter(
    prefix="/businesses",
    tags=["Businesses"],
)

controller = BusinessController()


@router.get("/role-governance/catalog")
def get_role_governance_catalog(
    current_user: dict[str, Any] = Depends(get_current_user),
):
    """Return reusable role/permission templates to authenticated platform users.

    This catalog is for businesses and companies using the platform, not for the
    private SUPREME OWNER ADMIN dashboard. It does not itself grant permissions.
    """
    catalog = role_governance_catalog()
    return {
        **catalog,
        "authenticated_user_id": str(current_user.get("user_id", "")),
        "note": "Templates are available to authenticated users; assignments and business-scoped permission enforcement require separate implemented workflows.",
    }


def _is_admin(user: dict[str, Any]) -> bool:
    return str(user.get("role", "")).upper() in {"ADMIN", "OWNER"}


def _can_manage_business(user: dict[str, Any], business: Any) -> bool:
    return _is_admin(user) or (
        bool(user.get("user_id"))
        and str(getattr(business, "owner_id", "")) == str(user["user_id"])
    )


def _require_business_manager(user: dict[str, Any], business: Any) -> None:
    if not _can_manage_business(user, business):
        # Return 404 rather than reveal another user's resource existence.
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")


@router.get("/")
def get_businesses(
    current_user: dict[str, Any] = Depends(get_current_user),
):
    businesses = controller.list()
    if not _is_admin(current_user):
        user_id = str(current_user.get("user_id", ""))
        businesses = [
            business for business in businesses
            if str(getattr(business, "owner_id", "")) == user_id
        ]

    return {
        "message": "Businesses retrieved successfully",
        "count": len(businesses),
        "data": [business.to_dict() for business in businesses],
    }


@router.get("/{business_id}")
def get_business(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    business = controller.get(business_id)
    if business is None or not _can_manage_business(current_user, business):
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")

    return {
        "message": "Business retrieved successfully",
        "data": business.to_dict(),
    }


@router.post("/")
def create_business(
    request: BusinessCreateRequest,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    owner_id = str(current_user.get("user_id", "")).strip()
    if not owner_id:
        raise HTTPException(status_code=401, detail="AUTHENTICATED_USER_ID_REQUIRED")

    # Never trust client-supplied owner_id, status, or verified values.
    business_id = f"BUS-{uuid4().hex.upper()}"
    business = controller.create(
        business_id=business_id,
        owner_id=owner_id,
        name=request.name,
        category=request.category,
        location=request.location,
        website=request.website,
        public_contact=request.public_contact,
        source=request.source,
        status="ACTIVE",
        verified=False,
        metadata=request.metadata,
    )

    return {
        "message": "Business created successfully",
        "data": business.to_dict(),
    }


@router.put("/{business_id}/status")
def update_business_status(
    business_id: str,
    request: BusinessStatusRequest,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    business = controller.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")
    _require_business_manager(current_user, business)

    status = request.status.strip().upper()
    if not status:
        raise HTTPException(status_code=422, detail="BUSINESS_STATUS_REQUIRED")
    if not _is_admin(current_user) and status not in {"ACTIVE", "INACTIVE"}:
        raise HTTPException(status_code=403, detail="PRIVILEGED_STATUS_CHANGE_REQUIRES_ADMIN")

    business = controller.update_status(business_id=business_id, status=status)
    if business is None:
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")

    return {
        "message": "Business status updated successfully",
        "data": business.to_dict(),
    }


@router.put("/{business_id}/verify")
def verify_business(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    if not _is_admin(current_user):
        raise HTTPException(status_code=403, detail="ADMIN_ACCESS_REQUIRED")

    business = controller.verify(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")

    return {
        "message": "Business verified successfully",
        "data": business.to_dict(),
    }


@router.delete("/{business_id}")
def delete_business(
    business_id: str,
    current_user: dict[str, Any] = Depends(get_current_user),
):
    business = controller.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")
    _require_business_manager(current_user, business)

    deleted = controller.delete(business_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="BUSINESS_NOT_FOUND")

    return {
        "message": "Business deleted successfully",
        "deleted": True,
        "business_id": business_id,
    }
