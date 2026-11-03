"""Transport-neutral route handlers for Electrical and mechanical engineering posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "engineering_and_technical", "specialization": "electrical_mechanical_posts", "display_name": "Electrical and mechanical engineering posts"}
