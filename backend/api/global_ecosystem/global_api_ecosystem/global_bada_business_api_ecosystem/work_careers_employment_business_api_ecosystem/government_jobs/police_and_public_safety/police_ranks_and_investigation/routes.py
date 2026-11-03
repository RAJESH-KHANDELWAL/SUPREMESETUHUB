"""Transport-neutral route handlers for Police rank and investigation posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "police_and_public_safety", "specialization": "police_ranks_and_investigation", "display_name": "Police rank and investigation posts"}
