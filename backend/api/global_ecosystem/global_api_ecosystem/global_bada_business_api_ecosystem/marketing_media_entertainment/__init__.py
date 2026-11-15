"""Marketing, Media & Entertainment industry API domain package."""

INDUSTRY_ID = "marketing_media_entertainment"
INDUSTRY_NAME = "Marketing, Media & Entertainment"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import MarketingMediaEntertainmentService

__all__ = [
    "INDUSTRY_ID",
    "INDUSTRY_NAME",
    "COVERAGE",
    "CHANNELS",
    "STATUS",
    "MarketingMediaEntertainmentService",
]
