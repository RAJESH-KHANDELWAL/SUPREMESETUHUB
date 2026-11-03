"""Transport-neutral route handlers for Prison, forensic and intelligence support posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "police_and_public_safety", "specialization": "prisons_forensics_and_intelligence_support", "display_name": "Prison, forensic and intelligence support posts"}
