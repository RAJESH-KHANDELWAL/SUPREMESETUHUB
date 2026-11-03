"""Transport-neutral route handlers for Software and application development posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "information_technology_and_digital", "specialization": "software_and_application_services", "display_name": "Software and application development posts"}
