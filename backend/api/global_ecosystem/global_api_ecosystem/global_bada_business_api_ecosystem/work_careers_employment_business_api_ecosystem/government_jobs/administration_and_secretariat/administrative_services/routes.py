"""Transport-neutral route handlers for Civil and allied administrative service posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "administration_and_secretariat", "specialization": "administrative_services", "display_name": "Civil and allied administrative service posts"}
