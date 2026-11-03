"""Canonical taxonomy data for Remote & Hybrid Work."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "remote_and_hybrid_work",
    "name": "Remote & Hybrid Work",
    "subcategories": [
        "fully_remote_jobs",
        "hybrid_roles",
        "cross_border_remote_work",
        "distributed_teams"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
