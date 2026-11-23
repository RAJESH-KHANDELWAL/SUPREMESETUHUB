"""AWS EC2 Compute family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsEc2ComputeCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-EC2-COMPUTE-CORE-ECOSYSTEM"
