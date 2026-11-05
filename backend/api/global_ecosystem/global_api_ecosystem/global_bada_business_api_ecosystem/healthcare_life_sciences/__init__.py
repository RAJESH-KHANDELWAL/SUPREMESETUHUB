"""Healthcare & Life Sciences industry API domain package."""
INDUSTRY_ID = "healthcare_life_sciences"
INDUSTRY_NAME = "Healthcare & Life Sciences"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import HealthcareService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "HealthcareService"]
