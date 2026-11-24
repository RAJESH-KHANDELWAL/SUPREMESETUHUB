"""Typed response contracts for one industry subcategory."""
from typing import TypedDict


class IndustrySubcategoryResponse(TypedDict):
    id: str
    name: str
    category_id: str
    taxonomy_status: str


class IndustrySubcategoryStatusResponse(TypedDict):
    success: bool
    category_id: str
    subcategory_id: str
    taxonomy_status: str
