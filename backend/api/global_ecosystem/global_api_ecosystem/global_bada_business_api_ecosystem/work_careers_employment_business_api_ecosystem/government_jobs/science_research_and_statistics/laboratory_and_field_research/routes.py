"""Transport-neutral route handlers for Laboratory and field research posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "science_research_and_statistics", "specialization": "laboratory_and_field_research", "display_name": "Laboratory and field research posts"}
