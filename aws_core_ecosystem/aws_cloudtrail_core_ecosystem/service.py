"""AWS CloudTrail family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsCloudtrailCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-CLOUDTRAIL-CORE-ECOSYSTEM"
