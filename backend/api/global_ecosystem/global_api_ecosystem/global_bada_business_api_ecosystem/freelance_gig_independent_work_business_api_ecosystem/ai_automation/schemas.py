"""Response schemas for ai_automation."""
from typing import TypedDict

class WorkTypeSchema(TypedDict):
    id: str
    name: str
    description: str
    specialization_id: str
    taxonomy_status: str

class SpecializationStatusSchema(TypedDict):
    success: bool
    specialization_id: str
    work_type_count: int
    taxonomy_status: str
    live_jobs_available: bool
