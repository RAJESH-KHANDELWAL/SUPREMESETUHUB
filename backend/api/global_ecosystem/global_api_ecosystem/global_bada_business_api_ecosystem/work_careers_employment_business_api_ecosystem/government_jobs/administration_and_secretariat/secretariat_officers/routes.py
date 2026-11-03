"""Transport-neutral route handlers for Secretariat and section officer posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "administration_and_secretariat", "specialization": "secretariat_officers", "display_name": "Secretariat and section officer posts"}
