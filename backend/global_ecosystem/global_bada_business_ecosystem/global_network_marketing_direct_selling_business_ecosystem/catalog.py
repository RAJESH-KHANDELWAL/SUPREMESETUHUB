"""Registry for network-marketing and direct-selling child ecosystems.

The registry records repository namespaces, not legal ownership, approval,
commission terms, earnings, or live integrations.
"""
from __future__ import annotations

from copy import deepcopy
from typing import Any

ECOSYSTEMS: tuple[dict[str, Any], ...] = (
    {
        "id": "global_youtag_business_ecosystem",
        "name": "GLOBAL YOUTAG BUSINESS ECOSYSTEM",
        "category": "direct_selling_and_services",
        "path": "global_youtag_business_ecosystem",
        "platforms": ("youtag_wellness_app", "youtag_recharges_app"),
        "relationship": "one_business_with_multiple_app_platforms",
        "verification_status": "OWNER_PROVIDED_RESOURCE_CATALOG",
    },
    {
        "id": "global_affiliate_marketing_business_ecosystem",
        "name": "GLOBAL AFFILIATE MARKETING BUSINESS ECOSYSTEM",
        "category": "affiliate_marketing",
        "path": "global_affiliate_marketing_business_ecosystem",
        "platforms": ("i_digitalpreneur", "leadsguru", "millionaire_track"),
        "relationship": "independent_platform_namespaces",
        "verification_status": "RESOURCE_CATALOG_REQUIRES_PROVIDER_VERIFICATION",
    },
)


def list_business_ecosystems(*, category: str | None = None) -> tuple[dict[str, Any], ...]:
    """Return defensive copies, optionally filtered by category."""
    records = ECOSYSTEMS
    if category:
        normalized = category.strip().lower()
        records = tuple(item for item in records if item["category"] == normalized)
    return tuple(deepcopy(item) for item in records)


def get_business_ecosystem(ecosystem_id: str) -> dict[str, Any] | None:
    """Find a child ecosystem by stable ID."""
    if not isinstance(ecosystem_id, str):
        return None
    normalized = ecosystem_id.strip().lower()
    for item in ECOSYSTEMS:
        if item["id"] == normalized:
            return deepcopy(item)
    return None


def find_platform(platform_id: str) -> dict[str, Any] | None:
    """Find a platform namespace and its parent ecosystem."""
    if not isinstance(platform_id, str):
        return None
    normalized = platform_id.strip().lower()
    for ecosystem in ECOSYSTEMS:
        if normalized in ecosystem["platforms"]:
            return {
                "platform_id": normalized,
                "parent_ecosystem_id": ecosystem["id"],
                "parent_ecosystem_name": ecosystem["name"],
                "category": ecosystem["category"],
                "verification_status": ecosystem["verification_status"],
            }
    return None


def validate_business_ecosystems() -> tuple[str, ...]:
    """Check stable IDs and prevent a platform being assigned to two parents."""
    errors: list[str] = []
    ecosystem_ids: set[str] = set()
    platform_parents: dict[str, str] = {}
    for ecosystem in ECOSYSTEMS:
        ecosystem_id = ecosystem.get("id")
        if not ecosystem_id or ecosystem_id in ecosystem_ids:
            errors.append(f"missing or duplicate ecosystem id: {ecosystem_id}")
        ecosystem_ids.add(ecosystem_id)
        for platform in ecosystem.get("platforms", ()):
            previous = platform_parents.get(platform)
            if previous:
                errors.append(f"{platform} assigned to both {previous} and {ecosystem_id}")
            platform_parents[platform] = ecosystem_id
    return tuple(errors)
