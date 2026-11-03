"""Transport-neutral route handlers for District and field administration posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "administration_and_secretariat", "specialization": "district_field_administration", "display_name": "District and field administration posts"}
