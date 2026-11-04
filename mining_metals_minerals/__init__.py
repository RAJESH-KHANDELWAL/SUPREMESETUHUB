"""Mining, Metals & Minerals industry API domain package."""
INDUSTRY_ID = "mining_metals_minerals"
INDUSTRY_NAME = "Mining, Metals & Minerals"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import MiningMetalsService
__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "MiningMetalsService"]
