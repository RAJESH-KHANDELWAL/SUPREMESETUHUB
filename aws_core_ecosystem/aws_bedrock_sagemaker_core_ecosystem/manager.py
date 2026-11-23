"""aws_bedrock_sagemaker_core_ecosystem product-family manager facade."""
from .service import AwsBedrockSagemakerCoreService
class AwsBedrockSagemakerCoreManager:
 def __init__(self)->None:self._service=AwsBedrockSagemakerCoreService()
 def status(self):return self._service.status()
 def capabilities(self):return self._service.capabilities()
 def authorize_capability(self,capability,context=None):return self._service.authorize_capability(capability,context)
def get_manager()->AwsBedrockSagemakerCoreManager:return AwsBedrockSagemakerCoreManager()
__all__=["AwsBedrockSagemakerCoreManager","get_manager"]
