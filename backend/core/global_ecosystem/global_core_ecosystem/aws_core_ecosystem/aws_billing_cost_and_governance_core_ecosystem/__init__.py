"""Billing, Cost and Governance AWS Core domain package."""
from .manager import BillingCostAndGovernanceDomainManager,get_manager
DOMAIN_ID="BILLING_COST_AND_GOVERNANCE"
__all__=["DOMAIN_ID","BillingCostAndGovernanceDomainManager","get_manager"]
