"""Payments, Banking & Finance domain package."""
from .manager import PaymentsBankingFinanceDomainManager, get_manager
DOMAIN_ID="PAYMENTS_BANKING_FINANCE"
__all__=["DOMAIN_ID","PaymentsBankingFinanceDomainManager","get_manager"]
