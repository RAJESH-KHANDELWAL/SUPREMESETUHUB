"""Agriculture, Food & Natural Resources industry API domain package."""

INDUSTRY_ID = "agriculture_food_natural_resources"
INDUSTRY_NAME = "Agriculture, Food & Natural Resources"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import AgricultureFoodService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "AgricultureFoodService"]
