"""Stable response schema for agriculture_food occupation taxonomy."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class ProfessionalSubcategorySchema:
    id: str
    name: str
    description: str
    parent_field_id: str
    api_ecosystem_id: str
    taxonomy_status: str = "taxonomy_only"
