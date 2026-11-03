"""Canonical taxonomy data for Human Resources & Payroll."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "human_resources_and_payroll",
    "name": "Human Resources & Payroll",
    "subcategories": [
        "hr_consulting",
        "payroll_services",
        "benefits_administration",
        "hr_technology"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
