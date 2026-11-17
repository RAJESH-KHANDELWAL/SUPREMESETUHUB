
"""Authenticated cross-module view for a single SUPREMESETUHUB identity."""
from __future__ import annotations

from fastapi import APIRouter, Header, HTTPException

from backend.auth.service import AuthenticationService
from backend.identity.controller import IdentityController
from backend.profiles.controller import ProfileController
from backend.businesses.controller import BusinessController
from backend.projects.controller import ProjectController

router = APIRouter(prefix="/user-hub", tags=["User Hub"])

authentication_service = AuthenticationService()
identity_controller = IdentityController()
profile_controller = ProfileController()
business_controller = BusinessController()
project_controller = ProjectController()


@router.get("/{master_id}")
def get_user_hub(
    master_id: str,
    authorization: str | None = Header(default=None),
):
    """Return the signed-in user's profiles, businesses, and projects."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="AUTHORIZATION_REQUIRED",
        )

    token = authorization.removeprefix("Bearer ").strip()
    if not token:
        raise HTTPException(
            status_code=401,
            detail="EMPTY_AUTH_TOKEN",
        )

    auth_result = authentication_service.validate_token(token)

    if not auth_result.get("authenticated"):
        raise HTTPException(
            status_code=401,
            detail="INVALID_AUTHENTICATION_TOKEN",
        )

    username = auth_result.get("username")
    if not username:
        raise HTTPException(
            status_code=401,
            detail="AUTHENTICATED_USERNAME_NOT_FOUND",
        )

    identity = identity_controller.get(master_id)

    if identity is None:
        raise HTTPException(
            status_code=404,
            detail="IDENTITY_NOT_FOUND",
        )

    if (
        (identity.username or "").strip().casefold()
        != str(username).strip().casefold()
    ):
        raise HTTPException(
            status_code=403,
            detail="IDENTITY_ACCESS_FORBIDDEN",
        )

    profiles = profile_controller.list(master_id=master_id)

    businesses = [
        item
        for item in business_controller.list()
        if (item.owner_id or "").strip() == master_id
    ]

    projects = project_controller.list(owner_id=master_id)

    return {
        "success": True,
        "master_id": master_id,
        "data": {
            "profiles": [item.to_dict() for item in profiles],
            "businesses": [item.to_dict() for item in businesses],
            "projects": [item.to_dict() for item in projects],
        },
        "counts": {
            "profiles": len(profiles),
            "businesses": len(businesses),
            "projects": len(projects),
        },
    }
