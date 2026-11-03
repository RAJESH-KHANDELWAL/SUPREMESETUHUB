"""Typed records for digital_marketing work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "digital_marketing"
    taxonomy_status: str = "taxonomy_only"
