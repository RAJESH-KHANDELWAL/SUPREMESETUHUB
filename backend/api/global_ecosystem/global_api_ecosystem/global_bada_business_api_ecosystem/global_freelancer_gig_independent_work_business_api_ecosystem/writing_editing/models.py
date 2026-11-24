"""Typed records for writing_editing work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "writing_editing"
    taxonomy_status: str = "taxonomy_only"
