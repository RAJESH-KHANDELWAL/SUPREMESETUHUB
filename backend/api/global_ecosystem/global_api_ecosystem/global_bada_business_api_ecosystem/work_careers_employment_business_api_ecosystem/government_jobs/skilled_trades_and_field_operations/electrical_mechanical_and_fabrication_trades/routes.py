"""Transport-neutral route handlers for Electrical, mechanical and fabrication trades."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "skilled_trades_and_field_operations", "specialization": "electrical_mechanical_and_fabrication_trades", "display_name": "Electrical, mechanical and fabrication trades"}
