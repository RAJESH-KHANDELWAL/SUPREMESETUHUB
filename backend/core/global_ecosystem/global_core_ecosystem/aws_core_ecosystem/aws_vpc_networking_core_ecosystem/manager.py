"""aws_vpc_networking_core_ecosystem product-family manager facade."""
from .service import AwsVpcNetworkingCoreService
class AwsVpcNetworkingCoreManager:
 def __init__(self)->None:self._service=AwsVpcNetworkingCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsVpcNetworkingCoreManager:return AwsVpcNetworkingCoreManager()
__all__=["AwsVpcNetworkingCoreManager","get_manager"]
