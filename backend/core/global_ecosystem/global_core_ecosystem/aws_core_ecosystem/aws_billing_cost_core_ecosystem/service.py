"""AWS Billing and Cost Management family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsBillingCostCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-BILLING-COST-CORE-ECOSYSTEM"
