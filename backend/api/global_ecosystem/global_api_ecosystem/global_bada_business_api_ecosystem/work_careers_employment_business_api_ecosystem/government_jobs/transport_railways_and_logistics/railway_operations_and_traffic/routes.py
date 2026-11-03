"""Transport-neutral route handlers for Railway operations and traffic posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "transport_railways_and_logistics", "specialization": "railway_operations_and_traffic", "display_name": "Railway operations and traffic posts"}
