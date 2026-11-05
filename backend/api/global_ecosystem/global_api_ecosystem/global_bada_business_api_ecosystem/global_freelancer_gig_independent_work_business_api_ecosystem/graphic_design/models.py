"""Typed records for graphic_design work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "graphic_design"
    taxonomy_status: str = "taxonomy_only"
