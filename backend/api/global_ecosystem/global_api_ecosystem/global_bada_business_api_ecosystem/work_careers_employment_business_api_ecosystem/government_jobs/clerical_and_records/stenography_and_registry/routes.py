"""Transport-neutral route handlers for Stenography, registry and records posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "clerical_and_records", "specialization": "stenography_and_registry", "display_name": "Stenography, registry and records posts"}
