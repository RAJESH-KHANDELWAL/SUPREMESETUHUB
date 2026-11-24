"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMCloudAccountResourceGovernanceCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("CLOUD_ACCOUNT_RESOURCE_GOVERNANCE")
