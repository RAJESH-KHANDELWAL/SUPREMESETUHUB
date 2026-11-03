"""Transport-neutral route handlers for Commissioned and junior commissioned officer routes."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "defence_and_uniformed_services", "specialization": "commissioned_and_junior_officers", "display_name": "Commissioned and junior commissioned officer routes"}
