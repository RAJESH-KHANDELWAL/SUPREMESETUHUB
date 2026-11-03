"""Canonical taxonomy data for Outsourcing & Business Process Services."""
from __future__ import annotations
from copy import deepcopy

CATEGORY: dict[str, object] = {
    "id": "outsourcing_and_bpo",
    "name": "Outsourcing & Business Process Services",
    "subcategories": [
        "business_process_outsourcing",
        "customer_support_operations",
        "knowledge_process_outsourcing",
        "staff_augmentation"
    ]
}

def get_category() -> dict[str, object]:
    """Return an isolated copy of this category definition."""
    return deepcopy(CATEGORY)
