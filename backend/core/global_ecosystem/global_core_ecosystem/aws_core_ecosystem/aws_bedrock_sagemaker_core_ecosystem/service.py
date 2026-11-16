"""AWS Bedrock and SageMaker AI family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsBedrockSagemakerCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-BEDROCK-SAGEMAKER-CORE-ECOSYSTEM"
