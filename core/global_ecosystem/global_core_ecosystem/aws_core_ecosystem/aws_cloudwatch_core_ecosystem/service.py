"""AWS CloudWatch family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsCloudwatchCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-CLOUDWATCH-CORE-ECOSYSTEM"
