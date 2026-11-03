"""Transport-neutral route handlers for Cybersecurity and digital governance posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "information_technology_and_digital", "specialization": "cybersecurity_and_digital_governance", "display_name": "Cybersecurity and digital governance posts"}
