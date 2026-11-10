"""Unified Work & Business API facade under Global Bada Business."""
from .routes import router
from .service import GlobalWorkBusinessAPIService
__all__ = ["router", "GlobalWorkBusinessAPIService"]
