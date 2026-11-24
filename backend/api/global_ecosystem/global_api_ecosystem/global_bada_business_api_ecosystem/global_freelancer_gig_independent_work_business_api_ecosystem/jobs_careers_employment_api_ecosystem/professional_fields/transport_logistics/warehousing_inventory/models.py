"""Data model for a professional occupation subcategory."""
from dataclasses import dataclass
@dataclass(frozen=True, slots=True)
class ProfessionalSubcategory:
    id: str
    name: str
    description: str
    parent_field_id: str
    taxonomy_status: str = "taxonomy_only"
