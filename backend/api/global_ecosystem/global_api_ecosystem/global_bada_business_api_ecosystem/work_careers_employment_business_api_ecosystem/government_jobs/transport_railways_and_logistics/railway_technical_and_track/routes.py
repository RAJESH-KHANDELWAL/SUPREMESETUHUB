"""Transport-neutral route handlers for Railway technical, signalling and track posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "transport_railways_and_logistics", "specialization": "railway_technical_and_track", "display_name": "Railway technical, signalling and track posts"}
