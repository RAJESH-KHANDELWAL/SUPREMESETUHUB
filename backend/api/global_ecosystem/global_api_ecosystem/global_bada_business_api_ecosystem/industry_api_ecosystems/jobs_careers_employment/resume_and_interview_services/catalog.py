"""Canonical taxonomy data for Resume, Interview & Job Readiness."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "resume_and_interview_services",
    "name": "Resume, Interview & Job Readiness",
    "subcategories": [
        "resume_writing",
        "profile_optimisation",
        "interview_preparation",
        "job_search_support"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
