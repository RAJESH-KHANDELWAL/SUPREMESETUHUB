"""Transport-neutral route handlers for Medical officer and specialist posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "healthcare_and_medical", "specialization": "medical_officers_and_specialists", "display_name": "Medical officer and specialist posts"}
