"""Manager for the ADULT_PAYMENTS_PAYOUTS integration domain."""
from ..domain_runtime import IntegrationDomainManager
class AdultPaymentsPayoutsDomainManager(IntegrationDomainManager):
    DOMAIN_ID="ADULT_PAYMENTS_PAYOUTS"
def get_manager(): return AdultPaymentsPayoutsDomainManager()
__all__=["AdultPaymentsPayoutsDomainManager","get_manager"]
