"""Canonical taxonomy data for Professional Networking & Talent Communities."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "professional_networking",
    "name": "Professional Networking & Talent Communities",
    "subcategories": [
        "professional_networks",
        "talent_communities",
        "referral_networks",
        "industry_associations"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
