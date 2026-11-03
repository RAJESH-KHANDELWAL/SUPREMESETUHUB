"""Canonical taxonomy data for Employer Branding & Talent Marketing."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "employer_branding",
    "name": "Employer Branding & Talent Marketing",
    "subcategories": [
        "employer_value_proposition",
        "talent_campaigns",
        "candidate_experience",
        "recruitment_marketing"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
