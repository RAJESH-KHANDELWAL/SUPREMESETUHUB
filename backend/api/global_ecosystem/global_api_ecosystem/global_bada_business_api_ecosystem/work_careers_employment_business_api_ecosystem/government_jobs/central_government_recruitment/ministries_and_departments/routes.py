"""Framework-neutral metadata handlers for ministry/department directory."""
from .services import get_directory_contract

def get_ministries_and_departments_metadata() -> dict:
    return {"success": True, "data": get_directory_contract()}
