"""AWS Database (RDS, Aurora and DynamoDB) family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsDatabaseCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-DATABASE-CORE-ECOSYSTEM"
