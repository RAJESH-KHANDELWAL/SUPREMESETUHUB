"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaThreadsSocialNetworkCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("THREADS_SOCIAL_NETWORK")
