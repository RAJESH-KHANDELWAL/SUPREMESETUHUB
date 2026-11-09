"""Typed records for professional_contracting work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "professional_contracting"
    taxonomy_status: str = "taxonomy_only"
