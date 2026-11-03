"""Transport-neutral route handlers for Court administration and registry posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "judiciary_and_legal", "specialization": "court_administration_and_registry", "display_name": "Court administration and registry posts"}
