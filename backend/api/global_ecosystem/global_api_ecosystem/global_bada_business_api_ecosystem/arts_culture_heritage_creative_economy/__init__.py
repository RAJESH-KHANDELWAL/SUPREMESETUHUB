"""Arts, Culture, Heritage & Creative Economy API ecosystem."""
INDUSTRY_ID = "arts_culture_heritage_creative_economy"
INDUSTRY_NAME = "Arts, Culture, Heritage & Creative Economy API Ecosystem"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"

from .service import ArtsCultureHeritageService

__all__ = ["INDUSTRY_ID", "INDUSTRY_NAME", "COVERAGE", "CHANNELS", "STATUS", "ArtsCultureHeritageService"]
