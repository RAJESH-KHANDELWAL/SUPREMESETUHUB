"""aws_api_gateway_core_ecosystem product-family manager facade."""
from .service import AwsApiGatewayCoreService
class AwsApiGatewayCoreManager:
 def __init__(self)->None:self._service=AwsApiGatewayCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsApiGatewayCoreManager:return AwsApiGatewayCoreManager()
__all__=["AwsApiGatewayCoreManager","get_manager"]
