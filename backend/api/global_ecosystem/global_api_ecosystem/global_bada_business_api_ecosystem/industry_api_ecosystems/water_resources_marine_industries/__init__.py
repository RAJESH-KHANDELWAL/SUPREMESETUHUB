"""Water Resources & Marine Industries domain package."""
INDUSTRY_ID = "water_resources_marine_industries"
INDUSTRY_NAME = "Water Resources & Marine Industries"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import WaterMarineService
