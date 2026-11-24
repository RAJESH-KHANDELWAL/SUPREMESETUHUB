"""aws_containers_core_ecosystem product-family manager facade."""
from .service import AwsContainersCoreService
class AwsContainersCoreManager:
 def __init__(self)->None:self._service=AwsContainersCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsContainersCoreManager:return AwsContainersCoreManager()
__all__=["AwsContainersCoreManager","get_manager"]
