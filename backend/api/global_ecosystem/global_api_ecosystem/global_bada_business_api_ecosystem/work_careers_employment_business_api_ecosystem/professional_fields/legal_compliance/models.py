"""Typed occupation record for legal compliance."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "legal_compliance"
