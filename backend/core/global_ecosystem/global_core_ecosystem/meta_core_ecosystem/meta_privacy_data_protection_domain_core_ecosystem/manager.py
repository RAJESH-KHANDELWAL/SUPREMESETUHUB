"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaPrivacyDataProtectionCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("PRIVACY_DATA_PROTECTION")
