"""Transport-neutral route handlers for Plant, vehicle and equipment operator posts."""
from .services import register_post

def create_government_post(payload):
    return register_post(payload)

def get_specialization_metadata():
    return {"job_family": "skilled_trades_and_field_operations", "specialization": "plant_vehicle_and_equipment_operators", "display_name": "Plant, vehicle and equipment operator posts"}
