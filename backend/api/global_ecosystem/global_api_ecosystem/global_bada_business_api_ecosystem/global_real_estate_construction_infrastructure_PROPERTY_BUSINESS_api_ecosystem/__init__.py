"""Real Estate & Construction domain package."""
INDUSTRY_ID = "real_estate_construction"
INDUSTRY_NAME = "Real Estate & Construction"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import RealEstateService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "RealEstateService"]
