"""Canonical taxonomy data for Internships & Apprenticeships."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "internships_and_apprenticeships",
    "name": "Internships & Apprenticeships",
    "subcategories": [
        "student_internships",
        "graduate_programmes",
        "trade_apprenticeships",
        "returnships"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
