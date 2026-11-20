"""Adult Payments & Payouts domain package."""
from .manager import AdultPaymentsPayoutsDomainManager, get_manager
DOMAIN_ID="ADULT_PAYMENTS_PAYOUTS"
__all__=["DOMAIN_ID","AdultPaymentsPayoutsDomainManager","get_manager"]
