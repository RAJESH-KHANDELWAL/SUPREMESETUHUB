"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaFacebookPagesAndPublishingCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("FACEBOOK_PAGES_AND_PUBLISHING")
