"""Independent API resource package for the senior_specialist_roles track."""
from .categories import TRACK_ID, get_track_definition
from .services import get_track_api_resource, get_track_status

__all__ = ["TRACK_ID", "get_track_definition", "get_track_api_resource", "get_track_status"]
