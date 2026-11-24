"""Public exports for aws_s3_storage_core_ecosystem."""
from .service import AwsS3StorageCoreService
from .manager import AwsS3StorageCoreManager,get_manager
__all__=["AwsS3StorageCoreService","AwsS3StorageCoreManager","get_manager"]
