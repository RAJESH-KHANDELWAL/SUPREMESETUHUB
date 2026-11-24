"""Compatibility facade for SERVER API tools catalog."""
from .service import list_entries
FOLDER_NAME = "tools"
__all__ = ["FOLDER_NAME", "list_entries"]
