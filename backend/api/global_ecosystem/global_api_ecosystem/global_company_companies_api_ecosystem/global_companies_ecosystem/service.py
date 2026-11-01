"""Aggregate service for the 26 source-aware Company profile adapters.

These are discovery profiles, not verified legal-entity records or live
third-party integrations. Canonical legal/company records remain in the
parent Company registry service.
"""
from __future__ import annotations

from importlib import import_module
from typing import Any

COMPANY_ADAPTER_IDS = (
    "adobe", "alibaba", "amazon", "apple", "atlassian", "aws",
    "bytedance", "cisco", "cloudflare", "github", "google", "ibm",
    "intel", "meta", "microsoft", "netflix", "nvidia", "openai",
    "oracle", "paypal", "salesforce", "samsung", "shopify", "stripe",
    "tencent", "zoom",
)


def _adapter(company_id: str) -> Any | None:
    key = (company_id or "").strip().casefold()
    if key not in COMPANY_ADAPTER_IDS:
        return None
    return import_module(f"{__package__}.{key}")


def list_companies(
    query: str | None = None,
    limit: int = 50,
    offset: int = 0,
) -> dict[str, Any]:
    """List source-aware company adapter profiles with stable pagination."""
    if limit < 1 or limit > 100:
        raise ValueError("limit must be between 1 and 100")
    if offset < 0:
        raise ValueError("offset must be non-negative")

    profiles = []
    term = query.casefold().strip() if query else None
    for company_id in COMPANY_ADAPTER_IDS:
        adapter = _adapter(company_id)
        profile = adapter.get_profile()
        name = str(profile.get("canonical_name") or profile.get("display_name") or company_id)
        if term and term not in company_id and term not in name.casefold():
            continue
        profiles.append(profile)

    profiles.sort(key=lambda item: (
        str(item.get("canonical_name") or item.get("display_name") or "").casefold(),
        str(item.get("company_id", "")),
    ))
    return {
        "total": len(profiles),
        "limit": limit,
        "offset": offset,
        "items": profiles[offset:offset + limit],
        "registry_mode": "source_metadata_only",
        "live_connections": False,
    }


def get_company_profile(company_id: str) -> dict[str, Any] | None:
    adapter = _adapter(company_id)
    return adapter.get_profile() if adapter else None


def get_company_sources(company_id: str) -> dict[str, Any] | None:
    adapter = _adapter(company_id)
    return adapter.get_sources() if adapter else None


def get_company_adapter_status(company_id: str) -> dict[str, Any] | None:
    adapter = _adapter(company_id)
    return adapter.get_adapter_status() if adapter else None


def get_company_ecosystem_status() -> dict[str, Any]:
    adapters = [_adapter(company_id) for company_id in COMPANY_ADAPTER_IDS]
    return {
        "ecosystem": "GLOBAL COMPANY PROFILE ADAPTERS",
        "adapter_count": len(adapters),
        "configured_adapters": sum(bool(item.get_adapter_status().get("configured")) for item in adapters),
        "live_connections": sum(bool(item.get_adapter_status().get("live_connection")) for item in adapters),
        "registry_mode": "source_metadata_only",
        "status": "catalog_ready" if adapters else "empty",
    }
