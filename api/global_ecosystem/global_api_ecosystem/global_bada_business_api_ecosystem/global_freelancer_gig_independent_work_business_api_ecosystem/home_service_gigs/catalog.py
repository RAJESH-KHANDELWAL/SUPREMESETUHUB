"""List, detail and search operations for home_service_gigs work types."""
from .models import WorkType
from .work_types import WORK_TYPES

WORK_TYPE_RECORDS = tuple(WorkType(**item) for item in WORK_TYPES)

def list_work_types():
    return list(WORK_TYPE_RECORDS)

def get_work_type(work_type_id: str):
    return next((item for item in WORK_TYPE_RECORDS if item.id == work_type_id), None)

def search_work_types(query: str):
    needle = query.strip().casefold()
    if not needle:
        return []
    return [item for item in WORK_TYPE_RECORDS if needle in item.id.casefold() or needle in item.name.casefold() or needle in item.description.casefold()]
