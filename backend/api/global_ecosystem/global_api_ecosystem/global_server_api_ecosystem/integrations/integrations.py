"""Compatibility facade for SERVER integration catalog."""
from .service import list_entries
FOLDER_NAME = "integrations"
__all__ = ["FOLDER_NAME", "list_entries"]
