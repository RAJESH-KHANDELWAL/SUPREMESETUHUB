"""Transport-neutral route handlers for Traffic, fire and emergency response posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "police_and_public_safety", "specialization": "traffic_fire_and_emergency", "display_name": "Traffic, fire and emergency response posts"}
