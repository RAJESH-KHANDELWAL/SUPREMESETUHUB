"""Canonical taxonomy data for Freelancing & Gig Work."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "freelancing_and_gig_work",
    "name": "Freelancing & Gig Work",
    "subcategories": [
        "freelance_marketplaces",
        "independent_contracting",
        "gig_platforms",
        "project_based_work"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
