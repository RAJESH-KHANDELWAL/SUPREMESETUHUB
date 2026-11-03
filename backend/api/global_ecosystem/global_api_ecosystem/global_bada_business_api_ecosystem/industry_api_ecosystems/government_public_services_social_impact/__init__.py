"""Government, Public Services & Social Impact API Ecosystem."""
INDUSTRY_ID = "government_public_services_social_impact"
INDUSTRY_NAME = "Government, Public Services & Social Impact API Ecosystem"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import PublicImpactService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "PublicImpactService"]
