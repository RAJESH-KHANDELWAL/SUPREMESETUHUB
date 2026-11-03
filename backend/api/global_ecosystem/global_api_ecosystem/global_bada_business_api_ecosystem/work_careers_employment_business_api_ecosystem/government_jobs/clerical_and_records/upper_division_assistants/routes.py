"""Transport-neutral route handlers for Senior clerical and establishment posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "clerical_and_records", "specialization": "upper_division_assistants", "display_name": "Senior clerical and establishment posts"}
