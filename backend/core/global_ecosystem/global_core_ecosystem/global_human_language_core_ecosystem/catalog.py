"""Canonical Human Language CORE registry and compatibility facade.

The registry, domain taxonomy and provider inventory are separate sources of
truth. This module composes them without performing provider API calls.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

from .constants import ECOSYSTEM_ID, ECOSYSTEM_NAME, PARENT_ECOSYSTEM_ID, STATUS
from .domain_catalog import (
    DOMAIN_DEFINITIONS, HUMAN_LANGUAGE_DOMAINS, get_domain, get_domains,
    human_language_domain_summary,
)
from .provider_catalog import (
    HUMAN_LANGUAGE_PROVIDERS, get_provider, get_provider_catalog,
    provider_catalog_summary,
)

SERVICE_TIERS = (
    {"tier_id": "NORMAL", "name": "Normal", "rank": 1, "description": "Foundational access and basic discovery."},
    {"tier_id": "BASIC", "name": "Basic", "rank": 2, "description": "Core human-language records and essential tools."},
    {"tier_id": "STANDARD", "name": "Standard", "rank": 3, "description": "Expanded human-language coverage and routine workflows."},
    {"tier_id": "PREMIUM", "name": "Premium", "rank": 4, "description": "Advanced human-language services and quality controls."},
    {"tier_id": "PROFESSIONAL", "name": "Professional", "rank": 5, "description": "Professional-grade workflows, governance and support."},
    {"tier_id": "ENTERPRISE", "name": "Enterprise", "rank": 6, "description": "Organization-scale governance, integrations and administration."},
    {"tier_id": "SUPREME", "name": "Supreme", "rank": 7, "description": "Highest defined service tier, subject to law, rights, safety and actual implementation."},
)

HUMAN_LANGUAGE_CORE_ECOSYSTEM: dict[str, Any] = {
    "ecosystem_id": ECOSYSTEM_ID,
    "name": ECOSYSTEM_NAME,
    "provider": "human_language",
    "ecosystem_type": "GLOBAL_CORE_SERVICE",
    "parent_id": PARENT_ECOSYSTEM_ID,
    "status": STATUS,
    "enabled": True,
    "capabilities": [
        "HUMAN_LANGUAGE_DOMAIN_REGISTRY",
        "BHARAT_AND_GLOBAL_LANGUAGE_TAXONOMY",
        "SCRIPT_AND_LOCALE_METADATA",
        "LANGUAGE_PROVIDER_DISCOVERY",
        "LANGUAGE_SERVICE_CAPABILITY_METADATA",
        "AGE_CONSENT_AND_CONTENT_RIGHTS_POLICY",
    ],
    "children": [
        {
            "ecosystem_id": item["ecosystem_id"],
            "provider_id": item["provider_id"],
            "name": item["name"],
            "provider": item["provider_key"],
            "core_module": f"backend/core/global_ecosystem/global_core_ecosystem/global_human_language_core_ecosystem/{item['folder']}",
            "status": item["status"],
            "enabled": item["enabled"],
            "capabilities": list(item["capabilities"]),
            "live_connection_verified": False,
        }
        for item in HUMAN_LANGUAGE_PROVIDERS
    ],
}


def get_divisions() -> list[dict[str, str]]:
    return [{
        "division_id": "HUMAN-LANGUAGES",
        "name": "HUMAN LANGUAGES",
        "folder": "global_human_language_core_ecosystem",
    }]


def get_service_tiers() -> list[dict[str, Any]]:
    return deepcopy(list(SERVICE_TIERS))


def get_human_language_core_catalog() -> dict[str, Any]:
    return deepcopy(HUMAN_LANGUAGE_CORE_ECOSYSTEM)


def list_human_language_core_modules(include_disabled: bool = False) -> list[dict[str, Any]]:
    modules = deepcopy(HUMAN_LANGUAGE_CORE_ECOSYSTEM["children"])
    if include_disabled:
        return modules
    return [item for item in modules if item.get("enabled", True)]


def get_catalog() -> dict[str, Any]:
    """Return the original combined response shape plus provider registry metadata."""
    domain_summary = human_language_domain_summary()
    provider_summary = provider_catalog_summary()
    return {
        "ecosystem_id": ECOSYSTEM_ID,
        "name": ECOSYSTEM_NAME,
        "parent_id": PARENT_ECOSYSTEM_ID,
        "status": STATUS,
        "division_count": len(get_divisions()),
        "divisions": get_divisions(),
        "domain_count": domain_summary["domain_count"],
        "domains": get_domains(),
        "provider_count": provider_summary["provider_count"],
        "providers": get_provider_catalog(),
        "service_tiers": get_service_tiers(),
        "human_language_coverage_exhaustive": False,
        "provider_coverage_exhaustive": False,
        "live_provider_connections_verified": False,
        "api_calls_performed": 0,
    }
