"""Canonical taxonomy data for Labour & Employment Compliance."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "employment_compliance",
    "name": "Labour & Employment Compliance",
    "subcategories": [
        "employment_contracts",
        "workplace_policies",
        "labour_compliance_advisory",
        "workplace_safety_training"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
