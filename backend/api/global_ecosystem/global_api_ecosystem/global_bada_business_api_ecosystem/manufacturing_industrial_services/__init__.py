"""Manufacturing, industrial, industries and factory-services ecosystem."""
INDUSTRY_ID = "manufacturing_industrial_services"
INDUSTRY_NAME = "Manufacturing, Industrial, Industries & Factory Services"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import ManufacturingService

__all__ = [
    "INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS",
    "STATUS", "ManufacturingService",
]
