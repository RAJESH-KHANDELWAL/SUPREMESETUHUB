"""Service facade for the software_engineering specialization catalogue."""
from .catalog import list_work_types, get_work_type, search_work_types
from . import SPECIALIZATION_ID, SPECIALIZATION_NAME, DESCRIPTION

def get_specialization_resource():
    return {"id": SPECIALIZATION_ID, "name": SPECIALIZATION_NAME, "description": DESCRIPTION, "work_types": [item.__dict__ if hasattr(item, "__dict__") else {"id": item.id, "name": item.name, "description": item.description, "specialization_id": item.specialization_id, "taxonomy_status": item.taxonomy_status} for item in list_work_types()], "taxonomy_status": "taxonomy_only", "live_jobs_available": False}

def get_status():
    return {"success": True, "specialization_id": SPECIALIZATION_ID, "work_type_count": len(list_work_types()), "taxonomy_status": "taxonomy_only", "live_jobs_available": False}
