"""Typed occupation record for real estate facilities."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "real_estate_facilities"
