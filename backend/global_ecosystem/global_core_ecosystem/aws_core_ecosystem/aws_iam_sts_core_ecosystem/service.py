"""AWS IAM and STS family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsIamStsCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-IAM-STS-CORE-ECOSYSTEM"
