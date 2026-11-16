"""AWS Route 53 DNS family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsRoute53DnsCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-ROUTE53-DNS-CORE-ECOSYSTEM"
