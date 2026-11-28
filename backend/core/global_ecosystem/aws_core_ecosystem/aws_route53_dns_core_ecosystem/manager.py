"""aws_route53_dns_core_ecosystem product-family manager facade."""
from .service import AwsRoute53DnsCoreService
class AwsRoute53DnsCoreManager:
 def __init__(self)->None:self._service=AwsRoute53DnsCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsRoute53DnsCoreManager:return AwsRoute53DnsCoreManager()
__all__=["AwsRoute53DnsCoreManager","get_manager"]
