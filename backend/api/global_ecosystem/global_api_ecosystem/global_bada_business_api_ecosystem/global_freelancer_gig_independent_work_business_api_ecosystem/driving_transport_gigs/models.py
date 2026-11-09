"""Typed records for driving_transport_gigs work types."""
from dataclasses import dataclass

@dataclass(frozen=True, slots=True)
class WorkType:
    id: str
    name: str
    description: str
    specialization_id: str = "driving_transport_gigs"
    taxonomy_status: str = "taxonomy_only"
