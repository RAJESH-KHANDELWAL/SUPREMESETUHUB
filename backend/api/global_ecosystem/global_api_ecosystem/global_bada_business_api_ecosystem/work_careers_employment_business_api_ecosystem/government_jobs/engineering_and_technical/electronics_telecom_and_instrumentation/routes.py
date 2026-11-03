"""Transport-neutral route handlers for Electronics, telecom and instrumentation posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "engineering_and_technical", "specialization": "electronics_telecom_and_instrumentation", "display_name": "Electronics, telecom and instrumentation posts"}
