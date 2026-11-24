"""Oracle company profile adapter package."""
from .routes import router
from .service import get_profile, get_sources, get_adapter_status
__all__ = ["router", "get_profile", "get_sources", "get_adapter_status"]
