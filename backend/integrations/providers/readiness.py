"""Shared, secret-safe readiness helpers for external provider adapters."""
from __future__ import annotations

import os
from typing import Iterable


def present_any(*groups: Iterable[str]) -> bool:
    """Return true when at least one complete credential/configuration group exists."""
    return any(
        all(os.getenv(key, "").strip() for key in group)
        for group in groups
    )


def provider_health(
    *,
    provider: str,
    category: str,
    configured: bool,
    auth_method: str,
    required_configuration: list[str],
    capabilities: list[str],
) -> dict:
    """Report configuration state without implying a live connection.

    Never return environment values, credential fragments, or private keys.
    A real adapter must run an authorized provider-specific probe before it may
    report a connected state.
    """
    missing = [
        key for key in required_configuration
        if not os.getenv(key, "").strip()
    ]
    return {
        "provider": provider,
        "category": category,
        "status": "CONFIGURED_NOT_VERIFIED" if configured else "NEEDS_CONFIGURATION",
        "authentication": "CONFIGURED" if configured else "NOT_CONFIGURED",
        "connection": "NOT_TESTED",
        "live_connection_verified": False,
        "auth_method": auth_method,
        "capabilities": capabilities,
        "missing_configuration": missing,
        "note": (
            "Credentials are detected but no live provider operation has been verified."
            if configured else
            "Set the required server-side environment variables; never commit secrets."
        ),
    }
