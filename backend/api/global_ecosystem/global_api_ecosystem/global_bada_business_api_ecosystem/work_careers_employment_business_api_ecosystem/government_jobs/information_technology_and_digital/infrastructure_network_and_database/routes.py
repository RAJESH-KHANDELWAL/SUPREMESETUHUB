"""Transport-neutral route handlers for IT infrastructure and database posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "information_technology_and_digital", "specialization": "infrastructure_network_and_database", "display_name": "IT infrastructure and database posts"}
