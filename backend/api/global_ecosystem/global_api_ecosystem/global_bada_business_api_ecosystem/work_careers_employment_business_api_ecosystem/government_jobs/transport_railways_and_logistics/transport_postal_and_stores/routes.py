"""Transport-neutral route handlers for Transport, postal and government logistics posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "transport_railways_and_logistics", "specialization": "transport_postal_and_stores", "display_name": "Transport, postal and government logistics posts"}
