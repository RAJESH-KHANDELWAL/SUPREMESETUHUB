"""Shared, secret-safe readiness helpers for external provider adapters."""
from __future__ import annotations

import os


def present_any(*groups: tuple[str, ...]) -> bool:
    """Return true when at least one complete credential/configuration group exists."""
    return any(all(os.getenv(key, "").strip() for key in group) for group in groups)


def provider_health(
    *,
    provider: str,
    category: str,
    configured: bool,
    auth_method: str,
    required_configuration: list[str],
    capabilities: list[str],
) -> dict:
    """Report configuration without implying live connectivity or exposing secrets."""
    missing = [
        key for key in required_configuration
        if key.isidentifier() and not os.getenv(key, "").strip()
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
            "Configuration is present, but no live provider operation has been verified."
            if configured else
            "Set required server-side environment variables; never commit secrets."
        ),
    }
