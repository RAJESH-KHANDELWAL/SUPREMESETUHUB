"""aws_iam_sts_core_ecosystem product-family manager facade."""
from .service import AwsIamStsCoreService
class AwsIamStsCoreManager:
 def __init__(self)->None:self._service=AwsIamStsCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsIamStsCoreManager:return AwsIamStsCoreManager()
__all__=["AwsIamStsCoreManager","get_manager"]
