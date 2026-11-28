"""Manager for the PAYMENTS_BANKING_FINANCE integration domain."""
from ..domain_runtime import IntegrationDomainManager
class PaymentsBankingFinanceDomainManager(IntegrationDomainManager):
    DOMAIN_ID="PAYMENTS_BANKING_FINANCE"
def get_manager(): return PaymentsBankingFinanceDomainManager()
__all__=["PaymentsBankingFinanceDomainManager","get_manager"]
