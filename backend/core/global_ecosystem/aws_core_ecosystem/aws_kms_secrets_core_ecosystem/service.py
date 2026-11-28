"""AWS KMS and Secrets Manager family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsKmsSecretsCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-KMS-SECRETS-CORE-ECOSYSTEM"
