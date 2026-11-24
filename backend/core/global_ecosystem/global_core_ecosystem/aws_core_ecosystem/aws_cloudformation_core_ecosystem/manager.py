"""aws_cloudformation_core_ecosystem product-family manager facade."""
from .service import AwsCloudformationCoreService
class AwsCloudformationCoreManager:
 def __init__(self)->None:self._service=AwsCloudformationCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsCloudformationCoreManager:return AwsCloudformationCoreManager()
__all__=["AwsCloudformationCoreManager","get_manager"]
