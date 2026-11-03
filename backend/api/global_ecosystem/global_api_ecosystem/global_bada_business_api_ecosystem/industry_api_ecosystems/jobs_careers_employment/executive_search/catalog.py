"""Canonical taxonomy data for Executive Search & Leadership Hiring."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "executive_search",
    "name": "Executive Search & Leadership Hiring",
    "subcategories": [
        "c_suite_search",
        "board_search",
        "senior_management_hiring",
        "leadership_assessment"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
