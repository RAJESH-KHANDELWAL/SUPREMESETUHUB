"""Compatibility service for the mounted Global Platforms directory."""
from __future__ import annotations

from typing import Any

from ..service import (
    get_ecosystem_status,
    get_platform,
    list_domains,
    search_platforms,
)


def list_platforms(
    query: str | None = None,
    domain: str | None = None,
    country: str | None = None,
    platform_type: str | None = None,
    verification_status: str | None = None,
    include_adult: bool = False,
    limit: int = 50,
    offset: int = 0,
) -> dict[str, Any]:
    """Delegate to the canonical registry; never maintain a second platform store."""
    return search_platforms(
        q=query,
        domain=domain,
        country=country,
        platform_type=platform_type,
        verification_status=verification_status,
        include_adult=include_adult,
        limit=limit,
        offset=offset,
    )


def get_platform_profile(platform_id: str, include_adult: bool = False) -> dict[str, Any] | None:
    return get_platform(platform_id, include_adult=include_adult)


def get_platform_directory_status() -> dict[str, Any]:
    return get_ecosystem_status()


def list_platform_domains(include_adult: bool = False) -> list[dict[str, Any]]:
    return list_domains(include_adult=include_adult)
