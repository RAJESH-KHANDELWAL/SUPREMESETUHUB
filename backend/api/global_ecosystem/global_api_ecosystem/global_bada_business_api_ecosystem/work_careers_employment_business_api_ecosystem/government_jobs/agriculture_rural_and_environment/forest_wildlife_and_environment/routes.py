"""Transport-neutral route handlers for Forest, wildlife and environmental posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "agriculture_rural_and_environment", "specialization": "forest_wildlife_and_environment", "display_name": "Forest, wildlife and environmental posts"}
