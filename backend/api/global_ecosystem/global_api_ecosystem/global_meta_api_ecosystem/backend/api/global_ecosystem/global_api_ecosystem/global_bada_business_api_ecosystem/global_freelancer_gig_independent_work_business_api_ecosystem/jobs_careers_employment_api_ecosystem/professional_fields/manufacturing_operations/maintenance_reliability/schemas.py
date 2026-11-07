"""Typed response contracts for a professional occupation subcategory."""
from typing import TypedDict
class ProfessionalSubcategoryResponse(TypedDict):
    id: str
    name: str
    description: str
    parent_field_id: str
    taxonomy_status: str
class ProfessionalSubcategoryStatus(TypedDict):
    success: bool
    api_ecosystem: dict
