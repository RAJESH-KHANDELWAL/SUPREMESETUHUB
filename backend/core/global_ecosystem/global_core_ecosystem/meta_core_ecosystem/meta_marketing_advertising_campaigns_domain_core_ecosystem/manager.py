"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaMarketingAdvertisingCampaignsCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("MARKETING_ADVERTISING_CAMPAIGNS")
