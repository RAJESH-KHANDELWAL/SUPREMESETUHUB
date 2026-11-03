"""Transport-neutral route handlers for Prosecution and government legal posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "judiciary_and_legal", "specialization": "prosecution_and_government_legal", "display_name": "Prosecution and government legal posts"}
