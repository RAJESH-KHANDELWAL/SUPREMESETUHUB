"""Transport-neutral route handlers for Veterinary, fisheries and rural development posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "agriculture_rural_and_environment", "specialization": "veterinary_fisheries_and_rural_development", "display_name": "Veterinary, fisheries and rural development posts"}
