"""aws_kms_secrets_core_ecosystem product-family manager facade."""
from .service import AwsKmsSecretsCoreService
class AwsKmsSecretsCoreManager:
 def __init__(self)->None:self._service=AwsKmsSecretsCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsKmsSecretsCoreManager:return AwsKmsSecretsCoreManager()
__all__=["AwsKmsSecretsCoreManager","get_manager"]
