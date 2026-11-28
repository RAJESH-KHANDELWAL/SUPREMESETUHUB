"""Thin adapter over the shared read-only Meta domain runtime."""
from ..domain_runtime import MetaCoreDomainManager
class MetaTenantAccountAssetGovernanceCoreManager(MetaCoreDomainManager):
    def __init__(self):
        super().__init__("TENANT_ACCOUNT_ASSET_GOVERNANCE")
