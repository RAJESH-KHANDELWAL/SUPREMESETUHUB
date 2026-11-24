"""AWS Lambda family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsLambdaCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-LAMBDA-CORE-ECOSYSTEM"
