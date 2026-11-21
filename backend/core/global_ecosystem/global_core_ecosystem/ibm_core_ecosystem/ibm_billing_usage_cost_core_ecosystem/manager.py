"""Thin shared-runtime adapter for Billing, Usage and Cost."""
from ..domain_runtime import IBMCoreDomainManager
class IBMBillingUsageCostCoreManager(IBMCoreDomainManager):
    def __init__(self):
        super().__init__("BILLING_USAGE_COST")
