"""Typed subcategory record for Education & Training."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class Subcategory:
    id: str
    name: str
    description: str
    parent_field_id: str = "education_training"
