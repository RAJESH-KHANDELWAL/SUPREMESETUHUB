"""Typed records for virtual_assistance work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "virtual_assistance"
    taxonomy_status: str = "taxonomy_only"
