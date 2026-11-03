"""Transport-neutral route handlers for Judicial officer recruitment."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "judiciary_and_legal", "specialization": "judicial_officers", "display_name": "Judicial officer recruitment"}
