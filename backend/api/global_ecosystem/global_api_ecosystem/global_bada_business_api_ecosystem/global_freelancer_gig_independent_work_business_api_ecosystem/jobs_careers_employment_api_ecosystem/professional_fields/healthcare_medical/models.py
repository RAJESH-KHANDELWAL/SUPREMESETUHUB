"""Typed subcategory record for Healthcare & Medical."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Subcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "healthcare_medical"
