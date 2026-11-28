"""aws_cloudtrail_core_ecosystem product-family manager facade."""
from .service import AwsCloudtrailCoreService
class AwsCloudtrailCoreManager:
 def __init__(self)->None:self._service=AwsCloudtrailCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsCloudtrailCoreManager:return AwsCloudtrailCoreManager()
__all__=["AwsCloudtrailCoreManager","get_manager"]
