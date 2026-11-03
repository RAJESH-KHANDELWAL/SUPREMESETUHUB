"""Transport-neutral route handlers for Entry-level clerical and data processing posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "clerical_and_records", "specialization": "lower_division_clerks", "display_name": "Entry-level clerical and data processing posts"}
