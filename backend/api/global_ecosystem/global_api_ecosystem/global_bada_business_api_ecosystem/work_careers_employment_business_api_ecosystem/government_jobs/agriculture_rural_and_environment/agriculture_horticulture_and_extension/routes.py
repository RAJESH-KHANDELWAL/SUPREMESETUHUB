"""Transport-neutral route handlers for Agriculture, horticulture and extension posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "agriculture_rural_and_environment", "specialization": "agriculture_horticulture_and_extension", "display_name": "Agriculture, horticulture and extension posts"}
