"""Canonical taxonomy data for Career Guidance & Counselling."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "career_guidance_and_counselling",
    "name": "Career Guidance & Counselling",
    "subcategories": [
        "career_assessment",
        "career_coaching",
        "career_transition",
        "workplace_guidance"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
