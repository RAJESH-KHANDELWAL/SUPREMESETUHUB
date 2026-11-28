"""PAYMENTS WALLET AND SUBSCRIPTIONS Google Core domain package."""
from .manager import PaymentsWalletDomainManager, get_manager

DOMAIN_ID = "PAYMENTS_WALLET_AND_SUBSCRIPTIONS"
__all__ = ["DOMAIN_ID", "PaymentsWalletDomainManager", "get_manager"]
