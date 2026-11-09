"""Typed occupation record for agriculture food."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "agriculture_food"
