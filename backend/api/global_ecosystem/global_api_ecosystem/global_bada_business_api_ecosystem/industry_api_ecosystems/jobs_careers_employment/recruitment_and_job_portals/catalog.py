"""Canonical taxonomy data for Recruitment & Job Portals."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "recruitment_and_job_portals",
    "name": "Recruitment & Job Portals",
    "subcategories": [
        "job_boards",
        "employer_job_sites",
        "executive_vacancies",
        "campus_recruitment"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
