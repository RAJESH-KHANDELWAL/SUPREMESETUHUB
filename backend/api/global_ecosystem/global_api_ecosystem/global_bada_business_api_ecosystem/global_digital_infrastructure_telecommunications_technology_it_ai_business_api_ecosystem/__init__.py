"""Global Digital Infrastructure, Telecommunications, Technology, IT & AI API Ecosystem."""
from pathlib import Path as _Path
from .digital_infrastructure_telecommunications import *
_BASE = _Path(__file__).resolve().parent
__path__ = [str(_BASE), str(_BASE / "digital_infrastructure_telecommunications")]
DOMAIN_ID = "global_digital_infrastructure_telecommunications_technology_it_ai"
DOMAIN_NAME = "Global Digital Infrastructure, Telecommunications, Technology, IT & AI API Ecosystem"
COVERAGE_SCOPE = ("bharat", "global")
CATEGORY_PACKAGES = (
    "digital_infrastructure_telecommunications",
    "technology_it_telecommunications",
    "technology_software_ai_cloud",
    "apple_business_api_ecosystem",
    "aws_business_api_ecosystem",
    "google_business_api_ecosystem",
    "ibm_business_api_ecosystem",
    "microsoft_business_api_ecosystem",
    "oracle_business_api_ecosystem",
)
