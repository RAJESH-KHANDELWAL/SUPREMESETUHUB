"""Typed occupation record for manufacturing operations."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "manufacturing_operations"
