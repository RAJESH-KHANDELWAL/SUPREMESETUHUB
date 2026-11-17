"""Typed records for data_analysis work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "data_analysis"
    taxonomy_status: str = "taxonomy_only"
