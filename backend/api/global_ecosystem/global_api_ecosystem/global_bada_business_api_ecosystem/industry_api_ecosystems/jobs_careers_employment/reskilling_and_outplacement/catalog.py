"""Canonical taxonomy data for Reskilling & Outplacement."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "reskilling_and_outplacement",
    "name": "Reskilling & Outplacement",
    "subcategories": [
        "career_reskilling",
        "redeployment_support",
        "outplacement_services",
        "workforce_transition"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
