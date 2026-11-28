"""AWS CloudFormation family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsCloudformationCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-CLOUDFORMATION-CORE-ECOSYSTEM"
