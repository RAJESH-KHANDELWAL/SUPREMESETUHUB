"""Typed records for coaching_training work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "coaching_training"
    taxonomy_status: str = "taxonomy_only"
