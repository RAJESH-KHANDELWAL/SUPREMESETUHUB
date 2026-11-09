"""Typed records for bookkeeping_accounting work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "bookkeeping_accounting"
    taxonomy_status: str = "taxonomy_only"
