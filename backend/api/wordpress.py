"""Owner-only API for registering and connecting live WordPress sites.

Credentials are read only from deployment environment variables.
No WordPress passwords or application passwords belong in GitHub.
"""
from __future__ import annotations

from typing import Optional

from fastapi import APIRouter, Header, HTTPException

from backend.auth.service import AuthenticationService
from backend.supreme.config import USERNAME as SUPREME_OWNER_USERNAME
from backend.wordpress.bootstrap import create_wordpress_service

router = APIRouter(prefix="/api/v1/wordpress", tags=["WordPress"])
wordpress_service = create_wordpress_service()
authentication_service = AuthenticationService()

# Explicit allow-list prevents callers from choosing arbitrary environment names.
SITE_ENV_PREFIXES = {
    "rajeshkhandelwalofficial": "WORDPRESS",
    "drrajeshkhandelwalibc": "DRRAJESHKHANDELWALIBC",
}


def _require_owner(authorization: Optional[str]) -> None:
    """Require a valid bearer token belonging to the SUPREME owner."""
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="AUTHENTICATION_REQUIRED")

    token = authorization[len("Bearer "):].strip()
    if not token:
        raise HTTPException(status_code=401, detail="AUTHENTICATION_REQUIRED")

    try:
        result = authentication_service.validate_token(token)
    except Exception:
        result = None

    if not isinstance(result, dict) or not result.get("authenticated"):
        raise HTTPException(status_code=401, detail="INVALID_OR_EXPIRED_TOKEN")

    username = str(result.get("username", "")).strip()
    if username.casefold() != SUPREME_OWNER_USERNAME.casefold():
        raise HTTPException(status_code=403, detail="WORDPRESS_OWNER_ACCESS_REQUIRED")


@router.get("/status")
def wordpress_status(authorization: Optional[str] = Header(default=None)):
    _require_owner(authorization)
    return {
        "success": True,
        "service": "SUPREMESETUHUB WordPress Bridge",
        "registered_sites": wordpress_service.list_sites().__len__(),
        "connections": wordpress_service.connection_status_all(),
        "credentials_source": "deployment environment variables",
    }


@router.get("/sites")
def wordpress_sites(authorization: Optional[str] = Header(default=None)):
    _require_owner(authorization)
    return {
        "success": True,
        "sites": [site.to_dict() for site in wordpress_service.list_sites()],
    }


@router.post("/sites/{site_id}/connect")
def connect_wordpress_site(
    site_id: str,
    authorization: Optional[str] = Header(default=None),
):
    _require_owner(authorization)
    prefix = SITE_ENV_PREFIXES.get(site_id)
    if prefix is None:
        raise HTTPException(status_code=404, detail="WORDPRESS_SITE_NOT_REGISTERED")
    result = wordpress_service.connect_site(
        site_id=site_id,
        environment_prefix=prefix,
    )
    if not result.get("success"):
        # Do not return raw driver errors or connection details to callers.
        safe_result = {
            key: value for key, value in result.items()
            if key not in {"error", "database", "health"}
        }
        raise HTTPException(status_code=503, detail=safe_result)
    return result


@router.get("/sites/{site_id}/health")
def wordpress_site_health(
    site_id: str,
    authorization: Optional[str] = Header(default=None),
):
    _require_owner(authorization)
    if site_id not in SITE_ENV_PREFIXES:
        raise HTTPException(status_code=404, detail="WORDPRESS_SITE_NOT_REGISTERED")
    return wordpress_service.health(site_id)


@router.get("/sites/{site_id}/tables")
def wordpress_site_tables(
    site_id: str,
    authorization: Optional[str] = Header(default=None),
):
    _require_owner(authorization)
    if site_id not in SITE_ENV_PREFIXES:
        raise HTTPException(status_code=404, detail="WORDPRESS_SITE_NOT_REGISTERED")
    result = wordpress_service.check_wordpress(site_id)
    if not result.get("success"):
        raise HTTPException(status_code=503, detail=result)
    return result


@router.post("/sites/{site_id}/disconnect")
def disconnect_wordpress_site(
    site_id: str,
    authorization: Optional[str] = Header(default=None),
):
    _require_owner(authorization)
    if site_id not in SITE_ENV_PREFIXES:
        raise HTTPException(status_code=404, detail="WORDPRESS_SITE_NOT_REGISTERED")
    return wordpress_service.disconnect_site(site_id)


__all__ = ["router", "wordpress_service"]
