"""Typed records for delivery_gig_work work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "delivery_gig_work"
    taxonomy_status: str = "taxonomy_only"
