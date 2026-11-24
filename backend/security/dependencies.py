"""Authentication and authorization dependencies for SUPREMESETUHUB."""

from __future__ import annotations

from typing import Any

from fastapi import Depends, Header, HTTPException

from backend.auth.service import AuthenticationService
from backend.users.controller import UserController

_authentication_service = AuthenticationService()
_user_controller = UserController()


def get_current_user(
    authorization: str | None = Header(default=None, alias="Authorization"),
) -> dict[str, Any]:
    """Validate a Bearer session token and resolve its active user."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="BEARER_TOKEN_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = authorization[len("Bearer "):].strip()
    if not token:
        raise HTTPException(
            status_code=401,
            detail="BEARER_TOKEN_REQUIRED",
            headers={"WWW-Authenticate": "Bearer"},
        )

    try:
        result = _authentication_service.validate_token(token)
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="INVALID_OR_EXPIRED_TOKEN",
            headers={"WWW-Authenticate": "Bearer"},
        ) from None

    if not isinstance(result, dict) or result.get("authenticated") is not True:
        raise HTTPException(
            status_code=401,
            detail="INVALID_OR_EXPIRED_TOKEN",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = result.get("username")
    if not isinstance(username, str) or not username.strip():
        raise HTTPException(status_code=401, detail="TOKEN_USER_NOT_FOUND")

    try:
        user = _user_controller.search(username)
    except Exception:
        raise HTTPException(status_code=503, detail="USER_DIRECTORY_UNAVAILABLE") from None

    if user is None or str(getattr(user, "status", "")).upper() != "ACTIVE":
        raise HTTPException(status_code=401, detail="USER_NOT_ACTIVE")

    role = str(getattr(user, "role", "")).upper()
    if not role:
        raise HTTPException(status_code=403, detail="USER_ROLE_NOT_CONFIGURED")

    return {
        "authenticated": True,
        "username": user.username,
        "user_id": user.user_id,
        "role": role,
        "status": str(user.status).upper(),
        "session_id": result.get("session_id"),
    }


def require_admin(
    current_user: dict[str, Any] = Depends(get_current_user),
) -> dict[str, Any]:
    """Allow only database users with an ADMIN or OWNER role."""
    if current_user.get("role") not in {"ADMIN", "OWNER"}:
        raise HTTPException(status_code=403, detail="ADMIN_ACCESS_REQUIRED")
    return current_user


__all__ = ["get_current_user", "require_admin"]
