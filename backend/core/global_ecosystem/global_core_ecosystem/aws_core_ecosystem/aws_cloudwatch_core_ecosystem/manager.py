"""aws_cloudwatch_core_ecosystem product-family manager facade."""
from .service import AwsCloudwatchCoreService
class AwsCloudwatchCoreManager:
 def __init__(self)->None:self._service=AwsCloudwatchCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsCloudwatchCoreManager:return AwsCloudwatchCoreManager()
__all__=["AwsCloudwatchCoreManager","get_manager"]
