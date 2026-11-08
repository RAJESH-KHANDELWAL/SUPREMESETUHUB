"""Read-only Hostinger API client for the SUPREMESETUHUB backend.

Only documented GET inventory endpoints are exposed here. This module does not
buy plans, register/transfer domains, change DNS, deploy files, or mutate VPS
state. Credentials must be supplied through the deployment secret manager.
"""
from __future__ import annotations

import os
from typing import Any

import httpx

HOSTINGER_API_BASE_URL = "https://developers.hostinger.com"
REQUEST_TIMEOUT_SECONDS = 10.0


class HostingerConfigurationError(RuntimeError):
    """Raised when no Hostinger API token is configured."""


class HostingerAPIError(RuntimeError):
    """Raised for sanitized Hostinger API failures."""


def _api_token() -> str:
    # HOSTINGER_API_TOKEN is the current documented name. Keep API_KEY as a
    # backwards-compatible alias for the initial catalog branch.
    token = (
        os.getenv("HOSTINGER_API_TOKEN", "").strip()
        or os.getenv("HOSTINGER_API_KEY", "").strip()
    )
    if not token:
        raise HostingerConfigurationError("HOSTINGER_API_TOKEN_NOT_CONFIGURED")
    return token


def _get(path: str, params: dict[str, Any] | None = None) -> Any:
    if not path.startswith("/api/"):
        raise ValueError("HOSTINGER_PATH_MUST_BE_API_RELATIVE")
    try:
        response = httpx.get(
            f"{HOSTINGER_API_BASE_URL}{path}",
            headers={
                "Authorization": f"Bearer {_api_token()}",
                "Accept": "application/json",
                "Content-Type": "application/json",
            },
            params=params,
            timeout=REQUEST_TIMEOUT_SECONDS,
        )
    except HostingerConfigurationError:
        raise
    except httpx.HTTPError as exc:
        raise HostingerAPIError("HOSTINGER_API_NETWORK_ERROR") from exc

    if response.status_code == 401:
        raise HostingerAPIError("HOSTINGER_API_UNAUTHORIZED")
    if response.status_code == 403:
        raise HostingerAPIError("HOSTINGER_API_FORBIDDEN")
    if response.status_code == 429:
        raise HostingerAPIError("HOSTINGER_API_RATE_LIMITED")
    if response.status_code >= 500:
        raise HostingerAPIError("HOSTINGER_API_UPSTREAM_ERROR")
    if response.status_code >= 400:
        raise HostingerAPIError(f"HOSTINGER_API_HTTP_{response.status_code}")

    try:
        return response.json()
    except ValueError as exc:
        raise HostingerAPIError("HOSTINGER_API_INVALID_JSON") from exc


def list_websites(page: int = 1) -> dict[str, Any]:
    """List websites available to the authenticated Hostinger account."""
    return {
        "success": True,
        "provider": "hostinger",
        "resource": "websites",
        "data": _get("/api/hosting/v1/websites", {"page": page}),
    }


def list_vps_instances(page: int = 1) -> dict[str, Any]:
    """List VPS instances available to the authenticated Hostinger account."""
    return {
        "success": True,
        "provider": "hostinger",
        "resource": "vps_instances",
        "data": _get("/api/vps/v1/virtual-machines", {"page": page}),
    }


def connection_status() -> dict[str, Any]:
    """Verify credentials with a read-only request; never return token material."""
    try:
        result = _get("/api/hosting/v1/websites", {"page": 1})
        return {
            "success": True,
            "provider": "hostinger",
            "status": "CONNECTED",
            "authentication": "VALID_FOR_WEBSITE_INVENTORY",
            "live_api_test_performed": True,
            "sample_resource": "websites",
            "sample_result_type": type(result).__name__,
            "secrets_returned": False,
            "mutations_performed": False,
        }
    except HostingerConfigurationError:
        return {
            "success": True,
            "provider": "hostinger",
            "status": "NOT_CONFIGURED",
            "live_api_test_performed": False,
            "secrets_returned": False,
            "mutations_performed": False,
        }
    except HostingerAPIError as exc:
        return {
            "success": False,
            "provider": "hostinger",
            "status": "CONNECTION_FAILED",
            "error": str(exc),
            "live_api_test_performed": True,
            "secrets_returned": False,
            "mutations_performed": False,
        }
