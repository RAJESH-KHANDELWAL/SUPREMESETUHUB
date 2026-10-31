"""Supply Chain, Warehousing & Distribution domain package."""
INDUSTRY_ID = "supply_chain_warehousing_distribution"
INDUSTRY_NAME = "Supply Chain, Warehousing & Distribution"
COVERAGE = ("india", "global")
CHANNELS = ("online", "offline", "hybrid")
STATUS = "taxonomy_scaffold"
from .service import SupplyChainDistributionService
