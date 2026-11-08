"""Compatibility facade for server service catalog."""
from .service import list_entries
FOLDER_NAME = "services"
__all__ = ["FOLDER_NAME", "list_entries"]
