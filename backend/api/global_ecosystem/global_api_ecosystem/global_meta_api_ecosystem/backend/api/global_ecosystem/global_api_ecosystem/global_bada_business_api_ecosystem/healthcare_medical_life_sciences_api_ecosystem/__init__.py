"""Healthcare, medical, life sciences and total wellness API ecosystem."""
from .routes import router
from .service import HealthcareMedicalLifeSciencesService

__all__ = ["router", "HealthcareMedicalLifeSciencesService"]
