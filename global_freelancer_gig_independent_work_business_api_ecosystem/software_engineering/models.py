"""Typed records for software_engineering work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "software_engineering"
    taxonomy_status: str = "taxonomy_only"
