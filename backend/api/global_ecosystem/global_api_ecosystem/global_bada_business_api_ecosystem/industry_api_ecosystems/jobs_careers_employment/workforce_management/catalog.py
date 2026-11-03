"""Canonical taxonomy data for Workforce Management."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "workforce_management",
    "name": "Workforce Management",
    "subcategories": [
        "workforce_planning",
        "shift_scheduling",
        "attendance_management",
        "field_workforce"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
