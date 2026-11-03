"""Full-name public entry point for the Kamasutra / Adult Wellness API Ecosystem."""
from .catalog import CATEGORIES
from .routes import router
from .service import AdultWellnessEcosystemService

__all__ = ["CATEGORIES", "router", "AdultWellnessEcosystemService"]
