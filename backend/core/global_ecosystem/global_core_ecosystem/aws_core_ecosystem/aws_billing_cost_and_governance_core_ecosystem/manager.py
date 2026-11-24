"""Manager for the Billing, Cost and Governance AWS Core domain."""
from ..domain_runtime import AwsCoreDomainManager
class BillingCostAndGovernanceDomainManager(AwsCoreDomainManager):
 DOMAIN_ID="BILLING_COST_AND_GOVERNANCE"
def get_manager()->BillingCostAndGovernanceDomainManager:return BillingCostAndGovernanceDomainManager()
__all__=["BillingCostAndGovernanceDomainManager","get_manager"]
