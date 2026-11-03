"""Adapter access to the canonical Work & Careers employment taxonomy.

No category data is duplicated in this module. Stable category IDs and
definitions remain owned by work_careers_employment_business_api_ecosystem.
"""
from __future__ import annotations

from dataclasses import asdict

from ...work_careers_employment_business_api_ecosystem.catalog import (
    get_category as get_canonical_category,
    list_categories as list_canonical_categories,
    search_categories as search_canonical_categories,
)
from ...work_careers_employment_business_api_ecosystem import DOMAIN_ID as CANONICAL_DOMAIN_ID

CANONICAL_OWNER = "work_careers_employment_business_api_ecosystem"


def list_categories() -> list[dict[str, object]]:
    """Return the canonical employment categories through the industry adapter."""
    return [asdict(item) for item in list_canonical_categories()]


def get_category(category_id: str) -> dict[str, object] | None:
    """Return one canonical employment category by stable ID."""
    item = get_canonical_category(category_id)
    return asdict(item) if item is not None else None


def search_categories(query: str) -> list[dict[str, object]]:
    """Search the canonical employment taxonomy without cloning its records."""
    return [asdict(item) for item in search_canonical_categories(query)]
