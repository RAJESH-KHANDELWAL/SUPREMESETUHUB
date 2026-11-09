"""Independent API resource package for the temporary_staffing track."""
from .categories import TRACK_ID, get_track_definition
from .services import get_track_api_resource, get_track_status

__all__ = ["TRACK_ID", "get_track_definition", "get_track_api_resource", "get_track_status"]
