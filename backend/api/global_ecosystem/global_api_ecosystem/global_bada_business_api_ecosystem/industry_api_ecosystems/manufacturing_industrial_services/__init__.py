"""Manufacturing & Industrial Services domain."""
INDUSTRY_ID = "manufacturing_industrial_services"
INDUSTRY_NAME = "Manufacturing & Industrial Services"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import ManufacturingService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "ManufacturingService"]
