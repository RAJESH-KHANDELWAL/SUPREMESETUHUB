"""Canonical taxonomy data for Staffing & Placement."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "staffing_and_placement",
    "name": "Staffing & Placement",
    "subcategories": [
        "temporary_staffing",
        "permanent_placement",
        "contract_staffing",
        "recruitment_process_outsourcing"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
