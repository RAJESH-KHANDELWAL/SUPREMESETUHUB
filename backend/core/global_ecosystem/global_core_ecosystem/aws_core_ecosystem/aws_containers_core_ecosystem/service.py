"""AWS Containers (ECS, EKS and ECR) family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsContainersCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-CONTAINERS-CORE-ECOSYSTEM"
