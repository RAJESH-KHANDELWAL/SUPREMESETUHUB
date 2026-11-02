"""Professional, Legal & Business Services industry API domain package."""
INDUSTRY_ID = "professional_legal_business_services"
INDUSTRY_NAME = "Professional, Legal & Business Services"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import ProfessionalServicesService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "ProfessionalServicesService"]
