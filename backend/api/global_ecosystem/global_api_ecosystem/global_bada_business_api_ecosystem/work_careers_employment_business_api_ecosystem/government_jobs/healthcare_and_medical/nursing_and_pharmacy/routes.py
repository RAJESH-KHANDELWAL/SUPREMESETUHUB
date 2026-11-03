"""Transport-neutral route handlers for Nursing and pharmacy posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "healthcare_and_medical", "specialization": "nursing_and_pharmacy", "display_name": "Nursing and pharmacy posts"}
