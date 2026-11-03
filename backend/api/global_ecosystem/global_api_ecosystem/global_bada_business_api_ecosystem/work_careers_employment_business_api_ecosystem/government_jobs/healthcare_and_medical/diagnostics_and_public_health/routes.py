"""Transport-neutral route handlers for Diagnostic and public health posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "healthcare_and_medical", "specialization": "diagnostics_and_public_health", "display_name": "Diagnostic and public health posts"}
