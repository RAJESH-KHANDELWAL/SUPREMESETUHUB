"""Transport-neutral route handlers for Civilian defence establishment posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "defence_and_uniformed_services", "specialization": "civilian_defence_support", "display_name": "Civilian defence establishment posts"}
