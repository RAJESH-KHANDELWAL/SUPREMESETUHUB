"""Transport-neutral route handlers for Other-rank and defence technical trade posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "defence_and_uniformed_services", "specialization": "other_ranks_and_technical_trades", "display_name": "Other-rank and defence technical trade posts"}
