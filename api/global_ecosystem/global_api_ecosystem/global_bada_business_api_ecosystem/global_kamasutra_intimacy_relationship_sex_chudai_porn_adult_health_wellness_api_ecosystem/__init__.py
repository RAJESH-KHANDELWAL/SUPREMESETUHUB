"""Standalone Kamasutra, intimacy, relationship, adult health and wellness API ecosystem."""
from .routes import router
from .service import AdultWellnessEcosystemService

__all__ = ["router", "AdultWellnessEcosystemService"]
