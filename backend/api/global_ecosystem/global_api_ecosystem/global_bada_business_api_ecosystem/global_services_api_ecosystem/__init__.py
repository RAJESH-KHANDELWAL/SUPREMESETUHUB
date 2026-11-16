"""GLOBAL SERVICES API ECOSYSTEM package."""
from .routes import router
from .service import GlobalServicesAPIService
__all__ = ["router", "GlobalServicesAPIService"]
