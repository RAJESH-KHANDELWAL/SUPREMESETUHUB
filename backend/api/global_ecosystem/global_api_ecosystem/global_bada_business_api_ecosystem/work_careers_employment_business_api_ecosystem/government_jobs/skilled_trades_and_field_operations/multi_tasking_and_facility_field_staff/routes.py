"""Transport-neutral route handlers for Multi-tasking, facility and field support posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "skilled_trades_and_field_operations", "specialization": "multi_tasking_and_facility_field_staff", "display_name": "Multi-tasking, facility and field support posts"}
