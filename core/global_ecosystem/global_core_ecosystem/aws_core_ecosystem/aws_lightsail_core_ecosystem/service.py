"""AWS Lightsail family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsLightsailCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-LIGHTSAIL-CORE-ECOSYSTEM"
