"""Typed response contracts for an industry category."""
from typing import TypedDict


class IndustryCategoryResponse(TypedDict):
    id: str
    name: str
    subcategories: list[str]
    taxonomy_status: str


class IndustryCategoryStatusResponse(TypedDict):
    success: bool
    category_id: str
    subcategory_count: int
    taxonomy_status: str
