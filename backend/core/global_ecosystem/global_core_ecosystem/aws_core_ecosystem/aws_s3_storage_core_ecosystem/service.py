"""AWS S3 Storage family-specific Core service."""
from ..module_service import AwsProductCoreService

class AwsS3StorageCoreService(AwsProductCoreService):
    ECOSYSTEM_ID = "AWS-S3-STORAGE-CORE-ECOSYSTEM"
