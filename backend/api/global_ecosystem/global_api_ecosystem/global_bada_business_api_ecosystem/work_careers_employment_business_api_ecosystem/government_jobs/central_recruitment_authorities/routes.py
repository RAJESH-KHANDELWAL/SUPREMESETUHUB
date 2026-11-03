"""Framework-neutral route handlers for recruitment authority metadata."""
from .services import get_authority_directory_contract

def get_authorities_metadata() -> dict:
    return {"success": True, "data": get_authority_directory_contract()}
