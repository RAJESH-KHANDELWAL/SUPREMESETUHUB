"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaBusinessPortfolioAssetsCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("BUSINESS_PORTFOLIO_ASSETS")
