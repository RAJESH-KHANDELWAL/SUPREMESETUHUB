"""aws_ec2_compute_core_ecosystem product-family manager facade."""
from .service import AwsEc2ComputeCoreService
class AwsEc2ComputeCoreManager:
 def __init__(self)->None:self._service=AwsEc2ComputeCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsEc2ComputeCoreManager:return AwsEc2ComputeCoreManager()
__all__=["AwsEc2ComputeCoreManager","get_manager"]
