"""Manager for the PAYMENTS_WALLET_AND_SUBSCRIPTIONS Google Core domain."""
from ..domain_runtime import GoogleCoreDomainManager


class PaymentsWalletDomainManager(GoogleCoreDomainManager):
    DOMAIN_ID = "PAYMENTS_WALLET_AND_SUBSCRIPTIONS"


def get_manager() -> PaymentsWalletDomainManager:
    return PaymentsWalletDomainManager()


__all__ = ["PaymentsWalletDomainManager", "get_manager"]
