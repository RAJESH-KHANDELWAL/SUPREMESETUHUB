"""Response contracts for one freelance work-type package."""
from typing import TypedDict


class WorkTypeResponse(TypedDict):
    id: str
    name: str
    description: str
    specialization_id: str
    taxonomy_status: str


class WorkTypeStatusResponse(TypedDict):
    success: bool
    specialization_id: str
    work_type_id: str
    taxonomy_status: str
    live_gig_available: bool
