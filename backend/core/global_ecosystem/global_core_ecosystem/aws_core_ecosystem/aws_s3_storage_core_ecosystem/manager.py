"""aws_s3_storage_core_ecosystem product-family manager facade."""
from .service import AwsS3StorageCoreService
class AwsS3StorageCoreManager:
 def __init__(self)->None:self._service=AwsS3StorageCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsS3StorageCoreManager:return AwsS3StorageCoreManager()
__all__=["AwsS3StorageCoreManager","get_manager"]
