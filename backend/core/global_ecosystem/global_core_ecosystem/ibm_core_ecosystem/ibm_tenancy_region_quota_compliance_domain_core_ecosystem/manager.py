"""Thin adapter over the shared read-only IBM domain runtime."""
from ..domain_runtime import IBMCoreDomainManager
class IBMTenancyRegionQuotaComplianceCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("TENANCY_REGION_QUOTA_COMPLIANCE")
