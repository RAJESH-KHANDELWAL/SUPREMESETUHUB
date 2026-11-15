"""Typed records for professional fields and subcategories."""
from dataclasses import dataclass
from typing import Tuple

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str

@dataclass(frozen=True, slots=True)
class ProfessionalField:
    id: str
    name: str
    description: str
    subcategories: Tuple[ProfessionalSubcategory, ...]
