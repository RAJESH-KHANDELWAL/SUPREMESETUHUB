"""AWS API Gateway family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsApiGatewayCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-API-GATEWAY-CORE-ECOSYSTEM"
